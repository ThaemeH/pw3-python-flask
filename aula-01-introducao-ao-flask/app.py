#importando o flask para a aplicação
from flask import Flask, render_template

#carregando o Flask na variavel app
app = Flask(__name__, template_folder='views')
#variaveis com dois _ são variaveis de ambiente do python
#__name__ representa o nome da aplicação

#criando a rota principal do site
@app.route('/')
#def cria funçãos
def home():
    return render_template('index.html')

#desafio
@app.route('/games')
def games():
    #criando variaveis para a rota
    titulo = "Portal 2"
    ano = 2011
    categoria = "Puzzle"
    #Lista de jogadores (uma lista é um vetor/array)
    jogadores = ['Marcos','Richard','Miguel','Renato','Pedro']
    
    #enviando as variaveis para html
    return render_template('games.html', titulo = titulo, ano = ano, categoria = categoria, jogadores = jogadores)

@app.route('/consoles')
def consoles():
    #criando um objeto
    console = {"Nome": "Playstation 2",
               "Fabricante": "Sony",
               "Ano": 2000}
    return render_template('consoles.html', console = console)


#iniciando o servidor na porta 5000
if __name__ == '__main__':
#verificando se o arquivo guardado em __name__ é o arquivo principal
    app.run(port=5000, debug=True)
#o metodo .run inicia o servidor