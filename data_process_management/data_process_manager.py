from multiprocessing.dummy import Pool

from logger import logger


class DataProcessManager:
    def __init__(self):
        self.pool = Pool()

    def run_data_process(self, data_name, data_extractor, data_transformer, data_publisher):
        try:
            logger.info(f'Starting etl process for hospital data. data name: {data_name}')
            df_chunks = data_extractor.extract_relevant_data(data_name)
            self.pool.imap(lambda chunk: self._run_chunk_process(chunk, data_transformer, data_publisher), df_chunks)
            logger.info(f'Finished etl process for hospital data. data name: {data_name}')
        except Exception as e:
            logger.error("Failed running hospital data process.", exc_info=e)

    def _run_chunk_process(self, chunk, data_transformer, data_publisher):
        try:
            data_transformer.transform_data(chunk)
            data_publisher.publish_data(chunk)
        except Exception as e:
            logger.error("Failed running chunk process.", exc_info=e)
