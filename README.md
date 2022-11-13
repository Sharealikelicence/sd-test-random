# sD Test - Random Number Generator Client

MQTT client that publishes random numbers.

## Installation

### Configuration

Create a configuration file, based off of the `config.sample.json` file. By default, the client will look for a file named `config.json`. See the Docker and CLI sections bellow for more information.
<!-- TODO: Add section regarding config options -->

### Docker (Preferred)

#### Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/)

#### Build and Run

```shell
DOCKER_BUILDKIT=1 docker build -t sd-client-random . && \
  docker run \
    -i \
    -rm \
    --net=host \
    --name=sd-client-random \
    -e CONFIG_PATH=path/to/config/file \
    sd-client-random
```

Where `-e CONFIG_PATH=path/to/config/file` is an optional argument for setting a configuration file other than `config.json` as referenced from within the container. If this file isn't within the project directory, make sure to add the `-v` option to the run command for mounting the host volume within the container and reference `CONFIG_PATH` accordingly. (Further details are out of scope for this test but just showing that it is possible to have more flexible deployment options if needed).

### CLI

#### Prerequisites

* [Python](https://www.python.org/downloads/) 3.11 or above

#### Initial Setup

Create and initialise a virtual environment (Optional):
```shell
python -m venv .venv
source .venv/bin/activate
```
Install required modules:
```shell
pip install -r requirements.txt
```

#### Run

```shell
python ./main.py
```

Optionally, it is possible to use a configuration file other than the default (`config.json`) by providing the `-c` (or `--config`) argument as follows:

```shell
python ./main.py -c path/to/config/file
```
