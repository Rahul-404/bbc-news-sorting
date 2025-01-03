from src.news_sorting_project.constants import *
from src.news_sorting_project.utils.common import read_yaml, create_directories
from src.news_sorting_project.entity.config_entity import (DataIngetsionConfig, DataCleaningConfig)
import os
from pathlib import Path

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngetsionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngetsionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_cleaning_config(self) -> DataCleaningConfig:
        config = self.config.data_cleaning

        create_directories([config.root_dir])

        data_clearning_config = DataCleaningConfig(
            root_dir=config.root_dir,
            raw_data_file=config.raw_data_file,
            clean_data_file = config.clean_data_file,
            preprocessing_obj = config.preprocessing_obj
        )

        return data_clearning_config

    # def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:

    #     config = self.config.prepare_base_model

    #     create_directories([config.root_dir])

    #     prepare_base_model_config = PrepareBaseModelConfig(
    #         root_dir= Path(config.root_dir),
    #         base_model_path=Path(config.base_model_path),
    #         updated_base_model_path=Path(config.updated_base_model_path),
    #         params_image_size=self.params.IMAGE_SIZE,
    #         params_learning_rate=self.params.LEARNING_RATE,
    #         params_include_top=self.params.INCLUDE_TOP,
    #         params_weights=self.params.WEIGHTS,
    #         params_classes=self.params.CLASSES
    #     )

    #     return prepare_base_model_config
    
    # def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
    #     config = self.config.prepare_callbacks

    #     model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)

    #     create_directories([
    #         Path(model_ckpt_dir),
    #         Path(config.tensorboard_root_log_dir)
    #     ])

    #     prepare_callback_config = PrepareCallbacksConfig(
    #         root_dir=Path(config.root_dir),
    #         tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
    #         checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
    #     )

    #     return prepare_callback_config
    
    # def get_training_config(self) -> TrainingConfig:
    #     training = self.config.training
    #     prepare_base_model = self.config.prepare_base_model
    #     params = self.params
    #     training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")
    #     create_directories([
    #         Path(training.root_dir)
    #     ])

    #     training_config = TrainingConfig(
    #         root_dir=Path(training.root_dir),
    #         trained_model_path=Path(training.trained_model_path),
    #         updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
    #         training_data=Path(training_data),
    #         params_epochs=params.EPOCHS,
    #         params_batch_size=params.BATCH_SIZE,
    #         params_is_augmentation=params.AUGMENTATION,
    #         params_image_size=params.IMAGE_SIZE,
    #         params_learning_rate=params.LEARNING_RATE
    #     )

    #     return training_config

    # def get_validation_config(self)-> EvaluationConfig:
    #     eval_config = EvaluationConfig(
    #         path_of_model=Path("artifacts/training/model.h5"),
    #         training_data=Path("artifacts/data_ingestion/Chicken-fecal-images"),
    #         all_params=self.params,
    #         params_image_size=self.params.IMAGE_SIZE,
    #         params_batch_size=self.params.BATCH_SIZE
    #     )

    #     return eval_config