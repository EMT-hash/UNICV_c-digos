import json
import inquirer
import os
import colorama

tarefas = []

if os.path.exists("tarefas.json"):
    with open("tarefas.json", "r") as arquivo:
        tarefas = json.load(arquivo)
else:
    tarefas = []

def adicionar_tarefa():
    return{
        "Tarefa" : input("Adicione uma Tarefa: "),
        "Data" : input("Marque uma data (dd/mm/aaaa): "),
        "Hora" : input("Marque um horário: ")
    }


while True:
    tarefa = [
        inquirer.List(
            "escolha",
            message = "Escolha que ação deseja fazer",
            choices = ["Adicionar uma Tarefa" , "Ver Tarefas" ,"Excluir uma Tarefa" , "Sair"]
        )
    ]

    resposta = inquirer.prompt(tarefa)
    os.system("cls")

    print(f"Sua escolha foi {colorama.Fore.RED + resposta["escolha"]}{colorama.Style.RESET_ALL}")

    match resposta["escolha"]:
        case "Adicionar uma Tarefa":
            while True:
                    t = adicionar_tarefa()
                    tarefas.append(t)
                    with open("tarefas.json", "w") as arquivo:
                        json.dump(tarefas, arquivo)

                    for chave, valor in t.items():
                        print(f"{chave} : {valor}")

                    continuar = input("Deseja adicionar outra Tarefa S/N \n").upper()

                    if continuar != "S":
                         break
                    
        case "Ver Tarefas":
           for i, tarefa in enumerate(tarefas,start=1):
            print(f"\nTarefa {i}")

            for chave, valor in tarefa.items():

                print(f"{chave} : {valor}")
        
        case "Excluir uma Tarefa":
            while True:
                excluir = input("Digite o índice da tarefa que você deseja deletar: ")

                if excluir.strip() == "":
                    print("Digite um valor válido")
                    continue
                
                if not excluir.isdigit():
                    print("Digite apenas números!")
                    continue

                indice = int(excluir)

                if indice < 0 or indice >= len(tarefas):
                    break
                    


                deletado = tarefas.pop(int(excluir))
                print(f"Tarefa deletada:\n{deletado['Tarefa']} - {deletado['Data']} às {deletado['Hora']}")
                print("Tarefa deletada com sucesso")
                break
                
    
        case "Sair":
            exit()

    input("\nPressione ENTER para voltar ao menu...")
