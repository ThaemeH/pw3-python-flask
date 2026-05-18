from flask import render_template, request, redirect, url_for
#importando o model de games
from models.database import Game,db, Console
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
    
#rota para o crud
    @app.route('/estoque', methods = ['GET', 'POST'])
    #adicionando o parametro ID a rota
    @app.route('/estoque/delete/<int:id>')
    def estoque(id=None):
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        
        #condição para verificar se o usuário está enviando uma requisição post
        if request.method == 'POST':
            #realiza o cadastro
            #coletando os dados do formulario
            dados = request.form.to_dict()
            #enviando os dados para o model
            newgame= Game(
                dados['titulo'],
                dados['ano'],
                dados['categoria'],
                dados['plataforma'],
                dados['preco'],
                dados['quantidade'],
            )
            #metodo do sqlachemy para gravar no banco
            db.session.add(newgame)
            #confirmação
            db.session.commit()
            return redirect(url_for('estoque'))
            
        games = Game.query.all()
        return render_template('estoque.html', games=games)
    @app.route('/estoque/editar/<int:id>', methods=['GET', 'POST'])
    def editar(id):
         #selecionando o jofo no banco pelo id
         game = Game.query.get(id)
         #verificando se a requisição é post
         if request.method == 'POST':
             dados_form = request.form.to_dict()
             #alterando os dados do jogo
             game.titulo = dados_form['titulo']
             game.ano = dados_form['ano']
             game.categoria = dados_form['categoria']
             game.plataforma = dados_form['plataforma']
             game.preco = dados_form['preco']
             game.quantidade = dados_form['quantidade']
             db.session.commit()
             return redirect(url_for('estoque'))
         return render_template('editGame.html', game=game)
    
    @app.route('/estoque-consoles', methods = ['GET', 'POST'])
    def estoque_consoles():
        #condição para verificar se o usuário está enviando uma requisição post
        if request.method == 'POST':
            #realiza o cadastro
            #coletando os dados do formulario
            dados = request.form.to_dict()
            #enviando os dados para o model
            newconsole= Console(
                dados['nome'],
                dados['fabricante'],
                dados['ano'],
                dados['preco'],
            )
            #metodo do sqlachemy para gravar no banco
            db.session.add(newconsole)
            #confirmação
            db.session.commit()
            return redirect(url_for('estoque_consoles'))
            
        consoles = Console.query.all()
        return render_template('estoque-consoles.html', consoles=consoles)