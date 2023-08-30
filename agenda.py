import os
agenda=[]
cntt=[]
nome=[]
nvcntt=[]
s=False
opc=int(input("O que deseja fazer?:\n(1)Inserir um novo contato:\n(2)Exibir a lista de contatos:\n(3)Editar contato:\n(4)Remover contato:\nResposta:",))


if (opc == 1):
    nome.append(str(input("Informe o nome do contato \n")))
    nvcntt.append(nome)
    cntt.append(int(input("Informe o número do contato \n")))
    nvcntt.append(cntt)
    agenda.append(nvcntt)
    
    os.system('cls')
    print("Novo contato adicionado:",nvcntt[0]," | ",nvcntt[1])
if (opc == 2):
    for nvcntt in agenda:
        print("\nNome:",nvcntt[0],"Telefone",nvcntt[1],"\n")  
if(opc==3):
    nome=input("\nDigite o nome do contato a editar:")
    for i in range(len(agenda)):
        if(agenda[i][0]==nome):
            nvnome=input("Digite o novo nome do contato")
            nvc=input("Digite o novo telefone do contato")
            agenda[i][0]=nvnome
            agenda[i][0]=nvc
            os.system('cls')
            break  
if(opc==4):
    nome=input("\nInforme o nome do contato que deseja excluir:")
    for i in range(len(agenda)):
        if(agenda[i][0]==nome):
            agenda.remove(nome)
            agenda.pop(0)
            print(agenda)

   
