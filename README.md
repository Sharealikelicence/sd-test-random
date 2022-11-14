# sD Test

Monorepo for random number generating MQTT test.

I have intentionally not enabled encryption since it is not sensitive data and to make it easier to try out/review. This could easily be done by generating certificates and then providing the appropriate configuration options.

## Structure

This repo consists of 3 main sections:
* A python based MQTT client for publishing and subscribing to topics (`./mqtt_client`)
* A web app for viewing published random values (`./web-app`)
* Configuration files for spinning up a Mosquitto MQTT broker (`./broker`)

## Running

#### Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/) for at least the MQTT broker.

### Docker

### Alternative Options

The web app and python MQTT clients may be run from the command line. See their readme files for more information.

**NOTE**: Remember to execute their commands from within their main project folders. E.g. `./mqtt_client` or `./web-app`
