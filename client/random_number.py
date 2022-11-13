from typing import Any, Callable
import paho.mqtt.client as mqtt

from util import BoundedRandom

class RandomNumberClient():
    __client: mqtt.Client
    __topic_prefix: str
    __random_gen: BoundedRandom

    def __init__(self, host: str, port: str = 1883, keepalive: int = 60, client_id: str = None, clean_session: bool = None, userdata: Any = None, protocol: int = mqtt.MQTTv311,
                transport: str = 'tcp', reconnect_on_failure: bool = True,
                domain: str = 'sdtest', name: str = 'random', generator_func: Callable[[float, float], float] = None, on_publish: Callable[[mqtt.Client, Any, int], None] = None) -> None:
        self.__client = mqtt.Client(client_id, clean_session, userdata, protocol, transport, reconnect_on_failure)
        if on_publish:
            self.__client.on_publish = on_publish

        self.__topic_prefix = f"{domain}/{name}"
        self.__random_gen = BoundedRandom(generator_func)

        # Connect to and start client.
        self.__client.connect(host, port, keepalive)
        # Using blocking loop since it is a simple implementation.
        self.__client.loop_forever()


    def publish(self, topic: str = 'number', lower: float = 1, upper: float = 100) -> None:
        print('Publishing...')
        self.__client.publish(f"{self.__topic_prefix}/{topic}", self.__random_gen.float(lower, upper))
