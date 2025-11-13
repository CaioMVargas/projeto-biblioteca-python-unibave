"""
Classe que representa um Livro no sistema de biblioteca.
"""

class Livro:
    """
    Representa um livro na biblioteca.
    
    Atributos:
        titulo (str): Título do livro
        autor (str): Autor do livro
        ano (int): Ano de publicação
        disponivel (bool): Indica se o livro está disponível para empréstimo
    """
    
    def __init__(self, titulo, autor, ano):
        """
        Inicializa um novo livro.
        
        Args:
            titulo: Título do livro
            autor: Autor do livro
            ano: Ano de publicação
        """
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
