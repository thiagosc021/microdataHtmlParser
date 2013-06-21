microdataHtmlParser
===================

Command python que importa dados estruturados de uma página html para o banco de dados.

Para tal foram utilizadas as seguintes bibliotecas:
     html5lib:https://github.com/html5lib/html5lib-python
     lxml:http://lxml.de/index.html
     https://github.com/edsu/microdata
     
App Django utilizada para acesso aos dados importados.

O banco de dados utlizado foi o sqLite e o arquivo do banco encontra-se na raiz do projeto django(django-app) com o nome database.
 
Como utilizar o importador:
  python techtudoHtmlToDBparser.py
  
Como utilizar a ferramenta administrativa
  acessa a pasta django-app
  execute o comando: python manage.py runserver
  acesse a url:http://localhost:8000/admin
          usuário:admin
          senha:admin
    


