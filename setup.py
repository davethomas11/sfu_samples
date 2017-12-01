from setuptools import setup, find_packages

setup(
	name='SFU-Samples',
	packages=find_packages(),
	install_requires=[
		'SQLAlchemy == 1.1',
		'mysqlclient == 1.3.12',
		'pandas == 0.21.0',
		'xlrd >= 0.9.0',
		'Flask == 0.12.2',
		'Flask-GraphQL == 1.4.1',
		'graphene == 2.0',
		'graphene-sqlalchemy == 2.0'
	]
)
