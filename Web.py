from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import test
from pymongo import MongoClient
app = Flask(__name__, static_folder='frontend/dist', static_url_path='')
CORS(app)

client = MongoClient('mongodb+srv://rebeccafitzpatrick:hfJ|m#gv5W55@cluster0.pvplf8n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['700_web_tool_db']
leaderboard_collection = db['leaderboard']

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
    data = list(leaderboard_collection.find({}, {'_id': 0}))  # Exclude MongoDB's _id field
    return jsonify(data)

if __name__ == '__main__':
    app.run()
    