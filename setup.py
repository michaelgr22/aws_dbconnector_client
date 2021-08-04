from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'client to connect to different db instances in aws via secret'
LONG_DESCRIPTION = 'client to connect to different db instances in aws via secret'

# Setting up
setup(
    name="aws_dbconnector_client",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['aws_dbconnector_client'],
    install_requires=['aws_secretsmanager_client', 'aws_postgresdb_client'],
)
