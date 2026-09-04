# Importando o Flask para a aplicação
from flask import render_template

# Importando as bibliotecas para consumir a API (mesmas do exemplo)
import urllib.request
import json

# URL BASE da API de música (iTunes - não exige chave/autenticação)
# Feed RSS com o TOP 100 do momento (chart oficial da Apple) em formato JSON
API_CHART_URL = 'https://itunes.apple.com/us/rss/topsongs/limit=50/json'
# Endpoint de busca detalhada por ID
API_LOOKUP_URL = 'https://itunes.apple.com/lookup?id='


# Criando a função principal para inicializar as rotas
def init_app(app):

    # ROTA PRINCIPAL - CATÁLOGO DE MÚSICAS (TOP 100 iTunes)
    # Consome a API e exibe nome (artista), imagem (capa) e título de cada item
    @app.route('/')
    def home():
        # Fazendo a requisição para a API
        req = urllib.request.urlopen(API_CHART_URL)
        # Lendo a resposta da requisição
        dados = req.read()
        # Convertendo os dados de JSON para dicionário Python
        resposta = json.loads(dados)
        # O feed do iTunes retorna as músicas dentro de feed -> entry
        entradas = resposta['feed']['entry']

        # Montando uma lista mais simples para enviar ao template
        listaMusicas = []
        for musica in entradas:
            listaMusicas.append({
                # ID usado na rota de detalhes
                'id': musica['id']['attributes']['im:id'],
                'titulo': musica['im:name']['label'],
                'artista': musica['im:artist']['label'],
                # Pega a imagem de maior resolução disponível (última da lista)
                'imagem': musica['im:image'][-1]['label']
            })

        # Enviando a lista de músicas para o template
        return render_template('catalogo.html', listaMusicas=listaMusicas)

    # ROTA SECUNDÁRIA - DETALHES DE UM ITEM ESPECÍFICO
    # Recebe o identificador (id) da música via parâmetro de rota
    @app.route('/item/<int:id>')
    def item(id):
        # Montando a URL de detalhe com o id recebido
        url = f'{API_LOOKUP_URL}{id}'
        # Fazendo a requisição para a API
        req = urllib.request.urlopen(url)
        # Lendo a resposta da requisição
        dados = req.read()
        # Convertendo os dados de JSON para dicionário Python
        resposta = json.loads(dados)

        # Verificando se a música foi encontrada
        if resposta['resultCount'] == 0:
            return f'Música com a ID {id} não foi encontrada.'

        # O lookup retorna uma lista com um único resultado
        musicaInfo = resposta['results'][0]

        # Trocando a capa pequena (100x100) por uma versão em alta resolução (600x600)
        musicaInfo['artworkUrl600'] = musicaInfo['artworkUrl100'].replace(
            '100x100bb', '600x600bb')

        # Enviando os dados da música para o template de detalhes
        return render_template('detalhes.html', musicaInfo=musicaInfo)
