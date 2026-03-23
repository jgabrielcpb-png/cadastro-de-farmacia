import os

farmacias = [{"nome": "Redepharma", "categoria": "remedios",  "ativo": True},
             {"nome": "Pague menos", "categoria": "remedios", "ativo": False },
             {"nome":  "Drogasil", "categoria": "remedios", "ativo": False} ]
              
def exibir_nome_do_programa(): 
 print( " 𝔻𝕣𝕠𝕘𝕒𝕣𝕚𝕒 𝕖𝕩𝕡𝕣𝕖𝕤𝕤: \n ")


def exibir_opçoes():
 print(" 1. cadastrar farmacia")
 print(" 2. listar farmacias")
 print(" 3. ativar farmacia ")
 print(" 4. sair ")

def voltar_ao_menu():
 voltar = input(" \naperte enter pra voltar ao menu")
 main()


def cadastrar_farm():
 os.system("cls") 
 nome_da_farmacia = input("digite o nome da farmacia: ")
 categoria_das_farmacias = input("digite a categoria da farmacia: ")
 dados_da_farmacias = { "nome": nome_da_farmacia, 
                       "categoria": categoria_das_farmacias,
                       "ativo": False}
 farmacias.append(dados_da_farmacias)
 print(f" famarcia {nome_da_farmacia} cadastrada com sucesso!")

 voltar_ao_menu()



def listar_farmacias():
 os.system("cls")
 print("listar farmacia: \n")
 print(f"{'Nome:'.ljust(20)} {'Categoria:'.ljust(20)} ativo:")
 for farmacia in farmacias: 
    ativa = "ativada" if farmacia ['ativo'] else "desativada"
    print(f"{farmacia ['nome'].ljust(20)} {farmacia['categoria'].ljust(20)} {ativa}")
 voltar_ao_menu()


def ativar_farmacia():
 os.system("cls")
 print("\nalterando estado da farmacia...")
 nome_da_farmacia = input("\ndigite o nome da farmacia que deseja alterar: ")
 farmacia_encontrada = False 
 for farmacia in farmacias:
  if nome_da_farmacia== farmacia["nome"]:
     farmacia_encontrada = True
     farmacia ["ativo"] = not farmacia ["ativo"]
     print("farmacia alterada com sucesso!")
 if not farmacia_encontrada:
        print(" farmacia não encontrada!")
 voltar_ao_menu()



def finalizar_app():
    print("Até logo!")
    exit()


def opçao_invalida ():
   print("\n opção invalida")
   voltar_ao_menu()
 

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_farm()
        elif opcao_escolhida == 2:
             listar_farmacias()
        elif opcao_escolhida == 3:
            ativar_farmacia()
        elif opcao_escolhida == 4:
           finalizar_app() 
        else:
           opçao_invalida()
    except ValueError:
     opçao_invalida()


def main(): 
 os.system("cls")
 exibir_nome_do_programa()
 exibir_opçoes()
 escolher_opcao()

    
if __name__ == '__main__':
  main()  