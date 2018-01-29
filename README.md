pymysql-wrapper

Installation:
- Download digin_database
- unzip digin_database.zip, enter the unpacked directory and run the following commands:
   shell> python setup.py build
   shell> python setup.py install

Example:
    from digin_database import DbDriver, printTable
    conn_param = {"host": "localhost",
                  "user": "user",
                  "password": "pass",
                  "dbname": "tests"}
    query = DbDriver(conn_param)
    result, desc, rows = query.execute(sql.get_queue)
    printTable(result)