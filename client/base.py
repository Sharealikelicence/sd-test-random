from typing import Any, Callable
from datetime import datetime
import paho.mqtt.client as mqtt


class BaseClient():
    __client: mqtt.Client
    __topic_prefix: str

    def __init__(self, host: str, port: str = 1883, keepalive: int = 60, client_id: str = None, clean_session: bool = None,
                 userdata: Any = None, protocol: int = mqtt.MQTTv311, transport: str = 'tcp', reconnect_on_failure: bool = True,
                 subscribe_props: dict = None, domain: str = 'sdtest', name: str = 'random',
                 on_publish: Callable[[mqtt.Client, Any, int], None] = None, on_message: Callable[[mqtt.Client, Any, str], None] = None) -> None:
        self.__client = mqtt.Client(client_id, clean_session, userdata, protocol, transport, reconnect_on_failure)
        if on_publish:
            self.__client.on_publish = on_publish
        self.__client.on_message = on_message if on_message else self.__on_message
        self.__client.on_connect = self.__get_on_connect(subscribe_props)

        self.__topic_prefix = f"{domain}/{name}"

        # Connect to and start client.
        self.__client.connect(host, port, keepalive)

    def __get_on_connect(self, subscribe_props: dict) -> Callable[[mqtt.Client, Any, dict, mqtt.ReasonCodes, mqtt.Properties], None]:
        def on_connect(client, userdata, flags, rc, props = None):
            print(f"Connected with result code {str(rc)}")
            if (subscribe_props):
                # Haven't worried about subscribing to multiple topics here as user could easily use the `client` property below if needed.
                topic = subscribe_props.get('topic')
                full_topic = f"{self.__topic_prefix}/{topic}" if topic else self.__topic_prefix
                print(f"Subscribing to {full_topic}")
                client.subscribe(full_topic, subscribe_props.get('qos', 0) or 0)
        return on_connect


    def __on_message(self, client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
        # Haven't made any of this method configurable as it could easily be overridden on instantiation.
        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")
        print(f"[{message.topic}] {now}: {message.payload.decode('UTF-8')}")


    @property
    def topic_prefix(self):
        return self.__topic_prefix


    @property
    def client(self):
        return self.__client


    def loop_forever(self, retry_first_connection: bool = False) -> None:
        self.__client.loop_forever(
            retry_first_connection=retry_first_connection)
