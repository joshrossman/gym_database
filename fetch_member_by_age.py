from connect import my_connect

def get_members_in_age_range(start_age, end_age):
    conn = my_connect()
    cursor=conn.cursor()

    query='SELECT * FROM members WHERE age BETWEEN %s AND %s'
    cursor.execute(query,(start_age,end_age))
    for row in cursor.fetchall():
        print(row)

get_members_in_age_range(20,22)