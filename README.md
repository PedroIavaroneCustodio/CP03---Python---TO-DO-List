# 🧠 Sistema de Gerenciamento de Tarefas

## 📘 Descrição do Projeto
O **Sistema de Gerenciamento de Tarefas** é uma aplicação em **Python** que permite ao usuário **cadastrar, listar, atualizar e remover tarefas** de forma simples e intuitiva.  
O projeto foi desenvolvido com foco em **organização, modularização e persistência de dados**, utilizando **arquivos JSON** para armazenar as tarefas de forma permanente.

---

## ⚙️ Funcionalidades

### ✅ Cadastro de Tarefas
- Permite criar novas tarefas informando:
  - Descrição  
  - Data de vencimento  
  - Status inicial (Pendente, Em andamento ou Concluída)

### 📋 Listagem de Tarefas
- Exibe todas as tarefas cadastradas.  
- Possibilidade de filtrar por status (pendente, em andamento, concluída).

### 🔄 Atualização de Tarefas
- Editar informações da tarefa (descrição, data, status).  
- Marcar como concluída.

### 🗑️ Remoção de Tarefas
- Excluir tarefas existentes pelo índice.

### 💾 Persistência de Dados
- Todas as tarefas são salvas automaticamente em um arquivo `tarefas.json`.  
- Ao reiniciar o sistema, as tarefas anteriores são carregadas automaticamente.

---

## 🧩 Estrutura do Projeto
gerenciador_tarefas/
- ├── main.py           # Arquivo principal que inicia o programa
- ├── tarefas.py        # CRUD das tarefas (criar, listar, atualizar, remover)
- ├── persistencia.py   # Salvamento e carregamento de dados em JSON
- └── interface.py      # Interface de linha de comando (menu interativo)

---

## 💻 Como Executar

### 1. Clone o repositório:
git clone https://github.com/PedroIavaroneCustodio/CP03---Python---TO-DO-List.git

### 2. Acesse o diretório:
cd CP03---Python---TO-DO-List

### 3. Execute o programa:
python main.py

---

## 👥 Integrantes
- Pedro Iavarone — RM 567638
- Rafael Tavares — RM 567357
- Yuri Santos — RM 568512
- Gabriel Muniz — RM 568237