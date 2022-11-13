# sd Test - Broker

MQTT Test Broker.

## Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/)

## Configuration

Create a configuration file, based off of the `mosquitto.sample.conf` file and name it `mosquitto.conf`. For configuration options, see the [official documentation](https://hub.docker.com/_/eclipse-mosquitto)

## Spin Up

For a Unix base host:

```shell
docker run -it --net=host -v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```

For a Windows based host `$PWD` must be an absolute path to the `/broker` directory.
