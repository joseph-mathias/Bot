import dbconfig
import postgres.connector
import psycopg2


conn = postgres.connector.connect(**dbconfig)
db = conn.db()
_SQL = """show tables"""
db.execute(_SQL)

res = db.fetchall()
res

for row in res:
    print(row)


# _SQL = """
#         insert into log
#         (phrase, letters, ip, browser_string, results)
#         values
#         ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")
#        """
_SQL = """
        insert into log
        (phrase, letters, ip, browser_string, results)
        values 
        (%s, %s, %s, %s, %s)
       """
db.execute(_SQL, ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}"))

conn.commit()
_SQL = """select * from log"""
db.execute(_SQL)
for row in db.fetchall:
    print(row)

db.close()
True
conn.close()
