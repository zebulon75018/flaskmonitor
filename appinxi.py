from flask import Flask, render_template, jsonify, request
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexinxi2.html')

@app.route('/execute_command', methods=['GET'])
def execute_command():
    command = "/home/easy/STUFF/inxi/inxi -F --output json --output-file /tmp/inxi.json"
    
    try:
        result = subprocess.run(command, shell=True, )
        with open('/tmp/inxi.json') as json_data:
            d = json.load(json_data)
        return jsonify({'success': True, 'output': d})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True,port = 5003)
