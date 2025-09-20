import os
import yaml
from box import ConfigBox
from pathlib import Path
from chicken_classifier.utils.common import create_directories
from chicken_classifier.entity.config_entity import DataIngestionConfig
from chicken_classifier.entity.config_entity import PrepareBaseModelConfig
from chicken_classifier.entity.config_entity import PrepareCallbackConfig
from chicken_classifier.constants import *


class ConfigurationManager:
    def __init__(self, 
                 config_filepath="config/config.yaml", 
                 params_filepath="params.yaml"):
        with open(config_filepath, "r") as f:
            self.config = ConfigBox(yaml.safe_load(f))

        # load params.yaml
        with open(params_filepath, "r") as f:
            self.params = ConfigBox(yaml.safe_load(f))

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

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
    
    def get_prepare_callback_config(self) -> PrepareCallbackConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbackConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config