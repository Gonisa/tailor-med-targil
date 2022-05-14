from data_publication import DataPublisher
import sqlite3
import configuration


class SqLitePublisher(DataPublisher):
    def __init__(self):
        self.con = sqlite3.connect(f'{configuration.ROOT_DIR}/hospitals.db')
        self.cur = self.con.cursor()

    def publish_data(self, chunk):
        rows = list(chunk.to_dict('records'))
        for row in rows:
            columns = ', '.join(row.keys())
            placeholders = ', '.join('?' * len(row))
            sql = 'INSERT INTO patient_treatment ({}) VALUES ({})'.format(columns, placeholders)
            row = [int(x) if isinstance(x, bool) else x for x in row.values()]
            cur.execute(sql, row)
        self.con.commit()


if __name__ == '__main__':
    con = sqlite3.connect(f'{configuration.ROOT_DIR}/hospitals.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE patient_treatment (patient_id, start_date, end_date, number_of_cycles)''')
    con.commit()
