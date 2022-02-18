import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=35.223.250.26;'
                      'Database=kanji;'
                      'UID=sqlserver;'
                      'PWD=sqlserver_kanji;')

def db_exe(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    #conn.close()

def db_select(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    content = []
    for data in cursor:
        content.append(data)
    conn.close()
    return content