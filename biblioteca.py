"""
Sistema de gerenciamento da biblioteca.
"""
from typing import List, Optional
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo

class Biblioteca:
    """
    Classe principal para gerenciar a biblioteca.
    
    Responsável por gerenciar livros, usuários e empréstimos.
    """
    
    def __init__(self):
        """Inicializa a biblioteca com listas vazias."""
        self.livros: List[Livro] = []
        self.usuarios: List[Usuario] = []
        self.emprestimos: List[Emprestimo] = []
    
    # ==================== GERENCIAMENTO DE LIVROS ====================
    
    def cadastrar_livro(self, titulo: str, autor: str, ano: int) -> Livro:
        """
        Cadastra um novo livro na biblioteca.
        
        Args:
            titulo: Título do livro
            autor: Autor do livro
            ano: Ano de publicação
            
        Returns:
            Livro: O livro cadastrado
        """
        livro = Livro(titulo, autor, ano)
        self.livros.append(livro)
        return livro
    
    def listar_livros(self) -> List[Livro]:
        """
        Lista todos os livros cadastrados.
        
        Returns:
            List[Livro]: Lista de todos os livros
        """
        return self.livros.copy()
    
    def buscar_livro_por_titulo(self, titulo: str) -> Optional[Livro]:
        """
        Busca um livro pelo título.
        
        Args:
            titulo: Título do livro a buscar
            
        Returns:
            Optional[Livro]: O livro encontrado ou None
        """
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
    
    def editar_livro(self, livro: Livro, titulo: str = None, autor: str = None, ano: int = None) -> bool:
        """
        Edita informações de um livro.
        
        Args:
            livro: Livro a ser editado
            titulo: Novo título (opcional)
            autor: Novo autor (opcional)
            ano: Novo ano (opcional)
            
        Returns:
            bool: True se o livro foi editado, False caso contrário
        """
        if livro not in self.livros:
            return False
        
        if titulo is not None:
            livro.titulo = titulo
        if autor is not None:
            livro.autor = autor
        if ano is not None:
            livro.ano = ano
        
        return True
    
    def remover_livro(self, livro: Livro) -> bool:
        """
        Remove um livro da biblioteca.
        
        Args:
            livro: Livro a ser removido
            
        Returns:
            bool: True se o livro foi removido, False caso contrário
        """
        # Verifica se o livro está emprestado
        if not livro.disponivel:
            return False
        
        if livro in self.livros:
            self.livros.remove(livro)
            return True
        return False
    
    # ==================== GERENCIAMENTO DE USUÁRIOS ====================
    
    def cadastrar_usuario(self, nome: str, matricula: str) -> Usuario:
        """
        Cadastra um novo usuário na biblioteca.
        
        Args:
            nome: Nome do usuário
            matricula: Matrícula do usuário
            
        Returns:
            Usuario: O usuário cadastrado
            
        Raises:
            ValueError: Se já existe um usuário com a mesma matrícula
        """
        # Verifica se já existe usuário com a mesma matrícula
        if self.buscar_usuario_por_matricula(matricula):
            raise ValueError(f"Já existe um usuário com a matrícula {matricula}")
        
        usuario = Usuario(nome, matricula)
        self.usuarios.append(usuario)
        return usuario
    
    def listar_usuarios(self) -> List[Usuario]:
        """
        Lista todos os usuários cadastrados.
        
        Returns:
            List[Usuario]: Lista de todos os usuários
        """
        return self.usuarios.copy()
    
    def buscar_usuario_por_matricula(self, matricula: str) -> Optional[Usuario]:
        """
        Busca um usuário pela matrícula.
        
        Args:
            matricula: Matrícula do usuário a buscar
            
        Returns:
            Optional[Usuario]: O usuário encontrado ou None
        """
        for usuario in self.usuarios:
            if usuario.matricula == matricula:
                return usuario
        return None
    
    # ==================== GERENCIAMENTO DE EMPRÉSTIMOS ====================
    
    def realizar_emprestimo(self, livro: Livro, usuario: Usuario, prazo_dias: int = Emprestimo.PRAZO_PADRAO) -> Emprestimo:
        """
        Realiza o empréstimo de um livro para um usuário.
        
        Args:
            livro: Livro a ser emprestado
            usuario: Usuário que está pegando o livro
            prazo_dias: Prazo em dias para devolução
            
        Returns:
            Emprestimo: O empréstimo realizado
            
        Raises:
            ValueError: Se o livro não estiver disponível
        """
        if not livro.disponivel:
            raise ValueError("Livro não está disponível para empréstimo")
        
        livro.emprestar()
        emprestimo = Emprestimo(livro, usuario, prazo_dias)
        self.emprestimos.append(emprestimo)
        return emprestimo
    
    def devolver_livro(self, livro: Livro) -> bool:
        """
        Realiza a devolução de um livro.
        
        Args:
            livro: Livro a ser devolvido
            
        Returns:
            bool: True se a devolução foi realizada, False caso contrário
        """
        # Busca o empréstimo ativo do livro
        for emprestimo in self.emprestimos:
            if emprestimo.livro == livro and emprestimo.esta_ativo():
                emprestimo.devolver()
                return True
        return False
    
    def listar_emprestimos_ativos(self) -> List[Emprestimo]:
        """
        Lista todos os empréstimos ativos (não devolvidos).
        
        Returns:
            List[Emprestimo]: Lista de empréstimos ativos
        """
        return [emp for emp in self.emprestimos if emp.esta_ativo()]
    
    def listar_emprestimos_por_usuario(self, usuario: Usuario) -> List[Emprestimo]:
        """
        Lista todos os empréstimos de um usuário específico.
        
        Args:
            usuario: Usuário para buscar os empréstimos
            
        Returns:
            List[Emprestimo]: Lista de empréstimos do usuário
        """
        return [emp for emp in self.emprestimos if emp.usuario == usuario]
    
    def listar_emprestimos_ativos_por_usuario(self, usuario: Usuario) -> List[Emprestimo]:
        """
        Lista os empréstimos ativos de um usuário específico.
        
        Args:
            usuario: Usuário para buscar os empréstimos
            
        Returns:
            List[Emprestimo]: Lista de empréstimos ativos do usuário
        """
        return [emp for emp in self.emprestimos if emp.usuario == usuario and emp.esta_ativo()]
    
    def listar_historico_emprestimos(self, usuario: Usuario) -> List[Emprestimo]:
        """
        Lista o histórico completo de empréstimos de um usuário.
        
        Args:
            usuario: Usuário para buscar o histórico
            
        Returns:
            List[Emprestimo]: Lista de todos os empréstimos do usuário (ativos e finalizados)
        """
        return self.listar_emprestimos_por_usuario(usuario)
    
    def listar_emprestimos_atrasados(self) -> List[Emprestimo]:
        """
        Lista todos os empréstimos atrasados.
        
        Returns:
            List[Emprestimo]: Lista de empréstimos atrasados
        """
        return [emp for emp in self.emprestimos if emp.esta_atrasado()]
