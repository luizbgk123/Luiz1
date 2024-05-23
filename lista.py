nume_inicial = int(input("Qual o numero inicial: "))
nume_final = int(input("Qual o numero final: "))

tamanhoIntervalo = nume_final - nume_inicial

if(tamanhoIntervalo > 100):
    print("Tamanho execidido")
else:
    for i in range(nume_inicial,nume_final+1):
        print(i)
