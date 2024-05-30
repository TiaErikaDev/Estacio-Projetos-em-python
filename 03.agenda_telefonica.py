""" Módulo que contém uma classe que representa uma agenda telefônica. """


class AgendaTelefonica:
    """Classe que representa uma agenda telefônica."""

    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        """Método que adiciona um contato à agenda."""
        if nome in self.contatos:
            return "Contato já existente!"
        else:
            self.contatos[nome] = telefone
            return "Contato adicionado com sucesso!"

    def remover_contato(self, nome):
        """Método que remove um contato da agenda."""
        if nome not in self.contatos:
            return "Contato não encontrado!"
        else:
            del self.contatos[nome]
            return "Contato removido com sucesso!"

    def pesquisar_contato(self, nome):
        """Método que busca um contato na agenda e imprime o resultado."""
        if nome in self.contatos:
            telefone = self.contatos[nome]
            return f"Nome: {nome} - Telefone: {telefone}"
        else:
            return "Contato não encontrado"

    def listar_contatos(self):
        """Método que exibe todos os contatos da agenda."""
        if not self.contatos:
            return "Nenhum contato na agenda!"
        else:
            contatos_list = [
                f"Nome: {nome} - Telefone: {telefone}"
                for nome, telefone in self.contatos.items()
            ]
            return "\n".join(contatos_list)

    def __str__(self):
        return str(self.contatos)


def menu():
    """Função que exibe o menu da agenda telefônica e manipula as entradas do usuário."""
    agenda = AgendaTelefonica()

    while True:
        print("\n1. Adicionar contato")
        print("2. Remover contato")
        print("3. Pesquisar contato")
        print("4. Listar contatos")
        print("5. Sair \n")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "5":
            print("Obrigada por utilizar a agenda telefônica!")
            break
        elif escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            mensagem = agenda.adicionar_contato(nome, telefone)
            print(mensagem)
        elif escolha == "2":
            nome = input("Digite o nome do contato: ")
            mensagem = agenda.remover_contato(nome)
            print(mensagem)
        elif escolha == "3":
            nome = input("Digite o nome do contato: ")
            mensagem = agenda.pesquisar_contato(nome)
            print(mensagem)
        elif escolha == "4":
            contatos = agenda.listar_contatos()
            print(contatos)
        else:
            print("Escolha inválida, tente novamente.")


if __name__ == "__main__":
    menu()
