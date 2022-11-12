# sd Test - Broker

MQTT Test Broker.

## Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/)

## Configuration

Create a configuration file, based off of the `mosquitto.sample.conf` file and name it `mosquitto.conf`. For configuration options, see the [official documentation](https://hub.docker.com/_/eclipse-mosquitto)

## Spin Up

For a Unix base host:

```shell
docker run -it -p 1883:1883 -p 9001:9001 -v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```

For a Windows based host `$PWD` must be an absolute path to the `/broker` directory.
