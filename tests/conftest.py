pytest_plugins = ['pytest_docker_fixtures']

from pytest_docker_fixtures import images

images.configure(
    'mysql',
    'mysql', '5.7',
    env={
        'MYSQL_USER': 'zbxdb',
        'MYSQL_PASSWORD': 'zbxdb',
        'MYSQL_DATABASE': 'zbxdb'
    },
    options={})
