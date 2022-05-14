from multiprocessing.dummy import Pool

import requests

import configuration
from logger import logger


class DataExtractor:
    def __init__(self):
        self.pool = Pool()

    # Relevant data is data with the correct columns from the mapping, and only with these columns.
    def extract_relevant_data(self, data_name: str):
        df_chunks = self._get_data(data_name)
        return self.pool.imap(lambda df: self._apply_mapping(data_name, df), df_chunks)

    def _get_data(self, data_name: str):
        raise NotImplementedError

    def _apply_mapping(self, data_name, df):
        try:
            mapping = self._get_data_mapping(data_name)
            if mapping:
                df = df.rename(columns=mapping)
                df = df.filter(list(mapping.values()))
                return df
        except Exception as e:
            logger.error("Failed applying mapping on df chunk.", exc_info=e)

    def _get_data_mapping(self, data_name: str):
        data_name = data_name.lower()
        logger.info(f"Getting {data_name} mapping")
        try:
            response = requests.get(f"{configuration.MAPPING_API_URL}/mapping/{data_name}").json()
            logger.info(f"Got {data_name} mapping")
            return response
        except requests.RequestException as e:
            logger.error(f"Could not find mapping. Can't handle {data_name} data", exc_info=e)
            # I Didn't have time ot implement the api - so I leave these lines for the program to work, but they need to be deleted.
            return {'hospital_1_patient': {'PatientID': 'patient_id'},
                    'hospital_1_treatment': {'PatientID': 'patient_id', 'StartDate': 'start_date',
                                             'EndDate': 'end_date', 'CyclesXDays': 'number_of_cycles'},
                    'hospital_2_patient': {'PatientId': 'patient_id'},
                    'hospital_2_treatment': {'PatientId': 'patient_id', 'StartDate': 'start_date',
                                             'EndDate': 'end_date', 'NumberOfCycles': 'number_of_cycles'}}[data_name]
