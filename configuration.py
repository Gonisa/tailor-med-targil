import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '.'))
HOSPITALS_DATA_DIRECTORY = f"{ROOT_DIR}/hospitals_data"

UPDATE_TIME_PERIOD_IN_SEC = 3000

MAPPING_API_URL = ''
COMOUTED_FIELDS_API_URL = ''

CSV_CHUNK_SIZE = 2