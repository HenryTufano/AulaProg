def calvel():
    G=float(input("Digite o valor da constante gravitacional universal: "))
    g1=float(input("Digite o valor da elevação: "))
    r=float(input("Digite o valor do raio: "))
    M=float(input("Digite o valor da massa do planeta: "))
    m1=float(input("Digite o valor da elevação: "))
    x=G*(10**g1)
    y=M*(10**m1)
    v=((x*y)/r)
    v=v**0.5
    print(v)

def calal():
    G=float(input("Digite o valor da constante gravitacional universal: "))
    g1=float(input("Digite o valor da elevação: "))
    v=float(input("Digite o valor da velocidade: "))
    M=float(input("Digite o valor da massa do planeta: "))
    m1=float(input("Digite o valor da elevação: "))
    x=G*(10**g1)
    y=M*(10**m1)
    r=((x*y)/v)
    print(r)
    


op=8
while op!=0:
    op=int(input("Escolha uma das opções:\n [2]-Calcular a velocidade minima do Objeto \n [1]-Calcular a altura minima\n [0]-Sair do programa\nDigite uma escolha: "))

    if op==1:
        calal()
    elif op==2:        
        calvel()
    elif op!=0 or op!=1 or op!=2:
        print("Digite uma opção valida")
else:
    print("Finalizando o software")
    