"""
Task 2: Add a Workout Session

Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.
    # Example code structure
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
Expected Outcome: A Python function that adds a new workout session to the 
'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors
gracefully, such as invalid member IDs or violations of other constraints.

"""
from connect import my_connect
def add_workout_session(member_id, date, duration_minutes, calories_burned):
        
    try:
        conn=my_connect()
        cursor=conn.cursor()
        data=(date,duration_minutes,calories_burned, member_id)
        query = 'SELECT id FROM members WHERE id=%s'
        cursor.execute(query,(member_id,))

        if cursor.fetchall():  
            query='''
            INSERT INTO workoutsessions(date,duration_minutes,calories_burned,member_id)
            VALUES (%s,%s,%s,%s)
            '''
            cursor.execute(query,data)
            conn.commit()
            print('New workout session added.')

        else:
            print("Unable to add workout session, invalid user ID.")
    
    except Exception as e:
        print(f'Error:{e}')
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()

add_workout_session(1, '2021-10-16', '30', '20')