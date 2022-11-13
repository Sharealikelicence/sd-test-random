from typing import Any, Callable
import paho.mqtt.client as mqtt

from client.base import BaseClient
from util.bounded_random import BoundedRandom


class RandomNumberClient(BaseClient):
    __random_gen: BoundedRandom

    def __init__(self, host: str, port: str = 1883, keepalive: int = 60, client_id: str = None, clean_session: bool = None,
                 userdata: Any = None, protocol: int = mqtt.MQTTv311, transport: str = 'tcp', reconnect_on_failure: bool = True,
                 subscribe_props: dict = None, domain: str = 'sdtest', name: str = 'random',
                 on_publish: Callable[[mqtt.Client, Any, int], None] = None, on_message: Callable[[mqtt.Client, Any, str], None] = None,
                 generator_func: Callable[[float, float], float] = None) -> None:
        self.__random_gen = BoundedRandom(generator_func)
        super().__init__(host, port, keepalive, client_id, clean_session, userdata, protocol, transport, reconnect_on_failure, 
                        subscribe_props, domain, name, on_publish, on_message)


    def publish(self, topic: str = 'number', lower: float = 1, upper: float = 100) -> None:
        full_topic = f"{self.topic_prefix}/{topic}"
        print(f"{full_topic}: Publishing...")
        self.client.publish(full_topic, self.__random_gen.float(lower, upper))
