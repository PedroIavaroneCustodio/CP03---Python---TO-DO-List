from tarefas import *
from persistencia import *

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n📋 GERENCIADOR DE TAREFAS")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            desc = input("Descrição: ")
            venc = input("Data de vencimento (dd/mm/aaaa): ")
            tarefa = criar_tarefa(desc, venc)
            tarefas.append(tarefa)
            salvar_tarefas(tarefas)
            print("✅ Tarefa adicionada com sucesso!")

        elif opcao == "2":
            status = input("Filtrar por status (enter para todos): ")
            for i, t in enumerate(listar_tarefas(tarefas, status)):
                print(f"{i} - {t['descricao']} | {t['vencimento']} | {t['status']}")

        elif opcao == "3":
            indice = int(input("Número da tarefa: "))
            novo_status = input("Novo status (Pendente/Em andamento/Concluída): ")
            atualizar_tarefa(tarefas, indice, novo_status=novo_status)
            salvar_tarefas(tarefas)
            print("🔄 Tarefa atualizada!")

        elif opcao == "4":
            indice = int(input("Número da tarefa: "))
            remover_tarefa(tarefas, indice)
            salvar_tarefas(tarefas)
            print("🗑️ Tarefa removida!")

        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida!")
