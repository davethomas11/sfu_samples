from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey
from models.DBModelBase import Base

class WaterSampleModel(Base):
	__tablename__ = 'water_sample'

	id = Column(Integer, primary_key=True)
	date = Column(DateTime)
	flow = Column(Float)
	level = Column(Float)
	conductivity = Column(Float)
	rain = Column(Float)
	temp = Column(Float)