# Controle de EPI

Sistema de gerenciamento de equipamentos de proteção individual (EPIs), desenvolvido com Django como projeto acadêmico para a matéria de Desenvolvimento de Sistemas.

## Funcionalidades

- Cadastro, listagem, pesquisa por nome, edição e exclusão de colaboradores.
- Cadastro, listagem, edição e exclusão de equipamentos.
- Cadastro de empréstimos vinculados a um colaborador e a um equipamento.
- Controle das datas do empréstimo, previsão de devolução e devolução efetiva.
- Status do empréstimo: Emprestado, Fornecido, Devolvido, Danificado ou Perdido.
- Atualização de status e registro da data e observação de devolução.
- Mensagens de sucesso e erro nas operações de cadastro e atualização.
- Menu lateral e identificação visual do usuário exibida de forma estática.

Os relatórios e os filtros por colaborador, equipamento e status não fazem parte do escopo desta etapa. O projeto também não implementa autenticação ou funcionalidades de login e logout.

## Tecnologias

- Python
- Django 6.1.1
- SQLite

## Como executar

1. Clone o repositório e entre na pasta do projeto:

   ```bash
   git clone https://github.com/brenofsb/epi.git
   cd epi
   ```

2. (Opcional, recomendado) Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows, ative com:

   ```powershell
   .venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie ou atualize as tabelas do banco SQLite:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

6. Acesse <http://127.0.0.1:8000/>.

O banco SQLite é armazenado no arquivo `db.sqlite3` na raiz do projeto. Não é necessário criar um usuário para acessar as telas do sistema.
