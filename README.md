---
marp: true
_class: lead
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
---

# Django
## The web framework for perfectionists with deadlines.
---
## Django
* [Github](https://github.com/django)
* [Documentação](https://docs.djangoproject.com/pt-br/3.2/)
* [Code of Conduct](https://www.djangoproject.com/conduct/)
* [Instalação via PIP]((https://docs.djangoproject.com/pt-br/3.2/intro/install/))
~~~python
pip install django
~~~

---
### [startproject](https://docs.djangoproject.com/pt-br/3.2/intro/tutorial01/)
* Nota sobre ambiguidade:
    Evitar dar nomes a projetos que remetam a componentes internos do Python ou do Django. 
    Particularmente, isso significa que deve evitar usar nomes como django (que irá conflitar com o próprio Django) ou test (que irá conflitar com um pacote interno do Python).

---

#### Começando o projeto
~~~python
django-admin startproject mysite
~~~
##### Resultado esperado:
mysite/
* manage.py
* mysite/
    * __ init __.py
    * settings .py
    * urls .py
    * asgi .py
    * wsgi .py
---

* O servidor de desenvolvimento
~~~python
python mysite/manage.py runserver
~~~

---
## [Banco de dados](https://docs.djangoproject.com/pt-br/3.2/topics/install/#database-installation)
[Principais:](https://docs.djangoproject.com/pt-br/3.2/ref/databases/)
* PostgreSQL: [psycopg](https://www.psycopg.org/)
* MySQL ou MariaDB
* SQLite
* Oracle: [cx_Oracle](https://oracle.github.io/python-cx_Oracle/)
