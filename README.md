<p align="center">
    <a src="https://fga-eps-mds.github.io/2019.2-Amika-Wiki/">
        <img src="https://raw.githubusercontent.com/fga-eps-mds/2019.2-Amika-Wiki/master/assets/img/AmikaComNome.png">
    </a>
</p>


#### Ambientes:
- [Desenvolvimento](https://amika-backend-dev.herokuapp.com/)
- [Homologação](https://amika-backend-stg.herokuapp.com/)
- [Produção](https://amika-backend.herokuapp.com/)

#### [Amika-Backend](https://github.com/fga-eps-mds/2019.2-Amika-Backend)
[![Build Status](https://travis-ci.org/fga-eps-mds/2019.2-Amika-Backend.svg?branch=master)](https://travis-ci.org/fga-eps-mds/2019.2-Amika-Backend)
[![Maintainability](https://api.codeclimate.com/v1/badges/fa0fbed2c8fa7014e542/maintainability)](https://codeclimate.com/github/fga-eps-mds/2019.2-Amika-Backend/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fa0fbed2c8fa7014e542/test_coverage)](https://codeclimate.com/github/fga-eps-mds/2019.2-Amika-Backend/test_coverage)
#### Ambientes:
- [Desenvolvimento](https://amika-dev.herokuapp.com/)
- [Homologação](https://amika-stg.herokuapp.com/)
- [Produção](https://amika-prod.herokuapp.com/)

## Sobre

Amika é um Progressive Web App com o objetivo de auxiliar a organização da disciplina de Tópicos Especiais em Engenharia de Software, com abordagem em Felicidade, da Universidade de Brasília. Assim como também proporcionar para os alunos um ambiente de interação e ajuda para lidar com problemas de saúde mental, fornecendo uma experiência mais agradável.

## Tecnologias Utilizadas

Este repositório se refere ao Backend da aplicação, caso deseje contribuir com nosso Frontend, visite o repositório: [Amika-Frontend](https://github.com/fga-eps-mds/2019.2-Amika-Frontend). Este repositório foi desenvovido com o framework [Django](https://www.djangoproject.com) escrito em [Python](https://www.python.org) e se comunica com o frontend criando a API da aplicação utilizando o [Django REST framework](https://www.django-rest-framework.org) na qual o Frontend realiza requisições HTTP. O ambiente de desenvolvimento é isolado em containers com o [Docker](https://www.docker.com) e o gerenciamento é feito pelo [Docker Compose](https://docs.docker.com/compose/). A integração contínua é feita pelo [Travis CI](https://docs.travis-ci.com). Os deployments de desenvolvimentos, homologações e produções são feitos no [Heroku](https://devcenter.heroku.com).

## Instalação

  #### Pré-requisitos
  * [Git](https://git-scm.com/)
  * [Docker](https://www.docker.com/get-docker)
  * [Docker-composer](https://docs.docker.com/compose/install/#install-compose)

  #### Configuração

  Clone o repositório no diretório desejado
  ```bash
  git clone https://github.com/fga-eps-mds/2019.2-Amika-Backend
  ```

  Utilize o seguinte comando para subir a aplicação
  ```bash
  docker-compose up
  ```

  A aplicação pode ser acessada através do localhost:
  ```
  localhost:8000
  ```
  
  
  ## Comandos Úteis

  #### Docker
  
  Listar containers ativos
  ```bash
  docker ps
  ```

  Entrar no bash do container
  ```bash
  docker exec -it backend bash
  ```

  Parar o container
  ```
  docker stop backend
  ```
  
  Remover o container
  ```
  docker rm backend
  ```

  #### Django(Comandos executados dentro do container)

  Criar um novo app
  ```bash
  python3 manage.py startapp nomeDoApp
  ```

  Gera as migrações
  ```bash
  python3 manage.py makemigrations
  ```

  Realiza as migrações
  ```
  python3 manage.py migrate
  ```

  Roda os testes
  ```
  python3 manage.py test
  ```
  
## Documentação

Documentação do porjeto está disponível em [Amika Wiki](https://fga-eps-mds.github.io/2019.2-Amika-Wiki/#/).

#### Como contribuir
Para contribuir com o projeto é importante seguir o [Guia de Contribuição](https://github.com/fga-eps-mds/2019.2-Amika-Wiki/blob/master/.github/CONTRIBUTING.md) do repositório, assim como seguir as [Politicas de Commits e Branches](https://fga-eps-mds.github.io/2019.2-Amika-Wiki/#/docs/projeto/planogerencia) presentes no nosso plano de gerencia de software.

## Licença

Este projeto está licenciado sob os termos da [licença MIT](https://github.com/fga-eps-mds/2019.2-Amika-Wiki/blob/master/LICENSE).

Copyright (c) 2019 Amika
