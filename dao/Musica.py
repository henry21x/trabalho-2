class Musica:
    def __init__(self, nome: str, album: str, ano: str, artista: str, genero: str, id: int = None) -> None:
        self.__id = id
        self.__nome = nome
        self.__album = album
        self.__ano = ano
        self.__artista = artista
        self.__genero = genero
        
    def setNome(self, x: str) -> dict:
        self.__nome = x

    def getNome(self) -> str:
        return self.__nome

    def setAno(self, m: str) -> dict:
        self.__ano = m

    def getAno(self) -> str:
        return self.__ano

    def setAlbum(self, y: str) -> dict:
        self.__album = y

    def getAlbum(self) -> str:
        return self.__album

    def setArtista(self, n: str) -> dict:
        self.__artista = n

    def getArtista(self) -> str:
        return self.__artista

    def setGenero(self, z: str) -> dict:
        self.__genero = z

    def getGenero(self) -> str:
        return self.__genero

    def setId(self, d: int) -> dict:
        self.__id = d

    def getId(self) -> int:
        return self.__id
