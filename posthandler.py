from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def capture():
    if request.method == 'POST':
        print(f"Data Received: {request.data.decode()}")
        return 'Data Received', 200
    return 'Listener is Live', 200

if __name__ == '__main__':
    app.run(host='IP', port=PORT)
