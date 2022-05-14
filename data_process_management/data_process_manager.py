from multiprocessing.dummy import Pool


class DataProcessManager:
    def __init__(self):
        self.pool = Pool()

    def run_data_process(self, data_name, data_extractor, data_transformer, data_publisher):
        df_chunks = data_extractor.extract_relevant_data(data_name)
        self.pool.imap(lambda chunk: self._run_chunk_process(chunk, data_transformer, data_publisher), df_chunks)

    def _run_chunk_process(self, chunk, data_transformer, data_publisher):
        data_transformer.transform_data(chunk)
        data_publisher.publish_data(chunk)
