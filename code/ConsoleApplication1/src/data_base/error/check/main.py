
def check_db(root, name_db):
    import sqlite3

    conn = sqlite3.connect(name_db) 
    cursor = conn.cursor()

    cursor.execute("""

        SELECT 
            EXISTS (SELECT 1 FROM check_db LIMIT 1) 
            OR 
            EXISTS (SELECT 1 FROM check_assistant_teacher LIMIT 1)
    """)
    
    if cursor.fetchone()[0]:
        return True

    return False
