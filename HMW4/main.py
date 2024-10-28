from flask import Flask, render_template, request, redirect, url_for
import socket
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        

        if not username or not message:
            return redirect(url_for('error_page'))

        data = {
            'username': username,
            'message': message
        }
        send_to_socket(data)


        save_to_json(data)
        
        return redirect(url_for('index'))
    return render_template('message.html')

@app.route('/error')
def error_page():
    return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

def send_to_socket(data):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(data).encode(), ('127.0.0.1', 5000))

def save_to_json(data):
    json_file_path = os.path.join('templates', 'storage', 'data_memory.json')
    

    timestamp = datetime.now().isoformat()


    entry = {timestamp: data}


    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = {}


    existing_data.update(entry)


    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)
