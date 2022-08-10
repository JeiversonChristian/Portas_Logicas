n = int(input()) # tananho das sequências
erro = 0 # variável de controle para erros

s1 = input()
s1 = s1.strip() # removendo espaços indesejados
s1 = list(s1) # transformo a entrada em uma lista de strings

s2 = input()
s2 = s2.strip()
s2 = list(s2)

exp = input() # exp de "expressão"
exp = exp.strip()
exp = exp.split(" ") # separo a expressão lógica em "palavras"

#verificando erros
#--------------------------------------------------------------------------------------------------------------
if n > 1000: # erro no valor máximo para  a sequência
    erro = 1

if len(s1)!= n or len(s2)!= n: # erro no tamanho das sequências
    erro = 1

for i in range(1, len(exp), 2): # erro nas operações lógicas
    if exp[i]!="AND" and exp[i]!="OR" and exp[i]!="XOR" and exp[i]!="NAND" and exp[i]!="NOR" and exp[i]!="MOR":
        erro = 1

if erro != 1: # so pode testar as sequências se pelo menos elas tiverem o tamanho certo
    for i in range(n): # erro nos símbolos das sequências
        if (s1[i]!="0" and s1[i]!="1") or (s2[i]!="0" and s2[i]!="1"):
            erro = 1
#--------------------------------------------------------------------------------------------------------------

saida = [] # saída a ser apresentada na saída
sequencia1 = [] # a primeira sequência digitada ficará armazenada aqui
sequencia2 = [] # a segunda sequência digitada ficará armazenada aqui

if erro == 1:
    print("ERRO")
else:
    # definindo qual é a primeira sequência e qual é a segunda
    #----------------------------------------------------------------------------------------------------------
    for j in range(1, len(exp), 2): # vai fazer de acorodo com a quantidade de operações

        if j == 1: # a primeira vez as sequências 1 e 2 ficam definidas assim
            if exp[0] == "S1":
                sequencia1 = s1
            elif exp[0] == "S2":
                sequencia1 = s2
            if exp[2] == "S2":
                sequencia2 = s2
            elif exp[2] == "S1":
                sequencia2 = s1
        elif j == 3: # já na segunda vez (se tiver uma)...
            sequencia1 = saida # se ouver mais de uma operação, ao final da primeira, a saída deverá ser usada
                               # para operar com a próxima sequência
            if exp[4] == "S1":
                sequencia2 = s1
            else:
                sequencia2 = s2
            saida = [] # aqui eu "reseto" a saída para poder criar uma nova que será apresentada no final
    #----------------------------------------------------------------------------------------------------------

    #fazendo as operações lógicas:
    #----------------------------------------------------------------------------------------------------------
        if exp[j] == "AND":
            for i in range(n):
                if sequencia1[i] == "1" and sequencia2[i] == "1":
                    saida.append("1")
                else:
                    saida.append("0")

        elif exp[j] == "OR":
            for i in range(n):
                if sequencia1[i] == "1" or sequencia2[i] == "1":
                    saida.append("1")
                else:
                    saida.append("0")

        elif exp[j] == "XOR": # OR exclusivo
            for i in range(n):
                if (sequencia1[i]=="0" and sequencia2[i]=="0") or (sequencia1[i]=="1" and sequencia2[i]=="1"):
                    saida.append("0")
                else:
                    saida.append("1")

        elif exp[j] == "NAND": # negação do AND
            for i in range(n):
                if sequencia1[i] == "1" and sequencia2[i] == "1":
                    saida.append("0")
                else:
                    saida.append("1")

        elif exp[j] == "NOR": # negação do OR
            for i in range(n):
                if sequencia1[i] == "1" or sequencia2[i] == "1":
                    saida.append("0")
                else:
                    saida.append("1")

        elif exp[j] == "MOR": # se então
            for i in range(n):
                if sequencia1[i] == "1" and sequencia2[i] == "0":
                    saida.append("0")
                else:
                    saida.append("1")
    #----------------------------------------------------------------------------------------------------------

    #apresentando a saída
    for i in range(n):
        print(saida[i], end="")