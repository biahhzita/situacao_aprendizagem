from database import Equipamentos, Salas
from lib.funcoes import verificar_equipamento, verificar_sala, atualizar_equipamento, atualizar_sala, deletar_equipamento

def menu():
    return """
    Menu
    1 - Cadastrar equipamento
    2 - Cadastrar sala
    3 - Verificar equipamento
    4 - Verificar sala
    5 - Atualizar equipamento
    6 - Atualizar sala
    7 - Deletar equipamento
    8 - Sair
""" 
while True:
    print(menu())
    op = int(input("Digite a opção: "))
    if op ==1:
        print(f"Cadastro de equipamento")
        class_equipamento = input("Digite a classificação do equipamento: ")
        modelo_equipamento = input("Modelo: ")
        valor_equipamento = float(input("Valor: "))
        Equipamentos.append({"id": "...", "Classificação": class_equipamento, "Modelo": modelo_equipamento, "Valor": valor_equipamento})
        print(Equipamentos)
    
    elif op ==2:
        print(f"Cadastro de sala")
        nome_sala = input("Digite o nome da sala: ")
        Salas.append({"id": "...", "Nome": nome_sala})
        print(Salas)

    elif op ==3:
        print(Equipamentos)
        id_ver_equipamento = int(input("Digite o id do equipamento para a verificação: "))
        verificar_equipamento(Equipamentos, id_ver_equipamento)

    elif op ==4:
        print(Salas)
        id_ver_sala = int(input("Digite o id da sala para a verificação: "))
        verificar_sala(Salas, id_ver_sala)

    elif op ==5:
        print(Equipamentos)
        update_equipamento = int(input("Digite o id do equipamento que você deseja atualizar: "))
        atualizar_equipamento(Equipamentos, update_equipamento)

    elif op ==6:
        print(Salas)
        update_sala = int(input("Digite o id da sala que você deseja atualizar: "))
        atualizar_sala(Salas, update_sala)
    
    elif op ==7:
        print(Equipamentos)
        delete_equipamento = int(input("Digite o ID que deseja deletar: "))
        deletar_equipamento(Equipamentos, delete_equipamento)

    else:
        print("Saindo do sistema...")
        break