import sqlite3

# データベース接続（なければ作成）
conn = sqlite3.connect("sakura_memory.db")
cursor = conn.cursor()

# 記憶データを保存するためのテーブルを作成
cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
conn.close()

print("Sakura Memory Database is ready!")
def save_memory(message):
    conn = sqlite3.connect("sakura_memory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memory (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()
    print(f"記憶を保存しました: {message}")

# テスト：メッセージを保存
save_memory("さくたん大好き💖")
