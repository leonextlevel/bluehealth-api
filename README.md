# BLUEHEALTH API - TESTE PARA EMPRESA "BLUESTORM SOFTWARE"

# DESAFIO

Uma empresa na área da saúde está precisando criar uma API REST privada (ou seja, que precisará de alguma
forma de autenticação para ser acessada) para que o seu setor financeiro tenha acesso às informações de
compras dos pacientes/clientes da empresa. O setor financeiro precisará acessar informações dos pacientes,
farmácias e transações feitas pelos clientes / recebidas pelas farmácias.

## REQUISITOS PARA EXECUÇÃO DO PROJETO

- Ferramentas `Docker` e `docker-compose` instaladas.
- Biblioteca `make` para utilizar os atalhos.

Obs: Caso opte por não utilizar o make, os comandos completos podem ser obtidos dentro do arquivo "Makefile".

## AMBIENTE DE DESENVOLVIMENTO

1. Crie um arquivo `.env` na raiz do projeto com base em `contrib/env-sample` e altere o que considerar necessário, como as portas, por exemplo.

```bash
cp contrib/env-sample .env
```

2. Faça o build da imagem.

```bash
make build
```

3. Execute o projeto

```bash
make run
```

## CRIAÇÃO DE USUÁRIO PARA UTILIZAÇÃO

1. Acesso o shell do Flask

```bash
make shell
```

2. Dentro do shell importe a função de criação

```python
from bluehealth.services import create_user
```

3. Crie o usuário informando username e password desejados

```python
create_user('username', 'password123')
```

## ORIENTAÇÕES PARA UTILIZAÇÃO

API está toda documentada com o padrão [OpenAPI](https://spec.openapis.org/oas/latest.html) e pode ser acessada através do
link http://localhost:5000/docs (caso não tenha alterado a porta no .env).

Lembre-se de acessar o botão "Authorize" no canto superior direito da página e adicionar as credenciais
do usuário criado no tópico anterior.


## UTILIDADES

1. Para atualizar as dependências

```bash
make build
```

2. Para executar os testes

```bash
make test
```

3. Para verificar erros de formatação no código

```bash
make lint
```

4. Para corrigir os erros de formatação

```bash
make format
```

5. Para acessar o shell do flask

```bash
make shell
```
