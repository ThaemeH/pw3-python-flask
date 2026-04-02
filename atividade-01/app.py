from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lista')
def games():
    return render_template('lista.html')

@app.route('/formularioAlbum')
def formulatioAlbum():
    return render_template('formularioAlbum.html')

@app.route('/formularioMusica')
def formularioMusica():
    return render_template('formularioMusica.html')


if __name__ == '__main__':
    app.run(port=4000, debug=True)
