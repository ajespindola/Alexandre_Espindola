import core.ia_service as ia_service
import core.tarefas as core_tarefas
from data.data_manager import carregar_dados, salvar_dados
from ui.utils import exibir_cabecalho


def _pedir_prioridade():
    print("\nPrioridade da tarefa:")
    print("1. Baixa")
    print("2. Média")
    print("3. Alta")
    escolha = input("Escolha: ").strip()

    if escolha == "1":
        return "baixa"
    if escolha == "3":
        return "alta"
    return "media"


def _mostrar_tarefas(tarefas):
    if not tarefas:
        print("[Nenhuma tarefa cadastrada.]")
        return

    for idx, tarefa in enumerate(tarefas, 1):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        prioridade = tarefa.get("prioridade", "media").upper()
        prazo = tarefa.get("prazo", "Sem prazo") or "Sem prazo"

        print(f"{idx}. {status} {tarefa['titulo']}")
        print(f"   Prioridade: {prioridade} | Prazo: {prazo}")

        if tarefa.get("descricao"):
            print(f"   Descrição: {tarefa['descricao']}")

        for i, passo in enumerate(tarefa.get("passos", []), 1):
            simbolo = "✓" if passo.get("concluido") else " "
            print(f"   {i}. {simbolo} {passo['texto']}")


def criar_usuario_menu(dados: dict):
    exibir_cabecalho("CRIAR PERFIL DO ESTUDANTE")
    nome = input("Digite o nome do estudante: ").strip()
    if not nome or nome in dados:
        input("\nNome inválido ou já existente. Pressione Enter.")
        return

    print("\n--- Preferências de Comunicação ---")
    print("1. Passo curto e direto")
    print("2. Detalhado e explicativo")
    pref = input("Opção: ").strip()
    estilo = "direto" if pref == "1" else "detalhado"

    dados[nome] = {
        "preferencias": {"estilo_instrucao": estilo},
        "tarefas_diarias": [],
        "tarefas_educacionais": [],
    }
    salvar_dados(dados)
    input(f"\nPerfil [{nome}] criado! Pressione Enter.")


def gerenciar_tarefas_menu(dados: dict, usuario: str, chave: str, titulo: str):
    while True:
        exibir_cabecalho(titulo)
        tarefas = dados[usuario][chave]

        if not tarefas:
            print("[Nenhuma tarefa pendente.]")
        else:
            for idx, t in enumerate(tarefas, 1):
                status = "[X]" if t["concluida"] else "[ ]"
                print(f"{idx}. {status} {t['titulo']}")
                for p in t.get("passos", []):
                    print(f"   ○ {p['texto']}")

        print("\n" + "-" * 30)
        print(
            "1. Criar Tarefa | 2. Alternar Status | 3. 🤖 Desmembrar com IA | 4. Voltar"
        )
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            titulo_tarefa = input("Título da tarefa: ").strip()
            if not titulo_tarefa:
                input("\nO título não pode ficar vazio. Pressione Enter.")
                continue

            descricao = input("Descrição curta da tarefa: ").strip()
            prioridade = _pedir_prioridade()
            prazo = input("Prazo no formato AAAA-MM-DD (ou deixe vazio): ").strip()

            core_tarefas.adicionar_tarefa(
                dados, usuario, chave, titulo_tarefa, descricao, prioridade, prazo
            )
            input("\nTarefa criada com sucesso! Pressione Enter.")
        elif opcao == "2" and tarefas:
            try:
                idx = int(input("Número da tarefa: ")) - 1
                core_tarefas.alternar_status_tarefa(dados, usuario, chave, idx)
            except ValueError:
                pass
        elif opcao == "3" and tarefas:
            try:
                idx = int(input("Número da tarefa para IA tratar: ")) - 1
                if 0 <= idx < len(tarefas):
                    passos = ia_service.gerar_passos_tarefa(tarefas[idx]["titulo"])
                    print("\n🤖 Passos sugeridos pela IA:")
                    for i, p in enumerate(passos, 1):
                        print(f"  {i}. {p}")
                    if input("\nAceitar sugestão? (s/n): ").lower() == "s":
                        core_tarefas.injetar_passos_ia(
                            dados, usuario, chave, idx, passos
                        )
            except ValueError:
                pass
        elif opcao == "4":
            break


def painel_ia_menu(dados: dict, usuario: str):
    exibir_cabecalho("ASSISTENTE DE IA PARA TPAC")
    print("Peça ajuda para simplificar enunciados, organizar rotinas ou tirar dúvidas.")
    print("Digite 'sair' para retornar.\n")
    estilo = dados[usuario]["preferencias"]["estilo_instrucao"]

    while True:
        pergunta = input("\nVocê: ").strip()
        if pergunta.lower() == "sair":
            break
        if not pergunta:
            continue

        print("\n🤖 Processando sem ambiguidades...")
        respostas = ia_service.obter_resposta_ia(pergunta, estilo)
        print(f"\n[Assistente - Modo {estilo.upper()}]:")
        for linha in respostas:
            print(f"- {linha}")
        print("-" * 30)


def painel_principal_menu(dados: dict, usuario: str):
    while True:
        exibir_cabecalho(f"PAINEL DO USUÁRIO: {usuario}")
        print(
            "1. Rotinas Diárias\n2. Estudos e atividades\n3. Central de apoio\n4. Logout"
        )
        opcao = input("\nEscolha: ").strip()
        if opcao == "1":
            gerenciar_tarefas_menu(dados, usuario, "tarefas_diarias", "ROTINA DIÁRIA")
        elif opcao == "2":
            gerenciar_tarefas_menu(
                dados, usuario, "tarefas_educacionais", "ESTUDOS E EDUCAÇÃO"
            )
        elif opcao == "3":
            painel_ia_menu(dados, usuario)
        elif opcao == "4":
            break
