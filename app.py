from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

BASE_DIR = r'B:\ftp'

@app.route('/')
@app.route('/browse/<path:subpath>')
def index(subpath=""):
    folder_path = os.path.join(BASE_DIR, subpath)

    if not os.path.exists(folder_path):
        return "Thư mục không tồn tại", 404

    items = os.listdir(folder_path)
    folders = [f for f in items if os.path.isdir(os.path.join(folder_path, f))]
    files = [f for f in items if os.path.isfile(os.path.join(folder_path, f))]

    return render_template('index.html', folders=folders, files=files, subpath=subpath)

@app.route('/download/<path:filepath>')
def download_file(filepath):
    return send_from_directory(BASE_DIR, filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=21215, debug=False)
