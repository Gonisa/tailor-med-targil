from pathlib import Path

import pandas as pd

import configuration
from data_extraction import DataExtractor


class CsvExtractor(DataExtractor):

    def _get_data(self, data_name):
        return pd.read_csv(f"{configuration.HOSPITALS_DATA_DIRECTORY}/{data_name}",
                           chunksize=configuration.CSV_CHUNK_SIZE)

    def _get_data_mapping(self, data_name: str):
        file_name_without_extension = Path(data_name).stem.lower()
        return super()._get_data_mapping(file_name_without_extension)
