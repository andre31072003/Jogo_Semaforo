from numpy import copy
from random import randint

def lerfile(): #abre o ficheiro, le e da split por linha 
    f = open("Savefile.txt", "r")
    jogo=f.read()
    lines=jogo.split('\n')
    #print(lines)
    return lines

def savefile(tabuleiro,jogatual,opcao,Jog1,Jog2): #guarda o estado do jogo matriz de jogo(separada por ';'), o jogador a jogar e o tipo de jogo (contra humano ou bot)
    f = open("Savefile.txt", "w")
    for x in range(3):
        for y in range(4):
            f.write(str(tabuleiro[x][y])+';')
    f.write('\n'+str(jogatual)+'\n'+str(opcao)+'\n'+str(Jog1)+';'+str(Jog2))

def verificar(tabuleiro): # verifica se alguem ganhou
    #VERIFICAR LINHAS
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0]!=0:
        return True
    if tabuleiro[0][1] == tabuleiro[0][2] == tabuleiro[0][3] and tabuleiro[0][1]!=0:   
        return True
    if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][0]!=0:
         return True
    if tabuleiro[1][1] == tabuleiro[1][2] == tabuleiro[1][3] and tabuleiro[1][1]!=0:
         return True
    if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0]!=0:
        return True
    if tabuleiro[2][1] == tabuleiro[2][2] == tabuleiro[2][3] and tabuleiro[2][1]!=0:
        return True    
    #VERIFICAR COLUNAS
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[0][0]!=0:
        return True
    if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[0][1]!=0:
        return True
    if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and tabuleiro[0][2]!=0:
        return True
    if tabuleiro[0][3] == tabuleiro[1][3] == tabuleiro[2][3] and tabuleiro[0][3]!=0:
        return True
    #VERIFICAR DIAGONAIS
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0]!=0:
        return True
    if tabuleiro[0][1] == tabuleiro[1][2] == tabuleiro[2][3] and tabuleiro[0][1]!=0:
        return True
    if tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] and tabuleiro[0][3]!=0:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2]!=0:
        return True
    return False

def showtab(tabuleiro): #printa o tabuleiro
    for x in range(3):
        print("   "+str(tabuleiro[x]))

def checkjogada(tabuleiro,i,j): #vrifica se uma jogada é possivel
    if i<0 or i>2 or j<0 or j>3: #verifica se esta dentro do array
        return False
    if tabuleiro[i][j]==3: #se ja esta a tentar jogar em cima de um vermelho
        return False
    return True

def game(tabuleiro,jogatual,Jog1="",Jog2=""):
    #defenicao dos jogadores
    if Jog1=="" and Jog2=="":          
        Jog1=input("Insira o nome do jogador 1: ")
        Jog2=input("Insira o nome do jogador 2: ")
    if jogatual==0:
        jogatual=randint(1,2) #escolha random do player a começar
    showtab(tabuleiro)
    i=""
    j="z"
    while(verificar(tabuleiro)==False):
        i=-1
        j=-1
        
 ##### como por o jogador a jogar
        if jogatual==1:     
            jogatual=jogadahumana(tabuleiro,Jog1,jogatual)
            if jogatual==-1: #caso o utlizador escreva "sair" na sua jogada a função "jogadahumana" retorna -1 para o jogatual
                savefile(tabuleiro,1,1,Jog1,Jog2)
                return False
        else:           
            jogatual=jogadahumana(tabuleiro,Jog2,jogatual)
            if jogatual==-1: #caso o utlizador escreva "sair" na sua jogada a função "jogadahumana" retorna -1 para o jogatual
                savefile(tabuleiro,2,1,Jog1,Jog2)
                return False
    if jogatual==2:
        print("jogador %s ganhou!" % Jog1)
    else:
        print("jogador %s ganhou!" % Jog2)
    return True

def checkwins(tabuleiro,i,j): #verifica se existem jogadas que ganhem o jogo se sim retorna essa jogada[x,y] se nao retorna[i,j]
    for x in range(3):
        for y in range(4): #tenta todas jogadas até encontrar uma que ganhe o jogo ou retorna as variaveis de entrada i,j
            test=copy(tabuleiro)
            test[x][y]+=1
            if verificar(test):
                return [x,y]
    return [i,j]

