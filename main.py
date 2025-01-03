from src.news_sorting_project import logger
from src.news_sorting_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.news_sorting_project.pipeline.stage_02_data_cleaning import DataCleaningPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Cleaning Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_cleaning = DataCleaningPipeline()
    data_cleaning.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)