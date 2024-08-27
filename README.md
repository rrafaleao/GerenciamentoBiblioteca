# GerenciamentoBiblioteca

# Sistema de Gerenciamento de Biblioteca

## Visão Geral
O projeto é feito em python e tem como principal função simular o sistema de gerenciamento de uma biblioteca. Com as funções de adicionar livros e usuarios e visualiza-los. O programa tem uma interface simples, mas muito intuitiva e eficaz.

## Como executar
Certifique que todas as extensões do programa python estejam instaladas no Visual Studio Code.  

Clone esse repositorio do github no Vscode com o o seguinte codigo:
```
git clone (link do repositorio 
```

Depois disso, Para executar é só digitar:

```
python.exe ./nomedoarquivo
```

## Como usar

## Codigo Explicado

Primeiro é criada a classe Item Biblioteca que é a classe base, que tem o atributo titulo. Depois, as subclasses são criadas, livro, que tem os atributos titulo, autor e isbn. E a subclasse usuario que tem os atributos nome e matricula.
Nos atributos "nome" e "titulo" é utilizado o super() que faz com que
