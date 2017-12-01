*November 30th 2017*

Today my goal was to import some of the data from one of 
the XLS files and play around with a basic setup for an API.

I decided to go with Python 3 and wanted to play around
and start to learn GraphQL.

I chose the file data/259C Weather - Summary 30SEPT16.xls
as my starting data.

---

Using pandas I read in the data from the file and imported
it into a MySQL database. You can find a dump of the 
database in the SQL folder.

I did this from the python terminal via:
```
>> import pandas
>> xls = pandas.read_excel("259C Weather - Summary 30SEPT16.xls")
```

I then used the SQLAlchmehy model you can find in the
models directory to import into the database.

I executed the SQLAlchemy model in terminal via:
```
>> exec(open(models/WeatherSample.py).read())
```

I then opened up a database connection:
```
>> from sqlalchemy import create_engine
>> engine = create_engine("mysql://...connection string goes here...")
>> from sqlalchemy.orm import sessionmaker
>> session = sessionmaker(bind=engine)()
```


Finally I dumped the data in MySQL:
```
>> for x in (8, len(xls.values)):
>> ...   sample = WeatherSample(date=xls.values[x][0], temp=xls.values[x][1], wind_speed=xls.values[x][2], wind_direction=xls.values[x][3], rain=xls.values[x][4])
>> ...   session.add(sample)
>>
>> session.commit() // Finalizes transaction in MySQL database
```

---

I then went off to research GraphQL and flask. I came across
a nice sample project at https://github.com/Getmrahul/Flask-Graphene-SQLAlchemy.
I used this and the https://github.com/graphql-python/graphene-sqlalchemy to
build my first very basic sample app.

It was amazing to see how much was provided by these frameworks
when I brought up my first queries!
