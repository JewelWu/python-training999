from flask import Flask
import crawler.training_material as tm

app = Flask(__name__)      # __name__ 表示目前模組

@app.route('/')
def home():
    return "This home page."

@app.route("/crawler")
def crawler():
    return tm.crawPages()
    
if __name__ == "__main__":      # 若以主程式來執行
    app.run()                  # 啟動 Server
