from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Categorias

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

# --> drive://usuario:senha@servidor/banco_de_dados

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/DbGio"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/categoria")
def categoria():
    c = Categorias.query.all()
    return render_template("categoria_lista.html", dados = c)

@app.route("/categoria/add")
def categoria_add():
    return render_template("categoria_add.html")

@app.route("/categoria/save", methods=['POST'])
def categoria_save():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    codigo = request.form.get('codigo')
    if nome and descricao and codigo:
        categoria = Categorias(nome, descricao, codigo)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria de Produto cadastrada com sucesso! XD')
        return redirect('/categoria')
    else:
        flash('Preencha todos os campos! >=P')
        return redirect('/categoria/add')

@app.route("/categoria/remove/<int:id_categoria>")
def categoria_remove(id_categoria):
    categoria = Categorias.query.get(id_categoria)
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
        flash('Categoria removida com sucesso!')
        return redirect("/categoria")
    else:
        flash("Caminho incorreto!")
        return redirect("/categoria")


@app.route("/categoria/edita/<int:id_categoria>")
def categoria_edita(id_categoria):
    categoria = Categorias.query.get(id_categoria)
    return render_template("categoria_edita.html", dados=categoria)

@app.route("/categoria/editasave", methods=['POST'])
def categoria_editasave():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    codigo = request.form.get('codigo')
    id_categoria = request.form.get('id_categoria')
    if id_categoria and nome and descricao and codigo:
        categoria = Categorias.query.get(id_categoria)
        categoria.nome = nome
        categoria.descricao = descricao
        categoria.codigo = codigo
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/categoria')
    else:
        flash('Dados incompletos.')
        return redirect("/categoria")


if __name__ == '__main__':
    app.run()