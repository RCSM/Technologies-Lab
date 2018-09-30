## Notas e comandos

1. Como instalar?
```
$ pip install Django
```

2. Iniciar um projeto
```
$ django-admin startproject PROJECT_NAME
```

3. Rodar servidor dev localmente
```
$ python manage.py runserver
```

5. User insertion example
```
user : User0
passwor : user0123456
```

6. Criar adm
```
$ python manage.py createsuperuser
```

7. Criação do banco usando sqlite3
```
$ python manage.py migrate
```

8. Desativação do sistema de debug para deploy
No arquivo settings.py dentro do diretório do projeto :
  1. Mudar o status da variável debug para 'False'
  2. Adicionar os hosts permitidos na lista de ALLOWED_HOSTS. Usar um '.' como 
  wildcard no começo do domínio já atende ao domínio e subdomínios. Ex :
    '.example.com' ao invés de 'www.example.com'

9. Mudar pacote de linguagem padrão da aplicação
No arquivo settings.py, mudar a variável LANGUAGE_CODE para a língua desejada. Ex :
-> pt-br : Português-Brasil
-> en-us : English (United States)


## Ref

BD : https://docs.djangoproject.com/en/2.1/ref/settings/#databases

BD-test : https://docs.djangoproject.com/en/2.1/topics/testing/overview/#the-test-database

Tradução : https://docs.djangoproject.com/en/2.1/topics/i18n/


## Pesquisa

Geradores de gráficos :
> https://github.com/matthisk/django-jchart

> https://github.com/areski/django-nvd3

> https://github.com/wq/django-rest-pandas
