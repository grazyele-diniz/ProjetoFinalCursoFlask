from ..extensions import db

class Livro(db.Model):
    __tablename__ = "livros"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150))
    vinculo = db.Column(db.String(50))
    emprestimo = db.Column(db.Date)
    devolucao = db.Column(db.Date)

    def __repr__(self):
        return "<Livro(titulo={}, vinculo={}, emprestimo={}, devolucao={})>".format(self.titulo, self.vinculo, self.emprestimo, self.devolucao)