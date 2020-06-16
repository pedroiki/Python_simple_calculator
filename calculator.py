# faca uma calculadora em Python

a = float(input("give me one number: "))
b = float(input("give me the second number: "))
escolha = input("which operation you want to do it,\n\t for add press S ,\n\tfor subtract press B ,\n\t for Multiplication press M \n\t for / , press D  ")

soma = a+b
sub = a-b
mult = a*b
div = a/b

if escolha == "S" or escolha =="s":
    print("the addition of this numbers is: {}".format(soma))
elif escolha == "B" or escolha == "b":
     print(" the subtract of this number is: {}".format(sub))
elif escolha == "M" or escolha == "m" :
    print("the Multiplication of this number is: {}".format(mult))
else:
     print("the divion of this number is: {}".format(div))
