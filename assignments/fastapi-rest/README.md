# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, os alunos aprenderão a desenvolver uma API REST moderna usando o framework FastAPI em Python, implementando operações CRUD e documentação automática.

## 📝 Tasks

### 🛠️ Configuração Inicial e Endpoints Básicos

#### Description
Você irá criar uma API REST para gerenciar uma biblioteca de livros, implementando os endpoints básicos para listar e adicionar livros.

#### Requirements
Completed program should:

- Configurar um projeto FastAPI básico com as dependências necessárias
- Criar um modelo Pydantic para representar um livro (título, autor, ano, ISBN)
- Implementar um endpoint GET `/books` para listar todos os livros
- Implementar um endpoint POST `/books` para adicionar um novo livro
- Incluir validação de dados usando Pydantic
- Testar os endpoints usando o Swagger UI integrado

### 🛠️ Operações Avançadas e Tratamento de Erros

#### Description
Expanda a API adicionando mais operações CRUD e implementando tratamento adequado de erros.

#### Requirements
Completed program should:

- Implementar endpoint GET `/books/{id}` para buscar um livro específico
- Implementar endpoint PUT `/books/{id}` para atualizar um livro
- Implementar endpoint DELETE `/books/{id}` para remover um livro
- Adicionar tratamento de erros para casos como livro não encontrado
- Implementar paginação na listagem de livros
- Adicionar filtros de busca (por autor, título ou ano)
- Documentar todos os endpoints usando docstrings do FastAPI