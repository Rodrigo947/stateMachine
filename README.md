## Cadastro de usuário WEB

## Principais Tecnologias Utilizadas

* Django REST framework v3.13.1 (https://www.django-rest-framework.org/)
* NuxtJS v2.15.8 (https://nuxtjs.org/)
* Vuetify v2.6.1 (https://vuetifyjs.com/en/components/app-bars/)
* Docker v4.3.2 (https://docs.docker.com/)
* Docker Compose v2.2.1
* Portainer (https://www.portainer.io/)
* PostgreSQL v13.3
* pgAdmin

## Iniciando o ambiente

1. Na pasta docker, crie um arquivo .env e copie o conteúdo do arquivo example.env.
2. Caso necessário, altere as variáveis de ambiente.
3. Execute o comando abaixo para iniciar os containers:
```
$ docker-compose -p state_machine up -d
```

## Informações gerais de cada Container

### sm_portainer
  Container para gerenciamento de Containers do Docker.
  
  As credenciais devem ser geradas no momento que acessar o link.
  
  Link: http://localhost:9002/
  
### sm_pgadmin
  Container para gerenciamento do banco de dados Postgres.
  
  Login: pgadmin@pgadmin.com
  
  Senha: pgadmin
  
  Link: http://localhost:9003/

### sm_postgres
  Contém o banco de dados relacional PostgreSQL
  
  As credenciais devem ser geradas no momento que acessar o link.
  
  Database: db
  
  User: postgres
  
  Password: postgres
  
  Host: 192.168.100.4
  
  Porta: 9004

### sm_backend
  Ao iniciar esse Container uma API em Django é criada.
  
  Um super usuário é criado e as migrations são executadas no momento do deploy.
  
  Uma documentação das rotas está disponível para consulta apenas no ambiente de desenvolvimento.
  
  Login: django@django.com
  
  Senha: django
  
  Documentação Swagger: http://localhost:9005/swagger/
  
  Documentação Redoc: http://localhost:9005/redoc/

### sm_frontend
  Por último, esse Container possui o frontend com NuxtJS.
  
  As mesmas credenciais do super usuário pode ser usada.
  
  Login: django@django.com
  
  Senha: django
  
  Link: http://localhost:9006/
