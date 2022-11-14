from typing import Any, Callable
import paho.mqtt.client as mqtt

from client.base import BaseClient
from util.bounded_random import BoundedRandom


class RandomNumberClient(BaseClient):
    """
    A convenience class for setup and running of an MQTT client that can publish a random number to a broker.
    """
    __random_gen: BoundedRandom

    def __init__(self, host: str, port: str = 1883, keepalive: int = 60, client_id: str = None, clean_session: bool = None,
                 userdata: Any = None, protocol: int = mqtt.MQTTv311, transport: str = 'tcp', reconnect_on_failure: bool = True,
                 subscribe_props: dict = None, domain: str = 'sdtest', name: str = 'random',
                 on_publish: Callable[[mqtt.Client, Any, int], None] = None, on_message: Callable[[mqtt.Client, Any, str], None] = None,
                 generator_func: Callable[[float, float], float] = None) -> None:
        """
        A convenience class for setup and running of an MQTT client that can publish a random number to a broker.

        Args:
            host (str): THe host address for the MQTT broker.
            port (str, optional): The port that the client should communicate on. Defaults to 1883.
            keepalive (int, optional): Maximum period in seconds allowed between communications with the broker. If no other messages are being exchanged,
                                       this controls the rate at which the client will send ping messages to the broker. Defaults to 60.
            client_id (str, optional): The unique client id string used when connecting to the broker. If client_id is zero length or None,
                                       then one will be randomly generated. In this case the clean_session parameter must be True.. Defaults to None.
            clean_session (bool, optional): A boolean that determines the client type. If True, the broker will remove all information about this client
                                            when it disconnects. If False, the client is a durable client and subscription information and queued messages
                                            will be retained when the client disconnects. Defaults to None.
                                            Note that a client will never discard its own outgoing messages on disconnect. Calling connect() or reconnect()
                                            will cause the messages to be resent. Use reinitialise() to reset a client to its original state.
            userdata (Any, optional): User defined data of any type that is passed as the userdata parameter to callbacks. It may be updated at a later
                                      point with the user_data_set() function.. Defaults to None.
            protocol (int, optional): The version of the MQTT protocol to use for this client. Can be either MQTTv31 or MQTTv311. Defaults to mqtt.MQTTv311.
            transport (str, optional): Set to "websockets" to send MQTT over WebSockets. Leave at the default of "tcp" to use raw TCP.. Defaults to 'tcp'.
            reconnect_on_failure (bool, optional): Whether or not loop_forever() will handle reconnecting automatically. Defaults to True.
            subscribe_props ({'topic': str, 'qos': int}, optional): The topic suffix (fully qualitifed topic will end up in the form {domain}/{name}/{topic})
                                                                    and MQTT QoS values used to subsribe to an initial topic. Further topics can be subscribed
                                                                    to by using the `client` property. Defaults to None.
            domain (str, optional): The domain that the client applies to. Used to construct the MQTT topic in the form {domain}/{name}/{topic}. Defaults to 'sdtest'.
            name (str, optional): The name to give to the client. Used to construct the MQTT topic in the form {domain}/{name}/{topic}. Defaults to 'random'.
            on_publish (Callable[[mqtt.Client, Any, int], None], optional): Callback for when a message that was to be sent using the client.publish() call
                                                                            has completed transmission to the broker. For messages with QoS levels 1 and 2, this
                                                                            means that the appropriate handshakes have completed. For QoS 0, this simply means
                                                                            that the message has left the client. The mid variable matches the mid variable
                                                                            returned from the corresponding publish() call, to allow outgoing messages to be tracked.
                                                                            This callback is important because even if the publish() call returns success, it does
                                                                            not always mean that the message has been sent. Defaults to None.
            on_message (Callable[[mqtt.Client, Any, str], None], optional): Callback for when a message has been received on a topic that the client subscribes
                                                                            to and the message does not match an existing topic filter callback.
                                                                            Use message_callback_add() to define a callback that will be called for specific
                                                                            topic filters. on_message will serve as fallback when none matched. Defaults to None.
            generator_func (Callable[[float, float], float]): The undelying random number generating function used for creating the random number that are to
                                                              be published. THe built in random.uniform function will be used if nothing is provided.
                                                              Defaults to None.
        """
        self.__random_gen = BoundedRandom(generator_func)
        super().__init__(host, port, keepalive, client_id, clean_session, userdata, protocol, transport, reconnect_on_failure, 
                        subscribe_props, domain, name, on_publish, on_message)


    def publish(self, topic_suffix: str = 'number', lower: float = 1, upper: float = 100) -> None:
        """
        Publishes a random number to the broker. Defaults to publishing floats between the interval [lower, upper).
        This can be changed by providing a different `generator_func` when instantiating the class.

        Args:
            topic_suffix (str, optional): The topic suffix to publish to.
                                          The fully qualified topic will be of the form {domain}/{name}/{topic}. Where domain and name are set when instantiating class.
                                          Defaults to 'number'. Full topic defaults to sdtest/random/number.
            lower (float, optional): _description_. Defaults to 1.
            upper (float, optional): _description_. Defaults to 100.
        """
        full_topic = f"{self.topic_prefix}/{topic_suffix}"
        print(f"{full_topic}: Publishing...")
        self.client.publish(full_topic, self.__random_gen.float(lower, upper))
