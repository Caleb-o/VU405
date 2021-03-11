from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<style>img { padding: 5px 10px; width: 100%; max-width: 200%; display: block; } </style><body><img src="https://johnnyalucard.com/wp-content/uploads/2020/04/shrek.jpg"><h1>Doing the big ol funny haha</h1></body><script>alert("666")</script>'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)