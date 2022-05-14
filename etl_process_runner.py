import os
import time
from multiprocessing.dummy import Pool

import configuration
from data_extraction import DataExtractor
from data_process_management import DataProcessManager
from data_publication import DataPublisher
from data_transformation import DataTransformer
from logger import logger


class EtlProcessRunner:
    def __init__(self, data_extractor: DataExtractor, data_transformer: DataTransformer,
                 data_process_manager: DataProcessManager, data_publisher: DataPublisher):
        self.data_extractor = data_extractor
        self.data_transformer = data_transformer
        self.data_process_manager = data_process_manager
        self.data_publisher = data_publisher

    def run_etl_process(self):
        logger.info('Starting etl process for all hospitals data.')
        try:
            while True:
                hospitals_data = os.listdir(configuration.HOSPITALS_DATA_DIRECTORY)
                thread_pool = Pool(len(hospitals_data))
                thread_pool.imap(
                    lambda hospital_data: self.data_process_manager.run_data_process(hospital_data, self.data_extractor,
                                                                                     self.data_transformer,
                                                                                     self.data_publisher),
                    hospitals_data)
                time.sleep(configuration.UPDATE_TIME_PERIOD_IN_SEC)
        except Exception as e:
            logger.error('Running etl process has failed', exc_info=e)
