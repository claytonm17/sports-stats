import sqlite3

con = sqlite3.connect("stats.db")

cur = con.cursor()

# Create table for pitcher stats
cur.execute('''
        CREATE TABLE IF NOT EXISTS colleges
            (name, championships, heismans)
''')

cur.execute('''
    INSERT INTO colleges VALUES
        ("Ohio State", 8, 7),
        ("Texas", 4, 2)
''')

res = cur.execute("SELECT * FROM colleges")
print(res.fetchall())

con.commit()

con.close()