# sD Test

Monorepo for random number generating MQTT test. This is a solution to the ST-FullStack problem.

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

**NOTE**: This is untested on a Windows host machine. For Windows, do not execute the `cp` steps. Either copy manually or use `xcopy`, etc.

#### Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/)

#### MQTT Broker

See broker [README](./broker/README.md).

#### MQTT Client(s)

For publishing client:

```shell
cd mqtt_client
DOCKER_BUILDKIT=1 docker build -t sd-client-random . && \
  docker run \
    -i \
    --rm \
    --net=host \
    -e CONFIG_PATH=config.pub.sample.json \
    sd-client-random
```

For subscribing client change `-e CONFIG_PATH=config.pub.sample.json \` to `-e CONFIG_PATH=config.sub.sample.json \`. Also, change `-i \` to `-it \` so that console output can be seen.

See client [README](./mqtt_client/README.md) for any more details.

#### Web App

For Unix based host:
```shell
cd ./web-app
cp config.sample.json config.json
DOCKER_BUILDKIT=1 docker build -t sd-random-webapp . && \
  docker run \
    -d \
    --rm \
    --net=host \
    --name=sd-random-webapp \
    sd-random-webapp
```

Using a browser on the host machine, navigate to `http://localhost:3000`.

**NOTE** The node does not like running with PID 1 (as in a docker container) hence why running in detached mode (`-d`) as it could not respond to signals like `Ctrl+C` or `SIGINT` . To stop type:
```shell
docker container stop sd-random-webapp
```

### Alternative Options

The web app and python MQTT clients may be run from the command line. See their readme files for more information.

**NOTE**: Remember to execute their commands from within their main project folders. As in `./mqtt_client` or `./web-app`.

It is also possible to install a Mosquitto broker and copy the Brokers sample config file in `/broker` using the [official installation instructions](https://mosquitto.org/download/).
