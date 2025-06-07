# Game Finder - Buscador de Jogos Multi-Plataforma

Um buscador automatizado de jogos que permite pesquisar preços e informações em múltiplas plataformas digitais simultaneamente, com ferramentas avançadas de comparação de preços e descoberta de jogos gratuitos.

## 📋 Visão Geral

O Game Finder é uma ferramenta desenvolvida em Python que utiliza automação web para buscar jogos nas principais plataformas de distribuição digital:

- **Steam** - A maior plataforma de jogos para PC
- **Nuuvem** - Loja brasileira de jogos digitais
- **Epic Games Store** - Plataforma da Epic Games com suporte completo

## 🚀 Funcionalidades

### Funcionalidades Principais

- ✅ **Busca simultânea** em múltiplas plataformas (Steam, Nuuvem, Epic Games)
- ✅ **Interface intuitiva** de linha de comando com cores e animações
- ✅ **Detecção automática** de promoções e descontos em tempo real
- ✅ **Comparação de preços** side-by-side entre plataformas
- ✅ **URLs diretas** para as páginas dos jogos encontrados
- ✅ **Descoberta de jogos gratuitos** na Epic Games Store

## 📦 Dependências

### Requisitos do Sistema

- **Python 3.8+**
- **Google Chrome** (versão mais recente)
- **ChromeDriver** (será baixado automaticamente pelo Selenium)

### Dependências Python

As dependências estão listadas no arquivo `requirements.txt`:

```
selenium>=4.15.0
rich>=13.0.0
questionary>=2.0.0
```

## 🛠️ Instalação

### 1. Clone ou baixe o projeto

```bash
git clone <url-do-repositorio>
cd game-finder
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv game_finder
```

### 3. Ative o ambiente virtual

```bash
# Windows
game_finder\Scripts\activate

# Linux/Mac
source game_finder/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Verifique a instalação do Chrome

Certifique-se de que o Google Chrome está instalado e atualizado em seu sistema.

## 📱 Como Usar

### Execução Básica

```bash
python main.py
```

### Fluxo de Uso

1. **Selecione a opção desejada:**

   - Steam
   - Nuuvem
   - Epic Games
   - Todas as plataformas
   - Verificar Jogos Gratuitos Epic Games
   - Sair

2. **Para busca de jogos específicos:**

   - Digite o nome do jogo desejado
   - Aguarde a busca automática em todas as plataformas selecionadas

3. **Para jogos gratuitos:**

   - Selecione "Verificar Jogos Gratuitos Epic Games"
   - Visualize jogos gratuitos disponíveis agora e futuros lançamentos

4. **Visualize os resultados** organizados com:

   - Nome do jogo encontrado
   - Plataforma de origem
   - Preço atual e original (se em promoção)
   - Desconto aplicado
   - Status especial
   - Link direto para a página da loja

5. **Continue pesquisando** ou finalize o programa

### Comparação de Tempo: Manual vs Automático

| Atividade                      | Tempo Manual      | Tempo Automatizado | Economia  |
| ------------------------------ | ----------------- | ------------------ | --------- |
| Buscar 1 jogo em 3 plataformas | 3-5 minutos       | 8-12 segundos      | 95%       |
| Verificar jogos gratuitos Epic | 2-3 minutos       | 5-8 segundos       | 97%       |
| Comparar preços e promoções    | 5-7 minutos       | 1-2 segundos       | 98%       |
| Anotar links e informações     | 2-3 minutos       | Automático         | 100%      |
| **TOTAL por pesquisa**         | **12-18 minutos** | **15-25 segundos** | **97.7%** |

## 🏗️ Estrutura do Projeto

```
game-search/
├── main.py              # Arquivo principal - gerencia fluxo da aplicação
├── search_manager.py    # Gerenciador de buscas e WebDriver
├── steam_search.py      # Módulo de busca Steam
├── nuuvem_search.py     # Módulo de busca Nuuvem
├── epic_search.py       # Módulo de busca Epic Games + jogos gratuitos
├── ui.py               # Interface do usuário e formatação
├── requirements.txt    # Dependências Python
```

**Desenvolvido com ❤️ para facilitar a busca por jogos nas melhores plataformas digitais!**
