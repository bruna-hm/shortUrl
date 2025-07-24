import sqlite3

def create_tab():
    with sqlite3.connect("urls.db") as conn:
        cur = conn.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS urls 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                longa VARCHAR(100) NOT NULL,
                curta VARCHAR(100) NOT NULL UNIQUE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
                """)
    
    conn.commit()
    conn.close()
    
def cad_url(url_longa, codigo):
    with sqlite3.connect("urls.db") as conn:
        cur = conn.cursor()
        
    cur.execute("INSERT INTO urls (longa, curta) VALUES (?, ?)", (url_longa, codigo))
    
    conn.commit()
    conn.close()