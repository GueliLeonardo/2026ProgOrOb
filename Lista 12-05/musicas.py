class PlayList:
    def __init__(self, i: int, n: str, d: str):
        self.id = i
        self.nome = n
        self.descricao = d

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao

    def set_nome(self, nome):
        self.nome = nome

    def set_descricao(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao}"


class Musica:
    def __init__(self, i: int, t: str, art: str, alb: str):
        self.id = i
        self.titulo = t
        self.artista = art
        self.album = alb

    def get_id(self):
        return self.id

    def get_titulo(self):
        return self.titulo

    def get_artista(self):
        return self.artista

    def get_album(self):
        return self.album

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_artista(self, artista):
        self.artista = artista

    def set_album(self, album):
        self.album = album

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Artista: {self.artista} | Álbum: {self.album}"


class PlayListItem:
    def __init__(self, i: int, ip: int, im: int, s: int):
        self.id = i
        self.idPlayList = ip
        self.idMusica = im
        self.sequencia = s

    def get_id(self):
        return self.id

    def get_idPlayList(self):
        return self.idPlayList

    def get_idMusica(self):
        return self.idMusica

    def get_sequencia(self):
        return self.sequencia

    def set_idPlayList(self, idPlayList):
        self.idPlayList = idPlayList

    def set_idMusica(self, idMusica):
        self.idMusica = idMusica

    def set_sequencia(self, sequencia):
        self.sequencia = sequencia

    def __str__(self):
        return f"ID: {self.id} | Playlist: {self.idPlayList} | Música: {self.idMusica} | Sequência: {self.sequencia}"


class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []

    def inserir_playlist(self):
        i = int(input("ID da playlist: "))
        n = input("Nome da playlist: ")
        d = input("Descrição: ")

        playlist = PlayList(i, n, d)
        self.playlists.append(playlist)

        print("Playlist cadastrada!\n")

    def listar_playlist(self):
        if len(self.playlists) == 0:
            print("Nenhuma playlist cadastrada.\n")
        else:
            for p in self.playlists:
                print(p)
            print()

    def atualizar_playlist(self):
        i = int(input("ID da playlist: "))

        for p in self.playlists:
            if p.get_id() == i:
                novo_nome = input("Novo nome: ")
                nova_descricao = input("Nova descrição: ")

                p.set_nome(novo_nome)
                p.set_descricao(nova_descricao)

                print("Playlist atualizada!\n")
                return

        print("Playlist não encontrada.\n")

    def excluir_playlist(self):
        i = int(input("ID da playlist: "))

        for p in self.playlists:
            if p.get_id() == i:
                self.playlists.remove(p)

                self.itens = [
                    item for item in self.itens
                    if item.get_idPlayList() != i
                ]

                print("Playlist removida!\n")
                return

        print("Playlist não encontrada.\n")

    def inserir_musica(self):
        i = int(input("ID da música: "))
        t = input("Título: ")
        art = input("Artista: ")
        alb = input("Álbum: ")

        musica = Musica(i, t, art, alb)
        self.musicas.append(musica)

        print("Música cadastrada!\n")

    def listar_musica(self):
        if len(self.musicas) == 0:
            print("Nenhuma música cadastrada.\n")
        else:
            for m in self.musicas:
                print(m)
            print()

    def atualizar_musica(self):
        i = int(input("ID da música: "))

        for m in self.musicas:
            if m.get_id() == i:
                novo_titulo = input("Novo título: ")
                novo_artista = input("Novo artista: ")
                novo_album = input("Novo álbum: ")

                m.set_titulo(novo_titulo)
                m.set_artista(novo_artista)
                m.set_album(novo_album)

                print("Música atualizada!\n")
                return

        print("Música não encontrada.\n")

    def excluir_musica(self):
        i = int(input("ID da música: "))

        for m in self.musicas:
            if m.get_id() == i:
                self.musicas.remove(m)

                self.itens = [
                    item for item in self.itens
                    if item.get_idMusica() != i
                ]

                print("Música removida!\n")
                return

        print("Música não encontrada.\n")

    def inserir_item(self):
        i = int(input("ID do item: "))
        ip = int(input("ID da playlist: "))
        im = int(input("ID da música: "))
        s = int(input("Sequência: "))

        playlist_existe = False
        musica_existe = False

        for p in self.playlists:
            if p.get_id() == ip:
                playlist_existe = True

        for m in self.musicas:
            if m.get_id() == im:
                musica_existe = True

        if not playlist_existe:
            print("Playlist não encontrada.\n")
            return

        if not musica_existe:
            print("Música não encontrada.\n")
            return

        item = PlayListItem(i, ip, im, s)
        self.itens.append(item)

        print("Item cadastrado!\n")

    def listar_item(self):
        if len(self.itens) == 0:
            print("Nenhum item cadastrado.\n")
        else:
            for item in self.itens:
                print(item)
            print()

    def atualizar_item(self):
        i = int(input("ID do item: "))

        for item in self.itens:
            if item.get_id() == i:
                nova_seq = int(input("Nova sequência: "))
                item.set_sequencia(nova_seq)

                print("Item atualizado!\n")
                return

        print("Item não encontrado.\n")

    def excluir_item(self):
        i = int(input("ID do item: "))

        for item in self.itens:
            if item.get_id() == i:
                self.itens.remove(item)

                print("Item removido!\n")
                return

        print("Item não encontrado.\n")

    def listar_musicas_playlist(self):
        ip = int(input("ID da playlist: "))

        encontrou = False

        for item in self.itens:
            if item.get_idPlayList() == ip:
                for musica in self.musicas:
                    if musica.get_id() == item.get_idMusica():
                        print(
                            f"Sequência: {item.get_sequencia()} | {musica}"
                        )
                        encontrou = True

        if not encontrou:
            print("Nenhuma música encontrada nessa playlist.\n")

    def main(self):
        while True:
            print("===== MENU =====")
            print("1 - Inserir playlist")
            print("2 - Listar playlists")
            print("3 - Atualizar playlist")
            print("4 - Excluir playlist")
            print("5 - Inserir música")
            print("6 - Listar músicas")
            print("7 - Atualizar música")
            print("8 - Excluir música")
            print("9 - Inserir item")
            print("10 - Listar itens")
            print("11 - Atualizar item")
            print("12 - Excluir item")
            print("13 - Listar músicas da playlist")
            print("0 - Sair")

            op = int(input("Escolha: "))
            print()

            if op == 1:
                self.inserir_playlist()

            elif op == 2:
                self.listar_playlist()

            elif op == 3:
                self.atualizar_playlist()

            elif op == 4:
                self.excluir_playlist()

            elif op == 5:
                self.inserir_musica()

            elif op == 6:
                self.listar_musica()

            elif op == 7:
                self.atualizar_musica()

            elif op == 8:
                self.excluir_musica()

            elif op == 9:
                self.inserir_item()

            elif op == 10:
                self.listar_item()

            elif op == 11:
                self.atualizar_item()

            elif op == 12:
                self.excluir_item()

            elif op == 13:
                self.listar_musicas_playlist()

            elif op == 0:
                print("Saindo..")
                break

            else:
                print("Opção inválida!\n")


ui = UI()
ui.main()