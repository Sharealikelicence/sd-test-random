import { useState, memo } from 'react';

import config from './config';
import MqttClient from './services/mqtt/client';
import BoxView from './components/BoxView/BoxView';

import './App.css';

const mqttClient = new MqttClient(config.mqtt);

const MAX_HEIGHT = 100

/**
 * Creates a component that annimates an svg boxes height depending on a number that was published to an MQTT broker.
 * @returns The React functional component.
 */
function App() {
  const [currentNumber, setCurrentNumber] = useState(0);

  // Set handler for receiving published messages.
  mqttClient.client.onMessageArrived = (message) => {
    // Try to convert payload to a number, if it fails just use zero.
    const payload = Number(message.payloadString);
    setCurrentNumber(isNaN(payload) ? 0 : payload);
  };
  
  return (
    <div className="App">
      <span><strong>Current Number</strong>: {currentNumber}</span>
      <br/>
      <BoxView maxHeight={MAX_HEIGHT} height={currentNumber} />
    </div>
  );
}

export default memo(App);
