from src.news_sorting_project.utils.common import get_size
from src.news_sorting_project import logger
from src.news_sorting_project.entity.config_entity import DataIngetsionConfig
from dotenv import load_dotenv
from pathlib import Path
import zipfile
import boto3
import os

load_dotenv()

# Retrieve the credentials from environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION")
# Define the S3 bucket and object
bucket_name = os.getenv("AWS_BUCKET_NAME")
object_key = os.getenv("AWS_OBJECT_KEY")

class DataIngetsion:
    def __init__(self, config: DataIngetsionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Initialize a session using Boto3 with the credentials from the environment
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=aws_default_region
            )

            s3_client.download_file(bucket_name, object_key, self.config.local_data_file)

            logger.info(f"{object_key} download! with following info: \n{get_size(Path(self.config.local_data_file))}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """ 
        zip_file_path: str
        Extract the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)