def jogadahumana(tabuleiro,nome,jogatual):
    thrown=0#inicialização
    i="" 
    j=""
    print("\npara sair e guardar jogo escreva sair)")
    i=(input("Insira a primeira cordenada x do jogador %s:" % nome))        
    if i=="Sair" or i=="sair":
        return -1
    j=(input("Insira a segunda cordenada y do jogador %s:" % nome))
    if j=="Sair" or j=="sair":
        return -1
    try: # estrutura para caso utilisador insira valores na inteiros
        _i=int(i)
        _j=int(j)
        _i-=1
        _j-=1
    except: # se 'i' e 'j' nao forem transformaveis em inteiros da print mensagem de controlo e definição de uma variavel de controlor para saber se alguma exceção é lançada
        print('Insira um inteiro')
        thrown=1
        _i=-1
        _j=-1
    if checkjogada(tabuleiro,_i,_j) and thrown!=1: # se a jogada for legal da update à mesa e passa a jogada
        tabuleiro[_i][_j]+=1
        showtab(tabuleiro)
        if jogatual==1:
            jogatual+=1
        else:
            jogatual=1
    else:                                           #se nao printa alerta
        print("jogada invalida!")
    return jogatual

def jogadaBOT(tabuleiro): #faz a jogada do bot
    i=-1#inicialização
    j=-1
    while checkjogada(tabuleiro,i,j)==False: #[i,j] é uma jogada random legal
        i=randint(0,2)
        j=randint(0,3)
    play=checkwins(tabuleiro,i,j) #verifica se existem jogadas que ganhem o jogo se sim retorna essa jogada[x,y] se nao retorna[i,j]
    print("bot jogou %i %i"%(play[0]+1,play[1]+1) )
    tabuleiro[play[0]][play[1]]+=1
    showtab(tabuleiro)
    jogatual=1
    return jogatual

def gamebot(tabuleiro,jogatual,Jog1=""): #jogo humano vs. bot 
    #defenicao do jogador  
    if Jog1=="":
        Jog1=input("Insira o nome do jogador 1: ")
    if jogatual==0:#caso o jogo seja carregado do file
        jogatual=randint(1,2) #escolha aleatória do player
    showtab(tabuleiro)
    while(verificar(tabuleiro)==False):
 ##### jogo humano(1) vs. bot(2)
        if jogatual==1:     
            jogatual=jogadahumana(tabuleiro,Jog1,jogatual)
            if jogatual==-1:
                savefile(tabuleiro,jogatual,2,Jog1,"BOT")
                return False
        else:           
            jogatual=jogadaBOT(tabuleiro)
    if jogatual==2:
        print("jogador %s ganhou!" % Jog1)
    else:
        print("BOT ganhou!")
    return True

def menu():
    tabuleiro=[[0,0,0,0], #inicialização de 
               [0,0,0,0],
               [0,0,0,0]]
    #menu
    print('''
    [1] Jogar com pessoa
    [2] Jogar com o computador
    [3] Carregar jogo guardado
    [4] Regras de jogo
    [0] Sair'''   )
    try: #estrutura try caso o utilizador inserir valores nao inteiro na opçao de menu
        opcao=int(input("Qual e a sua opcao? "))
    except: #caso não seja um valor não transformável em inteiro a função int() lança uma exceção
        print("insira um inteiro!")
        return False
#jogar com amigo
    if opcao==1 :
        game(tabuleiro,0)
#jogar contra bot
    if opcao==2:
        gamebot(tabuleiro,0)
#carregar partida
    if opcao==3:
        lines=lerfile() 
        #valores do file separados por linha:
        #lines[0]=matriz de jogo
        #lines[1]=jogador a jogar
        #lines[2]=tipo de jogo(contra humano ou bot)
        #lines[3]/[4]=nomes
        temp=lines[0].split(';')#valores da matriz estão no file separados por ';'
        for x in range(3):
            for y in range(4):
                tabuleiro[x][y]=int(temp[x*4+y])#os valores da matriz encontram-se todos seguidos em um array
                                                #entao temos que os ordenar numa matriz 2D
        jogatual=int(lines[1])#jogador a atual
        opcao=int(lines[2])#opção do jogo(1-humano vs. humano // 2-humano vs. BOT)
        nomes=lines[3].split(';')
        if opcao == 1 :
            Jog1=nomes[0]
            Jog2=nomes[1]
            game(tabuleiro,jogatual,Jog1,Jog2)
        else:
            nome=nomes[0]
            gamebot(tabuleiro,jogatual,nome)
    if opcao==4:
        f=open("regras.txt")
        print(f.read())
#sair
    if opcao==0:
        print("Finalizando...")
        exit()
        
while True:
    menu()