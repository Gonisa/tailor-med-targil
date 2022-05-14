from logger import logger


class DataTransformer:
    def __init__(self, transformations_to_run):
        self.transformations_to_run = transformations_to_run

    def transform_data(self, df):
        logger.info('Running data transformers on data.')
        for process in self.transformations_to_run:
            try:
                process(df)
            except Exception as e:
                logger.error('Running data transformer has failed.', exc_info=e)
        logger.info('Finished running data transformers on data.')
