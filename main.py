import tkinter as tk
#import pandas as pd


# Classe Base
class ItemBiblioteca:
    def __init__(self, titulo):
        self.titulo = titulo


# Classe Livro (Herda de ItemBiblioteca)
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo)
        self.autor = autor
        self.isbn = isbn


# Classe Usuario (Herda de ItemBiblioteca)
class Usuario(ItemBiblioteca):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []


    def adicionar_livro(self, livro):
        self.livros.append(livro)


    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)


# Classe GerenciadorDePedidos
class GerenciadorDePedidos:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.pedidos = []


    def solicitar_livro(self, usuario, livro):
        if livro in self.biblioteca.livros:
            self.pedidos.append((usuario, livro))
            return True
        return False


# Interface Gráfica
class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.biblioteca = Biblioteca()


        self.main_frame = tk.Frame(root)
        self.main_frame.pack()


        # Tela de Cadastro de Livros
        self.cadastro_livro_button = tk.Button(self.main_frame, text="Cadastrar Livro", command=self.cadastro_livro)
        self.cadastro_livro_button.pack()


        # Tela de Cadastro de Usuários
        self.cadastro_usuario_button = tk.Button(self.main_frame, text="Cadastrar Usuário", command=self.cadastro_usuario)
        self.cadastro_usuario_button.pack()


        # Tela de Visualização de Livros
        self.visualizar_livros_button = tk.Button(self.main_frame, text="Visualizar Livros", command=self.visualizar_livros)
        self.visualizar_livros_button.pack()


        # Tela de Visualização de Usuários
        self.visualizar_usuarios_button = tk.Button(self.main_frame, text="Visualizar Usuários", command=self.visualizar_usuarios)
        self.visualizar_usuarios_button.pack()


    def cadastro_livro(self):
        self.main_frame.pack_forget()
        cadastro_livro_frame = tk.Frame(self.root)
        cadastro_livro_frame.pack()


        # Campos para cadastro de livro
        titulo_label = tk.Label(cadastro_livro_frame, text="Título:")
        titulo_label.pack()
        titulo_entry = tk.Entry(cadastro_livro_frame)
        titulo_entry.pack()


        autor_label = tk.Label(cadastro_livro_frame, text="Autor:")
        autor_label.pack()
        autor_entry = tk.Entry(cadastro_livro_frame)
        autor_entry.pack()


        isbn_label = tk.Label(cadastro_livro_frame, text="ISBN:")
        isbn_label.pack()
        isbn_entry = tk.Entry(cadastro_livro_frame)
        isbn_entry.pack()


        def salvar_livro():
            titulo = titulo_entry.get()
            autor = autor_entry.get()
            isbn = isbn_entry.get()
            novo_livro = Livro(titulo, autor, isbn)
            self.biblioteca.adicionar_livro(novo_livro)
            cadastro_livro_frame.pack_forget()
            self.main_frame.pack()


        salvar_button = tk.Button(cadastro_livro_frame, text="Salvar", command=salvar_livro)
        salvar_button.pack()


        voltar_button = tk.Button(cadastro_livro_frame, text="Voltar", command=lambda: self.voltar(cadastro_livro_frame))
        voltar_button.pack()


    def cadastro_usuario(self):
        self.main_frame.pack_forget()
        cadastro_usuario_frame = tk.Frame(self.root)
        cadastro_usuario_frame.pack()


        # Campos para cadastro de usuário
        nome_label = tk.Label(cadastro_usuario_frame, text="Nome:")
        nome_label.pack()
        nome_entry = tk.Entry(cadastro_usuario_frame)
        nome_entry.pack()


        matricula_label = tk.Label(cadastro_usuario_frame, text="Matrícula:")
        matricula_label.pack()
        matricula_entry = tk.Entry(cadastro_usuario_frame)
        matricula_entry.pack()


        def salvar_usuario():
            nome = nome_entry.get()
            matricula = matricula_entry.get()
            novo_usuario = Usuario(nome, matricula)
            self.biblioteca.adicionar_usuario(novo_usuario)
            cadastro_usuario_frame.pack_forget()
            self.main_frame.pack()


        salvar_button = tk.Button(cadastro_usuario_frame, text="Salvar", command=salvar_usuario)
        salvar_button.pack()


        voltar_button = tk.Button(cadastro_usuario_frame, text="Voltar", command=lambda: self.voltar(cadastro_usuario_frame))
        voltar_button.pack()


    def visualizar_livros(self):
        self.main_frame.pack_forget()
        visualizar_livros_frame = tk.Frame(self.root)
        visualizar_livros_frame.pack()


        for livro in self.biblioteca.livros:
            livro_label = tk.Label(visualizar_livros_frame, text=f"Título: {livro.titulo}, Autor: {livro.autor}, ISBN: {livro.isbn}")
            livro_label.pack()


        voltar_button = tk.Button(visualizar_livros_frame, text="Voltar", command=lambda: self.voltar(visualizar_livros_frame))
        voltar_button.pack()


    def visualizar_usuarios(self):
        self.main_frame.pack_forget()
        visualizar_usuarios_frame = tk.Frame(self.root)
        visualizar_usuarios_frame.pack()


        for usuario in self.biblioteca.usuarios:
            usuario_label = tk.Label(visualizar_usuarios_frame, text=f"Nome: {usuario.titulo}, Matrícula: {usuario.matricula}")
            usuario_label.pack()


        voltar_button = tk.Button(visualizar_usuarios_frame, text="Voltar", command=lambda: self.voltar(visualizar_usuarios_frame))
        voltar_button.pack()


    def voltar(self, frame):
        frame.pack_forget()
        self.main_frame.pack()


# Inicializando o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()