from flask import Flask
app = Flask(__name__)      # __name__ 表示目前模組

@app.route('/')
def home():
    return "This home page."

@app.route("/crawler")
def crawler():
    return "This is crawler page."

if __name__ == "__main__":      # 若以主程式來執行
    app.run()                  # 啟動 Server
