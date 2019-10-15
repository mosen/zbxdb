import pytest
import psycopg2

from dbconnections.cockroach import connection_info


class TestCockroach:
    def test_connection_info(self, cockroach):
        host, port = cockroach
        conn = psycopg2.connect(host=host, port=port, username='root', password='')
        info = connection_info(conn)
        print(info)

