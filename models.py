from database import db

class Categorias(db.Model):
    __tablename__= "categorias"
    id_categoria = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(200))
    codigo = db.Column(db.String(30))

    # construtor
    def __init__(self, nome, descricao, codigo):
        self.nome = nome
        self.descricao = descricao
        self.codigo = codigo

    # representação do objeto criado...
    def __repr__(self):
        return "<Categoria: {}>".format(self.nome)