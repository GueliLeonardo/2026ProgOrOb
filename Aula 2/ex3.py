n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
x = [n1, n2, n3, n4]


if len(x) != len(set(x)):
    print("Erro")
else:

    x_ordem = sorted(x)
  
    menor = x_ordem[0]
    segundo_menor = x_ordem[1]
    segundo_maior = x_ordem[2]
    maior = x_ordem[3]
    
    soma = segundo_maior + segundo_menor
    
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Segundo maior: {segundo_maior}")
    print(f"Segundo menor: {segundo_menor}")
    print(f"Soma do segundo maior com o segundo menor: {soma}")
