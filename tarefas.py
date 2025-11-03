import datetime

def criar_tarefa(descricao, vencimento, status="Pendente"):
    return {
        "descricao": descricao,
        "vencimento": vencimento,
        "status": status
    }

def listar_tarefas(tarefas, filtro_status=None):
    if filtro_status:
        return [t for t in tarefas if t["status"].lower() == filtro_status.lower()]
    return tarefas

def atualizar_tarefa(tarefas, indice, nova_desc=None, novo_venc=None, novo_status=None):
    try:
        tarefa = tarefas[indice]
        if nova_desc:
            tarefa["descricao"] = nova_desc
        if novo_venc:
            tarefa["vencimento"] = novo_venc
        if novo_status:
            tarefa["status"] = novo_status
        return True
    except IndexError:
        return False

def remover_tarefa(tarefas, indice):
    try:
        tarefas.pop(indice)
        return True
    except IndexError:
        return False
