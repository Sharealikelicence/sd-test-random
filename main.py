import argparse
from datetime import datetime, timedelta
import json
import os

from apscheduler.schedulers.background import BackgroundScheduler
from client.random_number import RandomNumberClient

from util import BoundedRandom


DEFAULT_CONFIG_PATH = 'config.json'


# Just use a memory job store as there is no requirement to make publishing specific numbers persistent.
scheduler = BackgroundScheduler()


def on_publish(client, userdata, mid):
    print(f"Published mesasge with id {mid}")


def get_job_datetime():
    now = datetime.now()
    # Get a new random datetime between 1 and 30 seconds from now.
    return BoundedRandom.datetime(now + timedelta(seconds=1), now + timedelta(seconds=30))


def publish(client: RandomNumberClient):
    print('Publishing and rescheduling...')
    client.publish()
    scheduler.add_job(publish, 'date', run_date=get_job_datetime(),kwargs={'client': client})


def start(**kwargs):
    client = RandomNumberClient(**kwargs, on_publish=on_publish)

    # Schedule initial job and start scheduler
    scheduler.add_job(publish, 'date', run_date=get_job_datetime(),kwargs={'client': client})
    scheduler.start()

    # Using blocking loop since it is a simple implementation.
    client.loop_forever()


if __name__ == "__main__":
    # Read in configuration data. This offers both a CLI and Docker friendly method for more robust deployment options.
    # Note: Could of made this take in command line arguments as well (instead of just via a config file) but did not want to over-engineer for this test.

    # Load config path from command line args for non-docker deployments. Load from environment variable otherwise.
    env_config_path = os.environ.get('CONFIG_PATH')

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help="Path to the client's configuration file.")
    args = parser.parse_args()

    config_file_path = args.config if args.config else env_config_path if env_config_path else DEFAULT_CONFIG_PATH

    config = {}
    with open(config_file_path) as json_file:
        config = json.load(json_file)

    start(**config)
