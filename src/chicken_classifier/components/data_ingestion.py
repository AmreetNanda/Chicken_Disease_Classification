import os
import shutil
import zipfile
from pathlib import Path
import logging
from chicken_classifier.entity.config_entity import DataIngestionConfig


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_size(path: Path) -> str:
    size_in_kb = os.path.getsize(path) / 1024
    if size_in_kb < 1024:
        return f"{size_in_kb:.2f} KB"
    return f"{size_in_kb/1024:.2f} MB"


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Copies dataset zip file from local path into artifacts directory.
        """
        local_file = Path(self.config.local_data_file)

        if not local_file.exists():
            shutil.copy(self.config.source_URL, local_file)
            logger.info(f"Copied local file from {self.config.source_URL} → {local_file}")
        else:
            logger.info(f"File already exists: {local_file} ({get_size(local_file)})")

    def extract_zip_file(self):
        """
        Extracts the dataset zip file into the specified directory.
        """
        unzip_path = Path(self.config.unzip_dir)
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Extracted {self.config.local_data_file} → {unzip_path}")
