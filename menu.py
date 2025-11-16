"""
Interface de usuário para o sistema de biblioteca.
"""
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo

# ==================== LISTAS PRINCIPAIS ====================
# Armazenam os dados em memória durante a execução do programa
livros = []
usuarios = []
emprestimos = []


class Menu:
    """
    Classe responsável pela interface de usuário do sistema.
    """
    
    def __init__(self):
        """Inicializa o menu."""
        self.executando = True
    
    def limpar_tela(self):
        """Limpa a tela do console."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pausar(self):
        """Pausa a execução até o usuário pressionar Enter."""
        input("\nPressione ENTER para continuar...")
    
    def exibir_menu_principal(self):
        """Exibe o menu principal do sistema."""
        print("\n" + "="*50)
        print(" SISTEMA DE BIBLIOTECA ".center(50))
        print("="*50)
        print("\n[1] Gerenciar Livros")
        print("[2] Gerenciar Usuários")
        print("[3] Gerenciar Empréstimos")
        print("[4] Relatórios")
        print("[0] Sair")
        print("\n" + "="*50)
    
    def exibir_menu_livros(self):
        """Exibe o menu de gerenciamento de livros."""
        print("\n" + "="*50)
        print(" GERENCIAR LIVROS ".center(50))
        print("="*50)
        print("\n[1] Cadastrar novo livro")
        print("[2] Listar livros cadastrados")
        print("[3] Editar informações de um livro")
        print("[4] Remover livro")
        print("[0] Voltar")
        print("\n" + "="*50)
    
    def exibir_menu_usuarios(self):
        """Exibe o menu de gerenciamento de usuários."""
        print("\n" + "="*50)
        print(" GERENCIAR USUÁRIOS ".center(50))
        print("="*50)
        print("\n[1] Cadastrar novo usuário")
        print("[2] Listar usuários cadastrados")
        print("[0] Voltar")
        print("\n" + "="*50)
    
    def exibir_menu_emprestimos(self):
        """Exibe o menu de gerenciamento de empréstimos."""
        print("\n" + "="*50)
        print(" GERENCIAR EMPRÉSTIMOS ".center(50))
        print("="*50)
        print("\n[1] Realizar empréstimo")
        print("[2] Devolver livro")
        print("[3] Listar empréstimos ativos")
        print("[0] Voltar")
        print("\n" + "="*50)
    
    def exibir_menu_relatorios(self):
        """Exibe o menu de relatórios."""
        print("\n" + "="*50)
        print(" RELATÓRIOS ".center(50))
        print("="*50)
        print("\n[1] Livros emprestados por usuário")
        print("[2] Histórico de empréstimos de um usuário")
        print("[3] Empréstimos atrasados")
        print("[0] Voltar")
        print("\n" + "="*50)
    
    # ==================== FUNÇÕES DE LIVROS ====================
    
    def cadastrar_livro(self):
        """Cadastra um novo livro."""
        # TODO: Bruno - Implementar cadastro de livro
        # Criar objeto Livro e adicionar na lista livros
        print("\n--- CADASTRAR LIVRO ---")
        print("[Função a ser implementada pelo Bruno]")

        titulo = input("Título do livro: ")

        if not titulo:
            print("Título do livro é obrigatório")
            return

        for livro in livros:
            
            if livro.titulo.lower() == titulo.lower:
                print("Já existe um livro com este título!")
                return
        
        autor = input("Autor do livro: ")

        if not autor:
            print("Autor é obrigatório!")
            return
        
        ano = int(input("Ano de publicação: "))
        
        if ano < 0 or ano > 2025:
            print("Ano inválido!")
            return
        
        livro = Livro(titulo, autor, ano)
        livros.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
     
    def listar_livros(self):
        """Lista todos os livros cadastrados."""
        # TODO: Bruno - Implementar listagem de livros
        # Percorrer a lista livros e exibir cada livro
        print("\n--- LIVROS CADASTRADOS ---")
        print("[Função a ser implementada pelo Bruno]")

        if not livros:
            print("Nenhum livro cadastrado!")
            return
    
        print(f"{'Título':<30} {'Autor':<25} {'Ano':<6} {'Disponível':<10}")
        print("-" * 75)
    
        for i, livro in enumerate(livros, 1):
            status = "Sim" if livro.disponivel else "Não"
            print(f"{i:2}. {livro.titulo:<28} {livro.autor:<23} {livro.ano:<6} {status:<10}")
    
    def editar_livro(self):
        """Edita informações de um livro."""
        # TODO: Bruno - Implementar edição de livro
        # Buscar livro na lista e atualizar seus atributos
        print("\n--- EDITAR LIVRO ---")
        print("[Função a ser implementada pelo Bruno]")

        if not livros:
            print("Nenhum livro cadastrado para editar.")
            return
        
        #listar livros para escolher
        self.listar_livros()

        opcao = int((input("\nNúmero do livro a editar: ")))-1

        if opcao < 0 or opcao>=len(livros):
            print("Número inválido!")
            return
        
        livro = livros[opcao]
        print(f"\nEditando livro: {livro.titulo}\n")

        novoTitulo = input(f"Novo título: ").strip()
        novoAutor = input(f"Novo autor: ").strip()
        novoAno = input(f"Novo ano: ").strip()

        if novoTitulo:
            for l in livros:
                if l != livro and l.titulo.lower() == novoTitulo.lower():
                    print("Já existe outro livro com este título!")
                    return
            
            livro.titulo = novoTitulo

        if novoAutor:
            livro.autor = novoAutor

        if novoAno:
            ano = int(novoAno)
            if ano < 0 or ano > 2025:
                print("Ano inválido!")
                return
            livro.ano = ano

        print("Livro editado com sucesso!")
    
    def remover_livro(self):
        """Remove um livro."""
        # TODO: Bruno - Implementar remoção de livro
        # Verificar se o livro está disponível antes de remover
        print("\n--- REMOVER LIVRO ---")
        print("[Função a ser implementada pelo Bruno]")

        if not livros:
            print("não há livros cadastrados para remover.")
            return

        self.listar_livros()

        opcao = int(input("Número do livro a remover: "))-1

        if opcao < 0 or opcao >= len(livros):
            print("Número inválido!")
            return
        
        livro = livros[opcao]

        if not livro.disponivel:
            print("Não é possível remover um livro que está emprestado!")
            return
        
        confirmacao = input(f"Tem certeza que deseja remover '{livro.titulo}'? (s/n): ").strip().lower()

        if confirmacao == 's' or confirmacao == 'sim':
            livros.remove(livro)
            print("Livro removido com sucesso!")
        else:
            print("Remoção cancelada!")
    
    # ==================== FUNÇÕES DE USUÁRIOS ====================

#Cadastrar usuário    
def cadastrar_usuario(self):
    """Cadastra um novo usuário."""
    global usuarios

    print("\n--- CADASTRAR USUÁRIO ---")

    nome = input("Nome do usuário: ").strip()
    if not nome:
        print("O nome é obrigatório!")
        return

    matricula = input("Matrícula do usuário: ").strip()
    if not matricula:
        print("A matrícula é obrigatória!")
        return

    # Verificar matrícula duplicada
    for usuario in usuarios:
        if usuario.matricula == matricula:
            print("Já existe um usuário com essa matrícula!")
            return

    # Criar usuário
    novo_usuario = Usuario(nome, matricula)
    usuarios.append(novo_usuario)

    print(f"Usuário '{nome}' cadastrado com sucesso!")

    
def listar_usuarios(self):
    """Lista todos os usuários cadastrados."""
    global usuarios

    print("\n--- USUÁRIOS CADASTRADOS ---")

    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return

    print(f"{'N°':<4} {'Nome':<30} {'Matrícula':<15}")
    print("-" * 50)

    for i, usuario in enumerate(usuarios, 1):
        print(f"{i:<4} {usuario.nome:<30} {usuario.matricula:<15}")

def listar_emprestimos_por_usuario(self):
    """Lista livros emprestados por um usuário."""
    global usuarios, emprestimos

    print("\n--- LIVROS EMPRESTADOS POR USUÁRIO ---")

    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return

    # Listar usuários para escolher
    self.listar_usuarios()

    escolha = input("\nDigite o número do usuário: ").strip()
    if not escolha.isdigit():
        print("Opção inválida!")
        return

    index = int(escolha) - 1

    if index < 0 or index >= len(usuarios):
        print("Usuário inválido!")
        return

    usuario_escolhido = usuarios[index]

    # Filtrar empréstimos deste usuário
    emprestimos_usuario = [
        emp for emp in emprestimos
        if emp.usuario == usuario_escolhido and emp.data_devolucao is None
    ]

    print(f"\n--- Empréstimos ativos de {usuario_escolhido.nome} ---")

    if not emprestimos_usuario:
        print("Nenhum livro emprestado!")
        return

    print(f"{'Livro':<30} {'Data Empréstimo':<20}")
    print("-" * 55)

    for emp in emprestimos_usuario:
        print(f"{emp.livro.titulo:<30} {emp.data_emprestimo:<20}")

    # ==================== FUNÇÕES DE EMPRÉSTIMOS ====================
    
    def realizar_emprestimo(self):
        """Realiza um empréstimo de livro."""
        # TODO: Sidnei - Implementar empréstimo
        # - Verificar se o livro está disponível
        # - Atualizar livro.disponivel = False
        # - Criar objeto Emprestimo e adicionar na lista emprestimos
        print("\n--- REALIZAR EMPRÉSTIMO ---")
        print("[Função a ser implementada pelo Sidnei]")
    
    def devolver_livro(self):
        """Realiza a devolução de um livro."""
        # TODO: Sidnei - Implementar devolução
        # - Atualizar livro.disponivel = True
        # - Atualizar emprestimo.data_devolucao
        print("\n--- DEVOLVER LIVRO ---")
        print("[Função a ser implementada pelo Sidnei]")
    
    def listar_emprestimos_ativos(self):
        """Lista todos os empréstimos ativos."""
        # TODO: Sidnei - Pode implementar como funcionalidade extra
        print("\n--- EMPRÉSTIMOS ATIVOS ---")
        print("[Função a ser implementada pelo Sidnei]")
    
    # ==================== FUNÇÕES DE RELATÓRIOS ====================
    
    def listar_emprestimos_por_usuario(self):
        """Lista livros emprestados por um usuário."""
        # TODO: Arthur - Implementar listagem de livros emprestados por usuário
        # Percorrer a lista emprestimos e filtrar por usuário
        print("\n--- LIVROS EMPRESTADOS POR USUÁRIO ---")
        print("[Função a ser implementada pelo Arthur]")
    
    def exibir_historico_usuario(self):
        """Exibe o histórico completo de empréstimos de um usuário."""
        # TODO: Arthur - Funcionalidade adicional (opcional)
        # Exibir histórico completo de empréstimos de um usuário
        print("\n--- HISTÓRICO DE EMPRÉSTIMOS ---")
        print("[Função adicional - Arthur pode implementar para bônus]")
    
    def listar_emprestimos_atrasados(self):
        """Lista todos os empréstimos atrasados."""
        # TODO: Funcionalidade adicional (opcional)
        # Qualquer pessoa pode implementar para bônus
        print("\n--- EMPRÉSTIMOS ATRASADOS ---")
        print("[Função adicional - pode implementar para bônus]")
    
    # ==================== CONTROLE DE MENUS ====================
    
    def menu_livros(self):
        """Controla o menu de livros."""
        while True:
            self.limpar_tela()
            self.exibir_menu_livros()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                self.cadastrar_livro()
                self.pausar()
            elif opcao == '2':
                self.listar_livros()
                self.pausar()
            elif opcao == '3':
                self.editar_livro()
                self.pausar()
            elif opcao == '4':
                self.remover_livro()
                self.pausar()
            elif opcao == '0':
                break
            else:
                print("\n✗ Opção inválida!")
                self.pausar()
    
    def menu_usuarios(self):
        """Controla o menu de usuários."""
        while True:
            self.limpar_tela()
            self.exibir_menu_usuarios()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                self.cadastrar_usuario()
                self.pausar()
            elif opcao == '2':
                self.listar_usuarios()
                self.pausar()
            elif opcao == '0':
                break
            else:
                print("\n✗ Opção inválida!")
                self.pausar()
    
    def menu_emprestimos(self):
        """Controla o menu de empréstimos."""
        while True:
            self.limpar_tela()
            self.exibir_menu_emprestimos()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                self.realizar_emprestimo()
                self.pausar()
            elif opcao == '2':
                self.devolver_livro()
                self.pausar()
            elif opcao == '3':
                self.listar_emprestimos_ativos()
                self.pausar()
            elif opcao == '0':
                break
            else:
                print("\n✗ Opção inválida!")
                self.pausar()
    
    def menu_relatorios(self):
        """Controla o menu de relatórios."""
        while True:
            self.limpar_tela()
            self.exibir_menu_relatorios()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                self.listar_emprestimos_por_usuario()
                self.pausar()
            elif opcao == '2':
                self.exibir_historico_usuario()
                self.pausar()
            elif opcao == '3':
                self.listar_emprestimos_atrasados()
                self.pausar()
            elif opcao == '0':
                break
            else:
                print("\n✗ Opção inválida!")
                self.pausar()
    
    def executar(self):
        """Executa o sistema."""
        while self.executando:
            self.limpar_tela()
            self.exibir_menu_principal()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                self.menu_livros()
            elif opcao == '2':
                self.menu_usuarios()
            elif opcao == '3':
                self.menu_emprestimos()
            elif opcao == '4':
                self.menu_relatorios()
            elif opcao == '0':
                print("\n👋 Encerrando sistema...")
                self.executando = False
            else:
                print("\n✗ Opção inválida!")
                self.pausar()
