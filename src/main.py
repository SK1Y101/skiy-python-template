import logging.config
import os

import yaml

with open("src/logging_conf.yaml", "r") as f:
    logging_config = yaml.safe_load(f)
logging.config.dictConfig(logging_config)
base_log = logging.getLogger(os.getcwd().rsplit("/",1)[1].lower())


if __name__ == "__main__":
    base_log.info("Hello world!")
