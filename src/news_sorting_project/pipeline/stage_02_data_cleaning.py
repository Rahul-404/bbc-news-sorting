from src.news_sorting_project.config.configuration import ConfigurationManager
from src.news_sorting_project.components.data_cleaning import DataCleaning
from src.news_sorting_project import logger

STAGE_NAME = "Data Cleaning Stage"

class DataCleaningPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_cleaning_config = config.get_data_cleaning_config()
        data_cleaning = DataCleaning(config=data_cleaning_config)
        data_cleaning.initiate_data_cleaning()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataCleaningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
