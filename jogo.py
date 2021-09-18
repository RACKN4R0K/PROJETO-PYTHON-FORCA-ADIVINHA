

print("***********************************")
print("*****bem-vindo escolha o  jogo*****")
print("***********************************")

print("(1) adinhivação (2)Forca")

jogo =  int(input("Qual o jogo você escolhe? "))

if(jogo == 1):
    print("Jogando adivinhação")
    import jogoadivinha
elif(jogo == 2):
    print("Jogando forca")
    import forca

print("Fim do jogo!")


