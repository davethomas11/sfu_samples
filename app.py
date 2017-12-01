#! usr/bin/python

from flask import Flask
from flask_graphql import GraphQLView
from database import db_session
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/weather', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={'session': db_session}))

@app.route('/')
def index():
	return "Go to /weather"

if __name__ == "__main__":
	app.run()