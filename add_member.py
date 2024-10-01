from connect import my_connect
def add_member(name, age):
    try:
        conn=my_connect()
        cursor=conn.cursor()
        query='INSERT INTO members(name,age) VALUES(%s,%s)'
        data=(name,age)
        cursor.execute(query,data)
        conn.commit()
        print(f"New member {name} added")

    except Exception as e:
        print(f'Error:{e}')
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()

add_member("Josh Samuels", 20)
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints