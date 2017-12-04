import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models.WeatherSample import WeatherSampleModel
from models.WaterSample import WaterSampleModel
from models.JoinedSamples import Sample


class WeatherSample(SQLAlchemyObjectType):
	class Meta:
		model = WeatherSampleModel

class WaterSample(SQLAlchemyObjectType):
	class Meta:
		model = WaterSampleModel

class Sample(SQLAlchemyObjectType):
	class Meta:
		model = Sample

class Query(graphene.ObjectType):
	water = graphene.List(WaterSample)
	weather = graphene.List(WeatherSample)
	sample = graphene.List(Sample)

	def resolve_water(self, info):
		query = WaterSample.get_query(info)
		return query.all()

	def resolve_weather(self, info):
		query = WeatherSample.get_query(info)
		return query.all()

	def resolve_sample(self, info):
		query = Sample.get_query(info)
		return query.all()

schema = graphene.Schema(query=Query)