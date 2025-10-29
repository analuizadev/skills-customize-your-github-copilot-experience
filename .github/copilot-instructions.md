# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Conventional Commits

Este projeto segue o padrão de Conventional Commits para mensagens de commit. Cada mensagem de commit deve seguir a estrutura:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos de Commit

- `feat`: Uma nova funcionalidade
- `fix`: Correção de bug
- `docs`: Alterações em documentação
- `style`: Alterações que não afetam o significado do código (espaços, formatação, etc)
- `refactor`: Alteração de código que não corrige bug nem adiciona funcionalidade
- `test`: Adicionando ou modificando testes
- `chore`: Alterações em arquivos de build, configurações, etc

### Exemplos:

```
feat(assignments): adiciona nova tarefa de algoritmos

fix(templates): corrige link quebrado no template de exercícios

docs(README): atualiza instruções de instalação

style(css): formata arquivos CSS seguindo styleguide

refactor(js): simplifica lógica de carregamento de tarefas

test(utils): adiciona testes para funções utilitárias

chore(deps): atualiza dependências do projeto
```