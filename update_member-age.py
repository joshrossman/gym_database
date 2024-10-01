from connect import my_connect

def update_member_age(member_id,new_age):
    
    try:
        conn=my_connect()
        cursor=conn.cursor()
        
        query='SELECT id FROM members WHERE id = %s'
        cursor.execute(query,(member_id,))
        if cursor.fetchall():
            data=(new_age,member_id)
            query='UPDATE members SET age=%s WHERE id=%s'
            cursor.execute(query,data)
            conn.commit()
            print(f"Member's age succesfully changed.")
        else:
            print('Error. Could not change member age. Invalid member ID entered. Please check your data and try again.')

    except Exception as e:
        print(f"Error:{e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()

update_member_age(7,7)