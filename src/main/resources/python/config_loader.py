import configparser
import os

def load_config(env="dev", base_path="src/main/resources/etc"):
    """
    Load configuration properties from an INI file.

    Reads a configuration file (e.g., dev.ini or prod.ini) from the specified
    base path and returns key-value pairs as a dictionary using ConfigParser.

    Parameters:
    - env (str): The environment name (e.g., "dev" or "prod") to determine the file.
    - base_path (str): Path to the folder containing environment INI files.

    Returns:
    - dict: Configuration parameters from the loaded INI file.
    """
    config = configparser.ConfigParser()
    config.read(os.path.join(base_path, f"{env}.ini"))
    return config["COMMON"]