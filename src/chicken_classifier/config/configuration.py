import os
import yaml
from box import ConfigBox
from chicken_classifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath, "r") as f:
            self.config = ConfigBox(yaml.safe_load(f))

        os.makedirs(self.config.artifacts_root, exist_ok=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        cfg = self.config.data_ingestion
        os.makedirs(cfg.root_dir, exist_ok=True)

        return DataIngestionConfig(
            root_dir=cfg.root_dir,
            source_URL=cfg.source_URL,
            local_data_file=cfg.local_data_file,
            unzip_dir=cfg.unzip_dir
        )
