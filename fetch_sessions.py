from connect import my_connect

def fetch_sessions():
    try:
        conn=my_connect()
        cursor=conn.cursor()
        query='SELECT * FROM workoutsessions'
        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print("Error:{e}")

    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()