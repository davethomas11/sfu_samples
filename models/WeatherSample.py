from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, Float

Base = declarative_base()

class WeatherSampleModel(Base):
	__tablename__ = 'weather_sample'

	id = Column(Integer, primary_key=True)
	date = Column(DateTime)
	temp = Column(Float)
	wind_speed = Column(Integer)
	wind_direction = Column(Integer)
	rain = Column(Float)
