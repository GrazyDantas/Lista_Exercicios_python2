#Crie um programa que analise uma lista de palavras e encontre anagramas usando manipulação de strings
palavras = ["uva", "pêra", "maça", "pessoa", "código"]

i= 0
try:
    while (i != len(palavras)):
        Palavra = palavras[i]
        print(Palavra,len(palavras[i]))
        i += 1
        letra = Palavra[i]
        j = 0

        while (j != len(Palavra)):
            letra = Palavra[j]
            print(letra)
            j += 1

            if (Palavra == letra):
                fatorial = len(Palavra)
                while(fatorial != 0):
                    anagramas *= fatorial
                    fatorial -= 1
                    print("A quantidade de anagramas para a palavra",Palavra,"é:",anagramas)
except:
    print("Não foi possivel verificar a proxima")