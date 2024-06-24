import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/open_app', methods=['POST'])
def open_app():
    data = request.get_json()
    app_name = data.get('app')

    if app_name == 'calculator':
        subprocess.Popen('calc.exe')
    elif app_name == 'notepad':
        subprocess.Popen('notepad.exe')
    elif app_name == 'paint':
        subprocess.Popen('mspaint.exe')
    # Add more applications as needed

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)
