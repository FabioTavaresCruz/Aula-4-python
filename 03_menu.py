def soma():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    print ("A soma é", numero1 + numero2)

def subtracao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    print ("A subtração é", numero1 - numero2)

def multiplicacao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    print ("A multiplicação é", numero1 * numero2)

def divisao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    print ("Dividindo...")
    print ("A divisão é", numero1 / numero2)

def pares():
   quantidade = int(input("Digite quantos números você quer: "))
   par = 0
   loop = 1
   while loop <= quantidade:
        print(par + 2)
        par += 2
        loop += 1

def impar():
  quantidade = int(input("Digite quantos números você quer: "))
  impar = -1
  loop = 1
  while loop <= quantidade:
        print(impar + 2)
        impar += 2
        loop += 1

def somatoria():
   quantidade = int(input("Digite quantos números você quer: "))
   zero = 1
   smt = 0
   while zero <= quantidade:
      smt = smt + zero
      zero += 1
   print ("A somatoria é",smt)

def fatorial():
   quantidade = int(input("Digite o fatorial: "))
   zero = 1
   fatorial = 1
   while zero <= quantidade:
      fatorial = fatorial * zero
      zero += 1
   print ("O fatorial é",fatorial)

   

while True: 
 print ("CALCULADORA")
 print ("1 - Adição")
 print ("2 - Subtração")
 print ("3 - Multiplicação")
 print ("4 - Divisão")
 print ("5 - Pares")
 print ("6 - Ímpares")
 print ("7 - Somátoria")
 print ("8 - Fatorial")
 print ("0 - Sair")

 opcao = input ("Escolhe uma opção: ")

 if opcao == "1":
  soma()
 elif opcao == "2":
  subtracao()
 elif opcao == "3":
  multiplicacao()
 elif opcao == "4":
  divisao()
 elif opcao == "5":
   pares()
 elif opcao == "6":
   impar()
 elif opcao == "7":
   somatoria()
 elif opcao == "8":
    fatorial()


 elif opcao == "0":
  print ("Saindo...")
  break
 
 else:
  print ("Opção inválida, tente novamente!!!")