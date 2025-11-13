"""
Classe que representa um Usuário no sistema de biblioteca.
"""

class Usuario:
    """
    Representa um usuário da biblioteca.
    
    Atributos:
        nome (str): Nome do usuário
        matricula (str): Matrícula do usuário
    """
    
    def __init__(self, nome, matricula):
        """
        Inicializa um novo usuário.
        
        Args:
            nome: Nome do usuário
            matricula: Matrícula do usuário
        """
        self.nome = nome
        self.matricula = matricula
