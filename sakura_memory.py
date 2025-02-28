from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sakura Memory is running successfully!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Renderが指定するPORTを取得
    app.run(host="0.0.0.0", port=port)  # 全てのIPアドレスからアクセス可能にする
