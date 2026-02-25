import sqlite3
import json
from datetime import datetime
from backend.utils import DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transcripts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                upload_time TEXT,
                script_data TEXT
            )
        ''')

def save_transcript(filename, script_data):
    with sqlite3.connect(DB_PATH) as conn:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        conn.execute(
            'INSERT INTO transcripts (filename, upload_time, script_data) VALUES (?, ?, ?)',
            (filename, timestamp, json.dumps(script_data))
        )

def get_history():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT id, filename, upload_time FROM transcripts ORDER BY id DESC')
        return cursor.fetchall()

def get_transcript_by_id(t_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT filename, script_data FROM transcripts WHERE id = ?', (t_id,))
        row = cursor.fetchone()
        return {"filename": row[0], "script": json.loads(row[1])} if row else None