import os
from multiprocessing.dummy import Pool

import configuration
from data_process_management import DataProcessManager


class CsvProcessManager(DataProcessManager):

    def run_data_process(self, data_name, data_extractor, data_transformer, data_publisher):
        super().run_data_process(data_name, data_extractor, data_transformer, data_publisher)
        #os.remove(f'{configuration.HOSPITALS_DATA_DIRECTORY}/{data_name}')
