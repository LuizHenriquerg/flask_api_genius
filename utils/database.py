import boto3
import os


class Dynamo:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('ACCESS_SECRET_KEY'),
            region_name='us-west-2'
        )

    def database(self):
        try:
            tabela = self.dynamodb.create_table(
                TableName='artistas',
                KeySchema=[
                    {
                        'AttributeName': 'nome',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'nome',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )

            tabela = self.dynamodb.Table('artistas')
        except:
            tabela = self.dynamodb.Table('artistas')

        return tabela
        