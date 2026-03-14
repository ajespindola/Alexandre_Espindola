#[LIST] Lista de compras simples com opções de adicionar e remover itens sem usar funções.
# Criando uma lista vazia para armazenar os itens da compra
lista_compras = []
# Loop para permitir que o usuário adicione ou remova itens
while True:
    # Exibindo o menu de opções para o usuário
    print("Menu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista de compras")
    print("4. Sair")
    # Solicitando a escolha do usuário
    escolha = input("Escolha uma opção (1-4): ")
    
    if escolha == '1':
        # Adicionando um item à lista de compras
        item = input("Digite o nome do item para adicionar: ")
        lista_compras.append(item)
        print(f"{item} adicionado à lista de compras.")
        
    elif escolha == '2':
        # Removendo um item da lista de compras
        item = input("Digite o nome do item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido da lista de compras.")
        else:
            print(f"{item} não encontrado na lista de compras.")
            
    elif escolha == '3':
        # Exibindo a lista de compras atual
        if lista_compras:
            print("Lista de Compras:")
            for idx, item in enumerate(lista_compras, start=1):
                print(f"{idx}. {item}")
        else:
            print("A lista de compras está vazia.")
            
    elif escolha == '4':
        # Saindo do programa
        print("Saindo do programa. Até mais!")
        break
        
    else:
        # Opção inválida
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")