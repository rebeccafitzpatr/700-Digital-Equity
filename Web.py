from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import test
app = Flask(__name__, static_folder='frontend/dist', static_url_path='')
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/web', methods=['GET'])
def speedtest():
    (download, upload, packet_loss, avg_ping) = test.speedTest()
    return jsonify({
        'download': download,
        'upload': upload,
        'packet_loss': packet_loss,
        'avg_ping': avg_ping
    })

@app.route('/api/leaderboard', methods=['GET'])
def leaderboard():
    # Replace this with actual database query
    data = [
        {
            'name': 'School 1',
            'region': 'Auckland',
            'latency': 30,
            'upload': 80,
            'download': 200,
            'device': 'Laptop'
        },
        {
            'name': 'School 2',
            'region': 'Auckland',
            'latency': 20,
            'upload': 50,
            'download': 100,
            'device': 'Windows 10'
        },
        {
            'name': 'School 3',
            'region': 'Northland',
            'latency': 40,
            'upload': 100,
            'download': 120,
            'device': 'Laptop'
        }
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run()
    speedtest()
    