import pytest
import pymysql

from dbconnections import mysql as zbxmysql


@pytest.fixture
def mysql_connection(mysql):
    host, port = mysql


    connection = pymysql.connect(
        host=host,
        port=int(port),
        user='root',
        password='',
        db='zbxdb',
    )
    yield connection
    connection.close()


class TestMySQL:
    def test_connect(self, mysql):
        host, port = mysql
        config = {
            'server': host,
            'username': 'zbxdb',
            'password': 'zbxdb',
            'db_name': 'zbxdb',
            'server_port': port,
            'sqltimeout': 100,
            'ME': 'zbxdb_test',
        }

        conn = zbxmysql.connect(pymysql, config)
        assert conn is not None
        assert conn.open is True
        conn.ping()

    def test_current_role(self, mysql_connection):
        role = zbxmysql.current_role(mysql_connection, None)
        assert role is not None
        assert role == 'primary'

    def test_connection_info(self, mysql_connection):
        info = zbxmysql.connection_info(mysql_connection)
        assert info is not None

