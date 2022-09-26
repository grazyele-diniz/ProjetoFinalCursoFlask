# Importando o Blueprint
from turtle import st
from flask import Blueprint, render_template, request, session, redirect, url_for
from ..extensions import db
from ..models.livro import Livro
from datetime import date, datetime

#Instanciar o blueprint
#livroBp = Blueprint('livroBp', __name__)
livroBp = Blueprint('livroBp', __name__)

#criar a página de login inicial
@livroBp.route('/')
def login_livro():
    return render_template('livro_login.html')

@livroBp.route('/livro')
def livro_list():
    #db.create_all()

    livros_query = Livro.query.all()
    return render_template('livro_list.html', livros=livros_query)

@livroBp.route('/livro/create')
def create_livro():
    return render_template('livro_create.html')

@livroBp.route('/livro/add', methods=["POST"])
def add_livro():

    sTitulo = request.form["titulo"]
    sVinculo = request.form["vinculo"]
    dEmprestimo = datetime.strptime(request.form["emprestimo"], '%Y-%m-%d')
    dDevolucao = datetime.strptime(request.form["devolucao"], '%Y-%m-%d')

    livro = Livro(titulo=sTitulo, vinculo=sVinculo, emprestimo=dEmprestimo, devolucao=dDevolucao)
    db.session.add(livro)
    db.session.commit()

    return redirect(url_for("livroBp.livro_list"))

#Chamar o formulário de alteração
@livroBp.route('/livro/update/<livro_id>')
def update_livro(livro_id=0):
    livro_query = Livro.query.filter_by(id = livro_id).first()
    return render_template('livro_update.html', livro=livro_query)

#Tratar o update (update no banco de dados)
@livroBp.route('/livro/upd', methods=["POST"])
def upd_livro():

    iLivro = request.form["id"]
    sTitulo = request.form["titulo"]
    sVinculo = request.form["vinculo"]
    dEmprestimo = datetime.strptime(request.form["emprestimo"], '%Y-%m-%d')
    dDevolucao = datetime.strptime(request.form["devolucao"], '%Y-%m-%d')

    livro = Livro.query.filter_by(id = iLivro).first()
    livro.titulo = sTitulo
    livro.vinculo = sVinculo
    livro.emprestimo = dEmprestimo
    livro.devolucao = dDevolucao
    db.session.add(livro)
    db.session.commit()

    return redirect(url_for("livroBp.livro_list"))

#Tratar o delete (tela de confirmação)
@livroBp.route('/livro/delete/<livro_id>')
def delete_livro(livro_id=0):
    livro_query = Livro.query.filter_by(id = livro_id).first()
    return render_template('livro_delete.html', livro=livro_query)
#Para apagar de fato
@livroBp.route('/livro/dlt', methods=["POST"])
def dlt_livro():

    iLivro = request.form["id"]
    livro = Livro.query.filter_by(id = iLivro).first()
    db.session.delete(livro)
    db.session.commit()

    return redirect(url_for("livroBp.livro_list"))