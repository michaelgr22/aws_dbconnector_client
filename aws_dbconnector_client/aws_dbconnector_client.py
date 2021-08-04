import ast

from . import errors
from aws_secretsmanager_client import AwsSecretsManagerClient
from aws_postgresdb_client import AwsPostgresDBClient


class AwsDBConnectorClient:
    def __init__(self, secret_name, secret_region, database, enviroment):
        self.secret_name = secret_name
        self.secret_region = secret_region
        self.database = database
        self.enviroment = enviroment

    def get_db(self):
        aws_secret_client = AwsSecretsManagerClient(
            self.secret_name, self.secret_region)
        secret = ast.literal_eval(aws_secret_client.get_secret())
        db = self.__choose_db(secret, self.enviroment)
        if db:
            return db
        else:
            raise errors.DBConnectionError('Cant connect to db {} in env {} with secret {}'.format(
                self.database, self.enviroment, self.enviroment))

    def __choose_db(self, secret, enviroment):
        return {
            'postgres': self.__postgres_client(secret)
        }.get(enviroment, None)

    def __postgres_client(self, secret):
        return AwsPostgresDBClient(host=secret['host'],
                                   port=secret['port'],
                                   database=self.database,
                                   user=secret['username'],
                                   password=secret['password'])
