import sqlite3
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Connect to (or create) the database
db_path = os.path.join("data", "emotions.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS emotion_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT,
    predicted_emotion TEXT,
    confidence REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print(f"✅ Database initialized successfully at: {db_path}")
