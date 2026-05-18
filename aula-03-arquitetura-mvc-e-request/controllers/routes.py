from flask import render_template, request, redirect, url_for

# CRIANDO A ROTA PRINCIPAL DO SITE
#criando a função principal para iniciar as rotas
def init_app(app):
    #VARIAVEL GLOBAL
    listaConsoles =['Playstation 5','Xbox One', 'Super Nintendo', 'Atari', '3DS']
    listaGames =[{'titulo':'Super Meat Boy','ano':2008, 'categoria':'Plataforma','plataforma':'3DS'}]
    
    @app.route('/')
    # def cria funções no Python
    def home():
        return render_template('index.html')


    @app.route('/games')
    def games():
    # Criando variáveis para a rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        # Lista de jogadores (uma lista é um vetor/array)
        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
        # Enviando as variáveis para o HTML
        return render_template('games.html',
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores)


    @app.route('/consoles', methods=['GET','POST'])
    def consoles():
        # Criando um objeto
        console = {"Nome": "Playstation 2",
               "Fabricante": "Sony",
               "Ano": 2000}
        
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))
        return render_template('consoles.html',
                           console=console,
                           listaConsoles = listaConsoles)
        
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method=='POST':
            #aq ele irá gravar os dados na lista
            listaGames.append({'titulo': request.form.get('titulo'), 'ano': request.form.get('ano'), 'categoria' : request.form.get('categoria'), 'plataforma': request.form.get('plataforma')})
            #aqui o usuario sera redirecionado novamente para a pagina
            return redirect(url_for('cadgames'))
            
        return render_template('cadgames.html', listaGames = listaGames)