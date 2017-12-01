import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models.WeatherSample import WeatherSampleModel


class WeatherSample(SQLAlchemyObjectType):
	class Meta:
		model = WeatherSampleModel

class WeatherSampleQuery(graphene.ObjectType):
	samples = graphene.List(WeatherSample)

	def resolve_samples(self, info):
		query = WeatherSample.get_query(info)
		return query.all()

schema = graphene.Schema(query=WeatherSampleQuery)