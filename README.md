# Introduction 
Az isdc demo site backendje. Az alábbi db-ket támogatja:
Django officially supports the following databases:

PostgreSQL
MariaDB
MySQL
Oracle
SQLite

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)

See here : http://django.isdckft.com 
docker build -t isdckft/isdcbackend . 
#docker run -p 8000:8000 isdckft/isdcbackend
docker run -i -t isdckft/isdcbackend sh

# Django felépítés
python3 manage.py makemigrations isdcbackend
python3 manage.py makemigrations accounts
python3 manage.py makemigrations webpages
# DB migrálás
python manage.py migrate 