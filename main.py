import sys

tarefas = []

def menu():
        print("1 - adicionar tarefa")
        print("2 - ver tarefa")
        print("0 - sair")

def adicionar():
        nomeTarefa = str(input("nome da tarefa: "))
        tarefas.append(nomeTarefa)
        print(f"a tarefa {nomeTarefa} foi adicionada!")

def ver():
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"tarefa {i}: {tarefa}")

while True:
        print("bem vindo a To-Do List!")
        menu()
        escolha = int(input("escolha: "))

        print()

        if escolha == 0:
             print("saindo...")
             break
        elif escolha == 1:
             adicionar()
        elif escolha == 2:
             ver()
        else:
             print("escolha invalida!")

        print()