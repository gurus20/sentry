import sqlite3

def connect_to_db():    
    conn = sqlite3.connect('usage.db')
    print("Opened database successfully")

    table_name = "USAGE"

    conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
            (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
            PID INTEGER NOT NULL,
            NAME           TEXT    NOT NULL,
            SNAP_TIME       TEXT     NOT NULL,
            MEMORY       TEXT     NOT NULL,
            COMMAND       TEXT     NOT NULL,
            CPU       TEXT     NOT NULL,
            USERNAME       TEXT     NOT NULL
            );''')
    return conn


def save_snapshot_to_db(conn, usage):
    for obj in usage:
        values = obj.to_tuple() 
        conn.execute(f"""UPDATE USAGE SET (PID, NAME, SNAP_TIME, MEMORY, COMMAND, CPU, USERNAME) = {values} WHERE PID = {values[0]};""")
        conn.commit()
        # try:
        # except:    
        #     with open("usage.txt", 'a') as f:
        #         f.write(f'{str(values)}\n')

    print("Saved entries")
    conn.close()
    print("connection closed")