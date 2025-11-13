"""
Classe que representa um Empréstimo no sistema de biblioteca.
"""
from datetime import datetime

class Emprestimo:
    """
    Representa um empréstimo de livro.
    
    Atributos:
        livro: Livro emprestado
        usuario: Usuário que pegou o livro emprestado
        data_emprestimo: Data em que o empréstimo foi realizado
        data_devolucao: Data em que o livro foi devolvido (None se ainda não foi devolvido)
    """
    
    def __init__(self, livro, usuario):
        """
        Inicializa um novo empréstimo.
        
        Args:
            livro: Livro a ser emprestado
            usuario: Usuário que está pegando o livro
        """
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
