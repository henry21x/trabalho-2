from dao.Musica import Musica
from dao.MusicaDao import MusicaDao
from flask import redirect, render_template, request
from flask_classful import FlaskView, route

class MusicaView(FlaskView):
    dao = MusicaDao()
    route_base = '/'

    def index(self):
        return "<br>"

    @route('/alterar/<int:id>', methods=['POST'])
    @route('/cadastrar', methods=['POST'])
    def cadastrar(self, id: int = None):
        body = dict(request.form)
        m = Musica(body['nome'], body['album'], body['ano'],
                    body['artista'], body['genero'])
        if id:
            m.setId(id)
            self.dao.editar(m)
        else:
            self.dao.adicionar(m)
        return redirect("/listar")

    @route('/deletar/<int:id>', methods=['GET'])
    def deletar(self, id: int):
        self.dao.deletar(id)
        return redirect("/listar")

    @route('/cadastro/<int:id>', methods=['GET'])
    @route('/cadastro', methods=['GET'])
    def form(self, id: int = None):
        if id:
            return render_template("form.html", dados=self.dao.selecionar(id))

        return render_template("form.html")

    @route('/listar', methods=['GET'])
    def listar(self):
        return render_template("listar.html", lista=self.dao.selecionarTodos())
