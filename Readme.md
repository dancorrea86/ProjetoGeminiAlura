# **Companheiro de Estudos Inteligente com Gemini (Resumo)** 🚀

## Descrição 📘

### O que é:

Um aplicativo que utiliza a inteligência do Google Gemini para te auxiliar nos estudos.

![app](https://github.com/dancorrea86/ProjetoGeminiAlura/blob/main/static/imagens/app.png)

### Como funciona:

- Conecta-se às suas notas de estudo para te ajudar a revisar conceitos. 
- Entende o contexto da sua pergunta para fornecer respostas relevantes, recuperando as notas de estudos.

## Como funciona

O aplicativo inteligente projetado para elevar seus estudos. Ao integrar-se à poderosa inteligência do Google Gemini, este aplicativo simplifica sua jornada educacional.
Como funciona? Imagine conectar-se diretamente às suas notas de estudo para uma revisão personalizada. Este companheiro de estudos compreende o contexto das suas perguntas, fornecendo respostas precisas e relevantes, utilizando suas próprias anotações.

## Instalação do projeto 🔍

Para instalar os pacotes necessarios abra o CMD e navegue até a pasta do projeto.

Na pasta rode o comando de instalação dos pacotes requiridos.

```bash
pip install -r requirements.txt
```
## Preparando o ambiente

Na pasta principal do projeto crie um arquivo chamado ".env". Neste arquivo ficará salva a chave da API do Google Gemini.

GOOGLE_API_KEY=**sua_chave_api**

## Preparação do projeto

O projeto inicial tem um conjunto de notas sobre história, mas é possivel alterar as notas incluindo suas notas de preferência.
Para realizar a alteração basta salvar as notas em formato .md na pasta "biblioteca" no projeto.

Em seguida para transformar esse arquivo em um único arquivo Json, rode o arquivo Python "conversorJson.py".

> python conversorJson.py

Esse script vai ler todos os arquivos tipo .md dentro da pasta biblioteca e vai gerar um arquivo do tipo Json, com o título e o artigo.

## Rodando a aplicação

Para rodar a aplicação, utilize o comando.

> flask run

## Utilizando o sistema.

Na página princial existe um formulário.

![Primeira Etapa](https://github.com/dancorrea86/ProjetoGeminiAlura/blob/main/static/imagens/pesquisa1.jpg)

![Segunda Etapa](https://github.com/dancorrea86/ProjetoGeminiAlura/blob/main/static/imagens/pesquisa2.0.jpg)

![Terceira Etapa](https://github.com/dancorrea86/ProjetoGeminiAlura/blob/main/static/imagens/pesquisa3.jpg)

## Licença 📄

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Implementações pendentes 📄

- Criar função para limpar o Chat.
- Melhorar o visual da aplicação.
- Refatorar o código para maior separação e reutilização.

## Contato 📬

- [GitHub](https://github.com/dancorrea86)
- danielmacielcorrea@gmail.com
- [Linkedin](https://www.linkedin.com/in/danielmacielcorrea/)

