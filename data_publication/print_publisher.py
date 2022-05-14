from data_publication import DataPublisher


class PrintPublisher(DataPublisher):

    def publish_data(self, chunk):
        print(chunk)
