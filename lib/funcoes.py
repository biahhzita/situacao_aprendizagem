def verificar_equipamento (Equipamentos, id_ver_equipamento):
    for v_e in Equipamentos:
        if v_e["id"] == id_ver_equipamento:
            verificado = v_e
            print(v_e)
            return verificado

    print(f"Não existe um equipamento cadastrado com esse id.")
    return False

def verificar_sala (Salas, id_ver_sala):
    for v_s in Salas:
        if v_s["id_sala"] == id_ver_sala:
            verificado = v_s
            print(v_s)
            return verificado
    print(f"Não existe uma sala cadastrada com esse id.")
    return False

def atualizar_equipamento (Equipamentos, update_equipamento):
    for up_e in Equipamentos:
        if up_e["id"] == update_equipamento:
            verificado = up_e
            print(f""" 
                  1 - classificação
                  2 - modelo
                  3 - valor
                  4 - id da sala
                  """)
            
            op_update_e = int(input("Selecione o que você quer atualizar: "))
            if op_update_e ==1:
                up_e["classificacao"] = input("Digite a nova classificação: ")
            elif op_update_e ==2:
                up_e["modelo"] = input("Digite o novo modelo: ")
            elif op_update_e ==3:
                up_e["valor"] = input("Digite o novo valor: ")
            elif op_update_e ==4:
                up_e["id_sala"] = input("Digite o id da nova sala: ")
            else:
                print("Opção inválida.")
            print("Equipamento alterado com sucesso!")

            return verificado
def atualizar_sala (Salas, update_sala):
    for up_s in Salas:
        if up_s["id_sala"] == update_sala:
            verificado = up_s
            print(f"""
                  1 - Nome
                  """)
            op_update_s = int(input("Selecione o que você quer atualizar: "))
            if op_update_s ==1:
                up_s["nome"] = input("Digite o novo nome: ")
            else:
                print("Opção inválida.")
            print("Equipamento alterado com sucesso!")

            return verificado
        
def deletar_equipamento (Equipamentos, delete_equipamento):
    armazena= None # variável equipo
    for d in Equipamentos:
        if d["id"] == delete_equipamento:
            armazena = d # armazena d em equipo
            break
    Equipamentos.remove(armazena)
    print(f"Deletado com sucesso!")
    #fora do loop apaga equipo do equipamentos