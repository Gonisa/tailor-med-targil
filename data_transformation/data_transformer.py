class DataTransformer:
    def __init__(self, transformations_to_run):
        self.transformations_to_run = transformations_to_run

    def transform_data(self, df):
        for process in self.transformations_to_run:
            process(df)
