import os
agenda=[]
cntt=[]
nome=[]
s=False
opc=int(input("O que deseja fazer?:\n(1)Inserir um novo contato:\n(2)Exibir a lista de contatos:\n(3)Editar contato:\n(4)Remover contato:\nResposta:",))
nvcntt=[]
nvnome=[]

if (opc == 1):
    nome.append(str(input("Informe o nome do contato \n")))
    nvnome.append(nome)
    cntt.append(int(input("Informe o número do contato \n")))
    nvcntt.append(cntt)
    agenda.append(nvnome)
    
    os.system('cls')
    print("Novo contato adicionado:",nvnome," | ",nvcntt)
if (opc == 2):
    for cntt in agenda:
        print ("Nome:",(nvnome),"|  telefone",(nvcntt))
        print(" ")    
   
