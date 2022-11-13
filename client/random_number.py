from typing import Any, Callable
import paho.mqtt.client as mqtt

from util.bounded_random import BoundedRandom


class RandomNumberClient():
    __client: mqtt.Client
    __topic_prefix: str
    __random_gen: BoundedRandom

    def __init__(self, host: str, port: str = 1883, keepalive: int = 60, client_id: str = None, clean_session: bool = None, userdata: Any = None, protocol: int = mqtt.MQTTv311,
                 transport: str = 'tcp', reconnect_on_failure: bool = True, do_subscribe: bool = False,
                 domain: str = 'sdtest', name: str = 'random', generator_func: Callable[[float, float], float] = None, on_publish: Callable[[mqtt.Client, Any, int], None] = None) -> None:
        self.__client = mqtt.Client(client_id, clean_session, userdata, protocol, transport, reconnect_on_failure)
        if on_publish:
            self.__client.on_publish = on_publish
        self.__client.on_connect = self.__on_connect(do_subscribe)

        self.__topic_prefix = f"{domain}/{name}"
        self.__random_gen = BoundedRandom(generator_func)

        # Connect to and start client.
        self.__client.connect(host, port, keepalive)

    def __on_connect(self, do_subscribe: bool):
        def on_connect(client, userdata, flags, rc):
            print(f"Connected with result code {str(rc)}")
            if (do_subscribe):
                client.subscribe(f"{self.__topic_prefix}/#")
        return on_connect

    def publish(self, topic: str = 'number', lower: float = 1, upper: float = 100) -> None:
        full_topic = f"{self.__topic_prefix}/{topic}"
        print(f"{full_topic}: Publishing...")
        self.__client.publish(full_topic, self.__random_gen.float(lower, upper))

    def loop_forever(self, retry_first_connection: bool = False):
        self.__client.loop_forever(
            retry_first_connection=retry_first_connection)
