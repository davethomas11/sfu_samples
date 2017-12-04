*December 3rd, 2017*

Today I am going to be importing water sample data from
259C Site MA1 - Summary 30SEPT16.xls and cross referencing
it with data I imported from as ```WeatherSampleModels```

Import process (python command line):

Load excel data in var `xl`

```
>>> import pandas
>>> xl = pandas.read_excel("data/259C Site MA1 - Summary 30SEPT16.xls")
```

Load database ORM model

```
>>> exec(open("models/WaterSample.py").read())
```

Confirm model is loaded

```
>>> WaterSampleModel
<class '__main__.WaterSampleModel'>
```

Create database connection

```
>>> from sqlalchemy import create_engine
>>> engine = create_engine('mysql://*user*:*pwd*@localhost/OpaData')
>>> from sqlalchemy.orm import sessionmaker
>>> session = sessionmaker(bind=engine)()
```

Create model tabel

```
>>> Base.metadata.create_all(engine)
```

Insert records into database

```
>>> for x in range(8, len(xl.values)):
...      ws = xl.values[x]
...      record = WaterSampleModel(date=ws[0], flow=ws[1], level=ws[2], conductivity=ws[3], rain=ws[4], temp=ws[5])
...      session.add(record)
...
>>> session.commit()
```

---

With the data now in the database I am going to implement the
simple basic access to it using GraphQL as I did with the
weather samples.

I've created a simple schema for the model and made it queriable.
My next step now is to research making a joined model between
the two tables.

---

I've figured out how to create an unconventional SQLAlchemy model
across two tables using this reference: http://docs.sqlalchemy.org/en/latest/orm/nonstandard_mappings.html

Important to note, that once I did that query I realized really quickly
that I needed indexes created on the date fields. The query was even two slow to
return with 80,000ish records which is only one month of data.

With indexes the query became instant.

---

For my next journey I am going to upload to some custom hobby hosting what 
I currently have created.
