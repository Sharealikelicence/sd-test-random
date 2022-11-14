# sD Test

Monorepo for random number generating MQTT test.

## Notes/Assumptions

I have intentionally not enabled encryption since it is not sensitive data and to make it easier to try out/review. This could easily be done by generating certificates and then providing the appropriate configuration options.

I have also made the sample config files and instructions here for running on the same host machine but these could be easily changed for a production environment.

## Structure

This repo consists of 3 main sections:
* A python based MQTT client for publishing and subscribing to topics (`./mqtt_client`)
* A web app for viewing published random values (`./web-app`)
* Configuration files for spinning up a Mosquitto MQTT broker (`./broker`)

## Running

### Docker

**NOTE**: This is untested on a Windows host machine.

#### Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/)

#### Broker

See it's [README](./broker/README.md).

#### Web App

For Unix based host:
```shell
cd ./web-app
cp config.sample.json config.json
DOCKER_BUILDKIT=1 docker build -t sd-random-webapp . && \
  docker run \
    -i \
    --rm \
    --net=host \
    --name=sd-random-webapp \
    sd-random-webapp
```

For Windows, do not execute the `cp` step. Either copy manually or use `xcopy`, etc.

### Alternative Options

The web app and python MQTT clients may be run from the command line. See their readme files for more information.

**NOTE**: Remember to execute their commands from within their main project folders. As in `./mqtt_client` or `./web-app`.

It is also possible to install a Mosquitto broker and copy the Brokers sample config file in `/broker` using the [official installation instructions](https://mosquitto.org/download/).
