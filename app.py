from data_extraction import CsvExtractor
from data_process_management import CsvProcessManager
from data_publication import PrintPublisher
from data_transformation import DataTransformer
from data_transformation.transformations.cycle_days_number import get_cycle_days_number
from etl_process_runner import EtlProcessRunner

# Add data transformations (and computed fields transformations) here.
DATA_TRANSFORMATIONS_TO_RUN = [
    get_cycle_days_number
]

if __name__ == '__main__':
    csv_extractor = CsvExtractor()
    data_transformer = DataTransformer(DATA_TRANSFORMATIONS_TO_RUN)
    csv_process_manager = CsvProcessManager()
    data_publisher = PrintPublisher()
    etl_process_runner = EtlProcessRunner(csv_extractor, data_transformer, csv_process_manager, data_publisher)
    etl_process_runner.run_etl_process()
