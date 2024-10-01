from connect import my_connect


def delete_session(session_id):
    try:
        conn=my_connect()
        cursor=conn.cursor()

        query='SELECT id FROM workoutsessions WHERE id=%s'
        cursor.execute(query,(session_id,))
        if cursor.fetchall():
            query='DELETE FROM workoutsessions WHERE id=%s'
            cursor.execute(query,(session_id,))
            conn.commit()
            print('Session succesfully deleted')
            
        else:
            print('Error: Could not delete workoutsession. Invalid ID entered, session does not exsist.')
        
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()


delete_session(1)