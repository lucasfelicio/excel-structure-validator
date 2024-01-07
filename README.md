# Validador de Excel

## Sobre o projeto
Este projeto teve como objetivo praticar a solução proposta pelo [Luciano Filho](https://github.com/lvgalvao) vi linkedin para a realização de validações de arquivos excel.

Segundo o Luciano "com esta função, você pode validar rapidamente se a estrutura do novo arquivo Excel corresponde à do arquivo modelo. Economizando tempo, evitando erros e garantindo a consistência dos dados!."

Confira a publicação na integra [Aqui](https://www.linkedin.com/posts/lucianovasconcelosf_como-validar-excel-activity-7146130884570656768-k-xo?utm_source=share&utm_medium=member_desktop).

## Requisitos

* Poetry 
* Python 3.12.0
* Pandas
* Loguru

## Configure o projeto

1. Clone o repositório.

```bash
git clone https://github.com/lucasfelicio/excel-structure-validator.git
```
2. Navege até o diretório do projeto e instale as dependências.
```bash
poetry install
```
3. Ative o ambiente virtual do projeto. 
```bash
poetry shell
```

## Excutante o projeto

Para executar o projeto é necessário 
* colocar o arquivo modelo na pasta data/modelo
* colocar os arquivos de entrada na pasta data/input/

O arquivo modelo servirá como base para a realização das comparações com os arquivos de entrada para determinar se estes arquivos atendem aos requisitos ou não. 

* Execute o projeto. 
```bash
task run
```

Todos os crétidos à [Luciano Filho](https://github.com/lvgalvao) 😎