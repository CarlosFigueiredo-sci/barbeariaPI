<h1 align="center"> BarbVesp </h1>
<div align="center">
<img alt="Static Badge" src="https://img.shields.io/badge/Projeto%20Barbearia%20PI%202-v.2-blue">
<img alt="Static Badge" src="https://img.shields.io/badge/Em%20produ%C3%A7%C3%A3o-yellow?logoColor=red">
</div>


## Instruções de execução (Localmente | Windows)
1. Baixe o projeto</h3>
> Pré requisitos: Instalar o python, que pode ser baixado [Aqui](https://www.python.org/downloads/)
* Crie um ambiente virtual </br>
~~~
 python -m venv myenv
~~~
* Instale o Django </br>
~~~
pip install django
~~~
* Ative o ambiente </br>
~~~
 myenv\Scripts\activate
~~~
--------------------------------
2. Navegue até a pasta do projeto
* Use este comando para rodar o servidor </br>
~~~
python manage.py runserver
~~~
* Endereço do site (ele aparecerá no terminal após rodar o servidor) </br>
`http://127.0.0.1:8000/`
* Endereço para administradores </br>
`http://127.0.0.1:8000/admin`
--------------------------------
3. Informações para administradores
> Ambiente administrativo; pode ser visualizados e criar novos agendamentos, criação e edição de serviços, criação e edição de usuários, assim como grupos. </br>
Como o projeto usa o banco de dados SQLite como padrão, no administrador é possível visualizá-lo. </br>
Para uso exclusivo dos desenvolvedores e membros do grupo.

