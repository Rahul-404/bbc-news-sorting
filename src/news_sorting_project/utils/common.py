import os
from box.exceptions import BoxValueError
import yaml
from src.news_sorting_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import pandas as pd
from typing import Any
import pickle

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ 
    read yaml file and returns

    Args:
        path_to_yaml (str):

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file) 
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """ 
    create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Default is False. 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path_to_directories}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """ 
    save json data
    Arges:
        path (Path): path to the json file
        data (dict): data to be save in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ 
    load json file data

    Args:
        path (Path): path to the json file

    Returns:
        ConfigBox: data as class attributed instead of dict
    """
    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ 
    save binary file

    Args:
        data (Any): data to be save as binary
        path (Path): path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ 
    load bianry data

    Args:
        path (Path): path to binary file

    Returns: 
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path))
    return f"~ {size_in_kb} KB"

@ensure_annotations
def save_object(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
             
    except Exception as e:
        raise e
    
@ensure_annotations
def save_csv(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        obj.to_csv(file_path, index=False)
             
    except Exception as e:
        raise e