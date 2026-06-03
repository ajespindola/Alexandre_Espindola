from data.data_manager import carregar_dados, salvar_dados  # Certifique-se de ter/importar a função salvar_dados
from ui.menus import criar_usuario_menu, painel_principal_menu
from ui.utils import exibir_cabecalho

def executar_sistema():
    while True:
        dados = carregar_dados()
        exibir_cabecalho("SISTEMA DE APOIO AO ESTUDANTE - TEA")
        print("1. Entrar com perfil existente")
        print("2. Criar novo perfil de estudante")
        print("3. Apagar um perfil existente")
        print("4. Encerrar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            if not dados:
                input("\nNenhum perfil salvo. Crie um primeiro! (Enter)")
                continue
            print("\nPerfis:")
            for u in dados: print(f"- {u}")
            nome = input("\nNome do perfil: ").strip()
            if nome in dados:
                painel_principal_menu(dados, nome)
            else:
                input("\nPerfil não encontrado! (Enter)")
                
        elif opcao == "2":
            criar_usuario_menu(dados)
            
        elif opcao == "3":
            if not dados:
                input("\nNenhum perfil salvo para apagar! (Enter)")
                continue
            
            print("\nPerfis existentes:")
            for u in dados: print(f"- {u}")
            
            nome = input("\nNome do perfil que deseja apagar (ou Enter para cancelar): ").strip()
            
            if not nome:
                continue
                
            if nome in dados:
                confirmacao = input(f"Tem certeza que deseja apagar o perfil '{nome}'? (s/n): ").strip().lower()
                if confirmacao == 's':
                    # Remove o perfil dos dados
                    if isinstance(dados, dict):
                        del dados[nome]
                    else:
                        dados.remove(nome) # Use remove caso 'dados' seja uma lista
                        
                    # Salva os dados atualizados de volta no arquivo
                    salvar_dados(dados) 
                    input(f"\nPerfil '{nome}' apagado com sucesso! (Enter)")
            else:
                input("\nPerfil não encontrado! (Enter)")
                
        elif opcao == "4":
            print("\nAté logo! Bons estudos!")
            break

if __name__ == "__main__":
    executar_sistema()