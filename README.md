# 📚 Sistema de Biblioteca

> Projeto desenvolvido em Python para gerenciamento de livros e empréstimos de uma biblioteca.  
> Trabalho da disciplina de Programação - UNIBAVE

## 👥 Autores e Responsabilidades

### 👤 Caio Vargas — Estrutura base e classes
✅ **Responsável por montar a base do projeto e as classes principais.**

- Criar as classes:
  - `Livro` (título, autor, ano, disponível)
  - `Usuario` (nome, matrícula)
  - `Emprestimo` (livro, usuário, datas)
- Criar as listas principais em memória:
  - `livros = []`
  - `usuarios = []`
  - `emprestimos = []`
- Criar o menu principal com as opções do sistema (usar `while` e `input()`)

### 👤 Bruno Fernandes — CRUD de Livros
**Responsável pelas operações com os livros.**

Funções a implementar:
- `cadastrar_livro()`
- `listar_livros()`
- `editar_livro()`
- `remover_livro()`

Validações:
- Verificar se já existe livro com o mesmo título
- Controlar o campo `disponivel` (True/False)

### 👤 Arthur Martinelli — CRUD de Usuários e listagens
**Responsável por gerenciar os usuários e mostrar informações.**

Funções a implementar:
- `cadastrar_usuario()`
- `listar_usuarios()`
- `listar_livros_emprestados_por_usuario()`

Funcionalidade extra (opcional):
- Implementar histórico de empréstimos

### 👤 Sidnei Freitas — Empréstimos e Devoluções
**Responsável pela parte de empréstimos e regras de negócio.**

Funções a implementar:
- `realizar_emprestimo()`
- `devolver_livro()`

Validações:
- Verificar se o livro está disponível antes de emprestar
- Atualizar o status (`disponivel = False` ao emprestar e `True` ao devolver)
- Controlar datas e opcionalmente prazos de devolução

---

## 📁 Estrutura do Projeto

```
projeto-biblioteca-python-unibave/
│
├── models/                  # Módulo com as classes de entidades
│   ├── __init__.py         # Inicialização do módulo
│   ├── livro.py            # Classe Livro (Pessoa 1) ✅
│   ├── usuario.py          # Classe Usuario (Pessoa 1) ✅
│   └── emprestimo.py       # Classe Emprestimo (Pessoa 1) ✅
│
├── menu.py                 # Interface de usuário com menus (Pessoa 1) ✅
├── main.py                 # Arquivo principal de execução (Pessoa 1) ✅
└── README.md               # Este arquivo
```

---

## 🧱 Entidades Principais (Classes já criadas)

### 📖 Livro
- `titulo` - Título do livro
- `autor` - Autor do livro
- `ano` - Ano de publicação
- `disponivel` - Indica se está disponível (True/False)

### 👤 Usuário
- `nome` - Nome do usuário
- `matricula` - Matrícula única do usuário

### 📑 Empréstimo
- `livro` - Livro emprestado
- `usuario` - Usuário que realizou o empréstimo
- `data_emprestimo` - Data em que foi emprestado
- `data_devolucao` - Data de devolução (None se ainda não foi devolvido)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem principal
- **Bibliotecas nativas** - Apenas bibliotecas padrão do Python (`datetime`)

---

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado:
```bash
python --version
```

2. Navegue até o diretório do projeto:
```bash
cd projeto-biblioteca-python-unibave
```

3. Execute o programa:
```bash
python main.py
```

---

## 💡 Como Trabalhar no Projeto

### Bruno (CRUD de Livros):
Edite o arquivo `menu.py` e implemente as funções:
- `cadastrar_livro()` - linha ~27
- `listar_livros()` - linha ~34
- `editar_livro()` - linha ~41
- `remover_livro()` - linha ~48

**Acesse as listas globais:**
```python
global livros  # No início de cada função
```

### Arthur (CRUD de Usuários):
Edite o arquivo `menu.py` e implemente as funções:
- `cadastrar_usuario()` - linha ~58
- `listar_usuarios()` - linha ~65
- `listar_emprestimos_por_usuario()` - linha ~101

**Acesse as listas globais:**
```python
global usuarios, emprestimos  # No início de cada função
```

### Sidnei (Empréstimos):
Edite o arquivo `menu.py` e implemente as funções:
- `realizar_emprestimo()` - linha ~75
- `devolver_livro()` - linha ~85

**Acesse as listas globais:**
```python
global livros, emprestimos  # No início de cada função
```

---

## 📝 Observações Importantes

- **Dados em memória**: Todos os dados são perdidos ao fechar o programa
- **Listas globais**: Use `livros`, `usuarios` e `emprestimos` declaradas no `menu.py`
- **Classes disponíveis**: Importe de `models` quando necessário
  ```python
  from models.livro import Livro
  from models.usuario import Usuario
  from models.emprestimo import Emprestimo
  ```

---

## ✅ Funcionalidades Obrigatórias

- [x] Criar classes (Caio Vargas)
- [ ] Cadastrar livro (Bruno)
- [ ] Listar livros (Bruno)
- [ ] Editar livro (Bruno)
- [ ] Remover livro (Bruno)
- [ ] Cadastrar usuário (Arthur)
- [ ] Listar usuários (Arthur)
- [ ] Realizar empréstimo (Sidnei)
- [ ] Devolver livro (Sidnei)
- [ ] Listar livros emprestados por usuário (Arthur)
- [ ] Bloquear empréstimo se livro não disponível (Sidnei)

## ✨ Funcionalidades Adicionais (Bônus)

- [ ] Histórico de empréstimos por usuário
- [ ] Controlar prazo de devolução
- [ ] Alertas de empréstimos atrasados

---

## 🎓 Critérios de Avaliação

- 🟢 Funcionalidades obrigatórias: nota base
- 🟡 Funcionalidades adicionais: ponto bônus
- 🛑 Requisitos obrigatórios não atendidos: ponto negativo
- ⚠️ Qualidade e clareza do código também serão avaliadas

---

**Projeto desenvolvido para fins acadêmicos - UNIBAVE 2025**

---
