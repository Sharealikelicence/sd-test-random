# sD Test - Random Number Generator Client

MQTT client that publishes random numbers.

## Installation

### Docker (Preferred)

#### Prerequisites

* [Docker Engine](https://docs.docker.com/engine/install) or [Docker Desktop](https://docs.docker.com/desktop/)

#### Build

```shell
docker build -t sd-client-random .
```

#### Run

```shell
docker run --name=sd-client-random sd-client-random
```

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
