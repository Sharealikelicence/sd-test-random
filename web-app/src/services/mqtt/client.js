import Paho from 'paho-mqtt';
import { MakeRandomId } from '../../utils/random';


class MqttClient {
  constructor({subscriptions, ...config}) {
    this.subscriptions = subscriptions;
    // If clientId isn't provided, just generate a random one.
    this.client = new Paho.Client(config.hostname, Number(config.port), '', config?.clientId ?? MakeRandomId(23));

    // Set callback handlers
    this.client.onConnectionLost = this.onConnectionLost;
    this.client.onMessageArrived = this.onMessageArrived;

    // Connect to the broker.
    this.client.connect({ onSuccess: this.onConnect.bind(this) });
  }

  connect(connectionOptions) {
    // Connect to the broker.
    this.client.connect(connectionOptions ?? { onSuccess: this.onConnect });
  }

  onConnect() {
    console.log("Connected to host.", {subscriptions:this.subscriptions});

    for (const topic of this.subscriptions) {
      console.log('Subscribing to topic: ' + topic);
      this.client.subscribe(topic);
    }
  }

  onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("Connection lost with error: " + responseObject.errorMessage);
    }
  }

  onMessageArrived(message) {
    console.log("Message arrived: " + message.payloadString);
  }

  publish(message) {
    this.client.send(message);
  }
}

export default MqttClient;
