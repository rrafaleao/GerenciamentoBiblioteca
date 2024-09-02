# Sistema de Gerenciamento de Biblioteca

## Visão Geral
O projeto é feito em python e tem como principal função simular o sistema de gerenciamento de uma biblioteca. Com as funções de adicionar livros e usuarios e visualiza-los. O programa tem uma interface 
simples, mas muito intuitiva e eficaz.

## Manual de instalação/compilação

Certifique-se de ter o python instalado no seu computador, ou instale através desse link: [Instalação Python](https://python.org.br/instalacao-windows/)

1.  Com o python instalado, clone este repositorio no seu Visual Studio Code

imagem Clona repositorio
**

2.  Execute ele pelo terminal digitando "python nomedoprograma.py", Por exemplo:
```
python biblioteca.py
```
## Guia do usuario

### Tela Inicial
Com o programa ja aberto, a tela principal é aberta com quatro opções, Cadastrar Livro, Cadastrar Usuario, Visualizar Livros e Visualizar Usuarios.

![TelaPrincipal](image.png)

### Cadastrar Livro
Para cadastrar um livro é necessario apenas digitar o titulo do livro que deseja adicionar, o nome do autor do livro e o ISBN, que é um código numérico que serve para identificar publicações monográficas, como livros, artigos e apostilas. Com as informações preenchidas clique em adicionar
![alt text](image-3.png)

### Cadastrar Usuario
Para cadastrar um usuario é preciso preencher as informações, nome e matricula. Depois clique em adicionar

![alt text](image-4.png)

### Visualizar Livros
A aba de visualizar livros, vai mostrar todos os livros que você adicionou. 

![alt text](image-5.png)

### Visualizar Usuarios
Aqui vai mostrar todos os usuarios cadastrados, e seus respectivos numeros de matricula.

![alt text](image-6.png)



## Codigo Explicado
Diagrama UML de como funciona o programa:  

![image](https://github.com/user-attachments/assets/1497373b-884a-49ca-9162-27f99348ff57)

### Classes

#### Item Biblioteca
Aqui é definida a classe mãe, e o seu metodo construtor que é responsavel por criar o atributo titulo.
```
class ItemBiblioteca:
    def __init__(self, titulo):
        self.titulo = titulo
```

#### Livro e Usuario
Então sao criadas as classes filhas da classe mãe, Livro e Usuario, elas herdam da classe ItemBiblioteca. Cada uma tem seus respectivos atributos e é utilizada a função super(), para dar acesso a classe mãe.
```
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo)
        self.autor = autor
        self.isbn = isbn

class Usuario(ItemBiblioteca):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
```
Aqui é criada a classe biblioteca, que vai armazenar os livros e usuarios em uma lista e também vai fazer as funções principais do programa, adicionar livro e adicionar usuario, ele faz isso pegando as variaveis que o usuario digitou, passa para a função e passa para a lista. 

```
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []


    def adicionar_livro(self, livro):
        self.livros.append(livro)


    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
```
A classe gerenciador de pedidos é definida com o atributo biblioteca e a lista pedidos, e é declarada também a função solicitar livro que checa os livros na biblioteca e se tiver algo ele envia para a lista pedidos o usuario e o livro. Apesar disso, a função não é utilizada na interface grafica, se tornando inutil no codigo.
```
class GerenciadorDePedidos:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.pedidos = []

    def solicitar_livro(self, usuario, livro):
        if livro in self.biblioteca.livros:
            self.pedidos.append((usuario, livro))
            return True
        return False
```
E por fim, a classe BibliotecaApp, que é onde toda a interface visual é feita. Aqui todas as telas são criadas e feitas utilizando a logica do programa feita acima.
```
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
```
