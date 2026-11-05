# pai 404, api*

> pai presente\*ausente

API de humor feita com Python e Flask. Você manda uma mensagem e ela facilita o serviço dos pais de fim de semana.

## Como funciona

A API recebe uma mensagem pela URL, remove acentos e maiúsculas e procura por palavras-chave (palavra inteira, sem falso positivo):

| Palavra na mensagem | Resposta |
|---|---|
| `pensão` / `pensao` | `Silencio Profundo` |
| `pix` | `XX reais ta bom?` (valor sorteado entre 25 e 40) |
| qualquer outra coisa | `Joia` |

Se a mensagem tiver as duas palavras, `pensão` tem prioridade.

## Requisitos

- Python 3.8 ou superior
- Git (opcional, para clonar)

## Instalação

```bash
git clone https://github.com/DaviKirk/pai-404.git
cd pai-404
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (cmd)
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando

```bash
python app.py
```

A API sobe em `http://localhost:5000`.

## Endpoints

### `GET /`

Retorna uma resposta vazia. Serve só para checar se o servidor está no ar.

### `GET /menssage?msg=<texto>`

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `msg` | string | sim | Mensagem enviada ao pai |

**Exemplos:**

```
http://localhost:5000/menssage?msg=pai, me manda um pix
http://localhost:5000/menssage?msg=e a pensão?
http://localhost:5000/menssage?msg=oi
```

**Resposta de sucesso (200):**

```json
{
  "success": true,
  "menssage": "35 reais ta bom?"
}
```

**Resposta de erro (400):**

Acontece quando `msg` não é enviado, está vazio ou tem só espaços.

```json
{
  "success": false,
  "menssage": "ERROR - PARAMETER ?msg= IS NOT FOUND OR MENSSAGE NOT EXIST"
}
```

### Testando com curl

```bash
curl "http://localhost:5000/menssage?msg=pix"
```

## Estrutura do projeto

```
.
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Observações

- O servidor roda com `debug=False`.
- Com `host='0.0.0.0'` a API fica acessível para outros dispositivos da rede. Para uso só local, troque por `localhost` no `app.run(...)`.

## Tecnologias

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)

## Licença

Projeto sem fins sérios. Use como quiser.
