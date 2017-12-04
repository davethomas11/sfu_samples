#! usr/bin/python

from flask import Flask, redirect
from flask_graphql import GraphQLView
from database import db_session
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/samples', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={'session': db_session}))

@app.route('/')
def index():
	return redirect("/samples", code=302)

if __name__ == "__main__":
	app.run()