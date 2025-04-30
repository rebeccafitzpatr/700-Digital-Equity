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

if __name__ == '__main__':
    app.run()
    