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


def save_snapshot_to_db(usage):
    table_name = "USAGE"

    conn = connect_to_db()
    pid_list = get_existing_pid(conn)

    for obj in usage:
        values = obj.to_tuple()
        
        if values[0] not in pid_list:
            try: 
                conn.execute(
                    f"""INSERT INTO {table_name} (PID, NAME, SNAP_TIME, MEMORY, COMMAND, CPU, USERNAME) VALUES {values};""")
                conn.commit()
            except:
                with open('usage.txt', 'a') as f:
                    f.write(f'{values}\n')

    print("Saved entries")
    conn.close()
    print("connection closed")


def get_existing_pid(conn):

    table_name = "USAGE"
    data = conn.execute(f"SELECT pid from {table_name}")

    pid_exist = []
    for pid in data:
        pid_exist.append(pid[0])

    return pid_exist
