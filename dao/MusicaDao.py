import json
from random import random
from dao.Musica import Musica


class MusicaDao:
    def __init__(self, filename: str = "data.json") -> None:
        self.__filename = filename   


    def __loadFile(self) -> list:
        # self.x =__filename
        file = open(self.__filename, "r", encoding='utf-8')
        data = file.read()
        return json.loads(data)
    
    def __saveFile(self, data: list):
        newData = []
        for x in data:
            n = {}
            for chave, valor in x.__dict__.items():
                chave = chave.replace('_Musica__', '')
                n[chave] = valor
            
            newData.append(n)

        
        file = open(self.__filename, "w+", encoding='utf-8')
        data = json.dumps(newData)
        file.write(data)
        file.close()

    def adicionar(self, musica: Musica) -> Musica:
        data = self.selecionarTodos()
        musica.setId(int(round(random() * 10000, 0)))
        data.append(musica)
        self.__saveFile(data)

        return musica

    def editar(self, m: Musica) -> None:
        data = self.selecionarTodos()

        for x in data:
            if x.getId() == m.getId():
                data.remove(x)
                m.setId(m.getId())
                data.append(m)
                self.__saveFile(data)
                break


    def deletar(self, id: int) -> None:
        data = self.selecionarTodos()
        for x in data:
            if x.getId() == id:
                data.remove(x)
                break
        self.__saveFile(data)

    def selecionar(self, id: int) -> Musica:
        data = self.__loadFile()
        for d in data:
            if d['id'] == id:
                return Musica(d['nome'], d['album'], d['ano'], d['artista'], d['genero'], d['id'])
        return None

    def selecionarTodos(self) -> list:
        data = self.__loadFile()
        musicas = []
        for d in data:
            m = Musica(d['nome'], d['album'], d['ano'], d['artista'], d['genero'], d['id'] )
            musicas.append(m)
        return musicas

      