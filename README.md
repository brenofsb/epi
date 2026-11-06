   # Controle de EPI

Sistema de gerenciamento de equipamentos de proteção individual (EPIs), desenvolvido com Django como projeto acadêmico para a matéria de Desenvolvimento de Sistemas.

## Funcionalidades

- Cadastro, listagem, pesquisa por nome, edição e exclusão de colaboradores.
- Cadastro, listagem, edição e exclusão de equipamentos.
- Cadastro de empréstimos associados a colaboradores e equipamentos.
- Controle das datas de empréstimo, previsão de devolução e devolução efetiva.
- Status de empréstimo: Emprestado, Fornecido, Devolvido, Danificado e Perdido.
- Atualização do status e registro da data e observação da devolução.
- Consulta de empréstimos com filtros por colaborador, equipamento e status.
- Login e logout de usuários.
- Proteção das telas do sistema para usuários autenticados.
- Django Admin disponível para administração de usuários, grupos, permissões e dos modelos registrados.
- Menu lateral e identificação do usuário na interface.

As permissões de grupos configuradas no Django Admin são aplicadas ao próprio Admin. As telas personalizadas do sistema exigem login, mas não aplicam permissões de grupo específicas por operação.

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

5. Crie um superusuário para acessar o Django Admin e gerenciar usuários e grupos:

   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

7. Acesse:

   - Sistema: <http://127.0.0.1:8000/>
   - Django Admin: <http://127.0.0.1:8000/admin/>

O banco SQLite é armazenado no arquivo `db.sqlite3` na raiz do projeto. Usuários podem ser criados pelo Django Admin após o primeiro superusuário ser configurado.
