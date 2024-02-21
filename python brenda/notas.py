nota1=float(input("digite a nota do primeiro bimestre: "))
nota2=float(input("digite a nota do segundo bimestre: "))
nota3=float(input("digite a nota do terceiro bimestre: "))
nota4=float(input("digite a nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("a nota do 1° bimestre é:",nota1)
print("a nota do 2° bimestre é:",nota2)
print("a nota do 13° bimestre é:",nota3)
print("a nota do 4° bimestre é:",nota4)
print('a media final é',media)

if media >=7:
    print ("aprovado")
else: 
        print ("reprovado")