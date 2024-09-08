import yaml
import logging

with open("src/logging_conf.yaml", "r") as f:
    logging_config = yaml.safe_load(f)
logging.config.dictConfig(logging_config)
log = logging.getLogger(__name__)


if __name__ == "__main__":
    pass