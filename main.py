import argparse
import configparser
import json
import os
import paho.mqtt.client as mqtt

DEFAULT_CONFIG_PATH = 'config.json'

def start(**kwargs):
    client = mqtt.Client(**kwargs)

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
