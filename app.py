from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import psutil
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

def get_system_data():
    while True:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        processes = len(psutil.pids())
        load_avg = psutil.getloadavg()[0]  # 1-minute load average
        cpu_percent = psutil.cpu_percent(interval=1)  # CPU usage percentage
        
        data = {
            'memory': memory.percent,
            'swap': swap.percent,
            'processes': processes,
            'load_avg': load_avg,
            'cpu_percent': cpu_percent
        }
        
        socketio.emit('system_data', data)
        time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    thread = threading.Thread(target=get_system_data)
    thread.daemon = True
    thread.start()
    socketio.run(app, debug=True)

