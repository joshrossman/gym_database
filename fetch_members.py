from connect import my_connect

try:
    conn=my_connect()
    cursor=conn.cursor()

    query='SELECT * FROM members'
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print(f'Error:{e}')
    
finally:
    if conn and conn.is_connected():
        conn.close()
        cursor.close()