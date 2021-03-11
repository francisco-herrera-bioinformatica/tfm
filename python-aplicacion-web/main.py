from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename
import pymongo

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

ALLOWED_EXTENSIONS = {'pdf'}
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
bbdd = cliente["tfm-ltcyt"]

def ficheros_permitidos(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        etiqueta = request.form['etiqueta']
        fecha = request.form['fecha']
        tipo = request.form['tipo']

        if 'fichero' not in request.files:
            print('No hay fichero')
            return redirect(request.url)

        fichero = request.files['fichero']

        if fichero.filename == '':
            print('No file selected')
            return redirect(request.url)
        if fichero and ficheros_permitidos(fichero.filename):
            filename = secure_filename(fichero.filename)

            procesar_fichero(tipo, fichero)

            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            # return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')

def procesar_fichero(tipo, fichero):
    flash('Fichero procesado con éxito')
    return render_template('index.html')

    coleccion = bbdd["aferesis"]

    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
