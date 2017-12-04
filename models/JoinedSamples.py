from sqlalchemy import join, Integer, Float, DateTime, Column, Table, MetaData, ForeignKey
from models.DBModelBase import Base
from sqlalchemy.orm import column_property

metadata = MetaData()

water_table = Table('water_sample', metadata,
	Column('id', Integer, primary_key=True),
	Column('date', DateTime),
	Column('flow', Float),
	Column('level', Float),
	Column('conductivity', Float),
	Column('rain', Float),
	Column('temp', Float),
)	

weather_table = Table('weather_sample', metadata,
	Column('id', Integer, primary_key=True),
    Column('date', DateTime, ForeignKey('water_sample.date')),
	Column('temp', Float),
	Column('wind_speed', Integer),
	Column('wind_direction', Integer),
	Column('rain', Float),
)

class Sample(Base):
	__table__ = join(water_table, weather_table, water_table.c.date == weather_table.c.date).alias()