from ..extensions import db

class Livro(db.Model):
    __tablename__ = "livros"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    vinculo = db.Column(db.String(50))
    emprestimo = db.Column(db.Date)
    devolucao = db.Column(db.Date)

    def __repr__(self):
        return "<Livro(titulo={}, nome={}, vinculo={}, emprestimo={}, devolucao={})>".format(self.titulo, self.nome, self.vinculo, self.emprestimo, self.devolucao)