from flask import render_template, request, redirect

musicas = []
albuns = []

def init_app(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/lista')
    def lista():
        return render_template('lista.html', musicas=musicas, albuns=albuns)

    @app.route('/formularioMusica')
    def formularioMusica():
        return render_template('formularioMusica.html')

    @app.route('/formularioAlbum')
    def formularioAlbum():
        return render_template('formularioAlbum.html')

    # CADASTRAR MUSICA
    @app.route('/cadastrarMusica', methods=['POST'])
    def cadastrarMusica():
        nome = request.form.get('nome')
        artista = request.form.get('artista')
        nota = request.form.get('nota')
        resenha = request.form.get('resenha')

        musica = {
            'nome': nome,
            'artista': artista,
            'nota': nota,
            'resenha': resenha
        }

        musicas.append(musica)

        return redirect('/lista')

    # CADASTRAR ALBUM
    @app.route('/cadastrarAlbum', methods=['POST'])
    def cadastrarAlbum():
        nome_album = request.form.get('nome_album')
        artista_album = request.form.get('artista_album')

        album = {
            'nome_album': nome_album,
            'artista_album': artista_album
        }

        albuns.append(album)

        return redirect('/lista')