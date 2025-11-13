# src/utils/config.py
import yaml

def load_config(config_path="params.yaml"):
    """
    Load the YAML configuration file.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def get_model_params(config):
    """
    Get model parameters from the config dictionary.
    """
    return config.get("model", {})

def get_data_params(config):
    """
    Get data-related parameters from the config dictionary.
    """
    return config.get("data", {})

def get_logging_params(config):
    """
    Get logging-related parameters from the config dictionary.
    """
    return config.get("logging", {})

