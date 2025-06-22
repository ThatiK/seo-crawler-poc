import configparser
import os

def load_config(env="dev", base_path="src/main/resources/etc"):
    config = configparser.ConfigParser()
    config.read(os.path.join(base_path, f"{env}.ini"))
    return config["COMMON"]