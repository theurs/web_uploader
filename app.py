from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
import random
import string

import cfg

app = Flask(__name__)


BOT_LINK = cfg.BOT_LINK


UPLOAD_FOLDER = cfg.UPLOAD_FOLDER
ALLOWED_EXTENSIONS = cfg.ALLOWED_EXTENSIONS
MAX_FILE_SIZE = cfg.MAX_FILE_SIZE
MAX_UPLOAD_FOLDER_SIZE = cfg.MAX_UPLOAD_FOLDER_SIZE


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_upload_folder_size() -> int:
    """Calculates the total size of the upload folder."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(app.config['UPLOAD_FOLDER']):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def cleanup_old_files():
    """Deletes the oldest files in the upload folder if it exceeds the maximum size."""
    if get_upload_folder_size() > MAX_UPLOAD_FOLDER_SIZE:
        files = sorted(
            [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER)],
            key=os.path.getmtime
        )
        bytes_to_delete = get_upload_folder_size() - MAX_UPLOAD_FOLDER_SIZE
        deleted_bytes = 0
        for file_path in files:
            if deleted_bytes >= bytes_to_delete:
                break
            try:
                deleted_bytes += os.path.getsize(file_path)
                os.remove(file_path)
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")


def generate_safe_filename(length: int = 30) -> str:
    """Generates a random filename without dots and hyphens."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            # Генерируем безопасное имя файла без точек и тире
            safe_filename = generate_safe_filename()
            filename_with_extension = safe_filename
            filename = secure_filename(filename_with_extension) # Для безопасности файловой системы
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cleanup_old_files()
            # Формируем ссылку для Telegram бота с командой /start
            telegram_link = f'{BOT_LINK}?start={safe_filename}'
            return jsonify({'message': 'File uploaded successfully', 'telegram_link': telegram_link})
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def download_file(filename):
    """Serves the uploaded file."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=cfg.DEBUG, host=cfg.ADDRESS, port=cfg.PORT)
