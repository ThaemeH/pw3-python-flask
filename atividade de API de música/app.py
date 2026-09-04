# Comentário no Python
# Importando o Flask para a aplicação
from flask import Flask

# Importando o Controller (rotas)
from controllers import routes

# Carregando o Flask na variável "app"
app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente do Python
# __name__ representa o nome da aplicação

# DEFININDO UMA CHAVE SECRETA
app.config['SECRET_KEY'] = 'meusegredo'

# Enviando a variável app para as rotas
routes.init_app(app)

# Iniciando o servidor na porta 5000
if __name__ == '__main__':
    # Inicializando o servidor:
    app.run(port=5000, debug=True)  # O método .run() inicia o servidor
