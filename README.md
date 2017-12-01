**SFU Samples Playground Prototyping**

--

To run this application locally you need to install
MySQL and dump the database file in the sql directory
into a new database.

This is the database you will want to connect to with 
your connection stirng.

Then in config.py setup your mysql conneciton string.
As such:
```
connection_string='mysql://username:password@domain/database'
```

First create a virtual environment then install with
```
python setup.py install
```

Run app with
``` 
python app.py
```

When it is running goto http://127.0.0.1:5000/weather to make some queries!
