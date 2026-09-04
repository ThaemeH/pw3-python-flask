# Music Catalog (Flask + API iTunes)

Aplicação Flask que consome a **API pública da iTunes/Apple** (não exige chave/autenticação) para
montar um catálogo com o Top 100 do momento e exibir os detalhes de cada música.

## Estrutura (baseada no exemplo enviado)

```
music-api-app/
├── app.py                     # Inicializa o Flask e chama as rotas
├── controllers/
│   └── routes.py              # Rotas que consomem a API (urllib.request + json)
├── views/
│   ├── base.html              # Layout base (Bootstrap)
│   ├── catalogo.html          # Rota principal "/" - catálogo (nome, imagem, título)
│   └── detalhes.html          # Rota secundária "/item/<id>" - detalhes do item
└── static/
    └── css/style.css
```

## APIs utilizadas

- **Catálogo (chart Top 100):**
  `https://itunes.apple.com/us/rss/topsongs/limit=50/json`
- **Detalhe por ID (lookup):**
  `https://itunes.apple.com/lookup?id=<id>`

## Rotas

- **`GET /`** → rota principal. Consome o feed RSS "Top Songs" da Apple e gera o catálogo,
  exibindo para cada item a imagem (capa do álbum em alta resolução), o título da música e o
  nome do artista.
- **`GET /item/<int:id>`** → rota secundária. Ao clicar em "+ Info" em um item do catálogo, o `id`
  da faixa (track ID da Apple) é passado via parâmetro de rota e a aplicação consulta o endpoint
  `lookup` para exibir os dados detalhados: álbum, gênero, duração, data de lançamento, preço,
  prévia de 30s em áudio e link para ouvir na Apple Music.

## Como rodar

1. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   python app.py
   ```
4. Acesse no navegador: `http://localhost:5000`

## Observações

- A biblioteca usada para consumir a API é a `urllib.request` (padrão do Python), com `json.loads`
  para converter a resposta, exatamente como no arquivo de exemplo (`apigames` do projeto
  "aula-07-integracao-com-api").
- A API da iTunes é pública e gratuita, sem necessidade de cadastro ou chave.
- Caso queira trocar de API de música novamente, basta ajustar as URLs `API_CHART_URL` e
  `API_LOOKUP_URL` em `controllers/routes.py` e os nomes dos campos usados nos templates.
