#Exercício 1
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
print(f'Soma: {n1 + n2}')

#Exercício 2
m = float(input('Valor em metros: '))
print(f'Valor é igual a {m * 1000:.0f} milímetros')

#Exercício 3
d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
print(f'Total em segundos: { s + (m*60) + (h*60*60) + (d*60*60*24) } ')

#Exercício 4
s1 = float(input('Salário antigo: '))
p = float(input('Porcentagem do aumento: '))
a = s1 * p /100
s2 = s1 + a
print(f'Aumento de R${a:.2f} . Novo salário: R${s2:.2f}')

#Exercício 5
v = float(input('Preço da mercadoria: '))
p = float(input('Percentual do desconto: '))
print(f'Desconto: R${v * p/100:.2f} . Preço com desconto: R${v - (v*p/100):.2f}.')

#Exercício 6
d = float(input('Distância em km: '))
vm = int(input('Velocidade média em km/h: '))
print(f'Tempo da viagem: {d / vm:.1f} hora(s)')

#Exercício 7
c = int(input('Tempratura em graus Celcius: '))
print(f'{(9*c/5) + 32}° Fahrenheit')

#Exercício 8
f = int(input('Temperatura em graus Fahrenheit: '))
print(f'{5/9 * (f-32)}° Celcius')

#Exercício 9
km = int(input('Km percorridos: '))
d = int(input('Dias de locação: '))
print(f'Preço a pagar: R${(km*0.15) + (d*60):.2f}.')

#Exercício 10
c = int(input('Cigarros por dia: '))
a = int(input('Anos fumando: '))
print(f'Dias de vida a menos: {c * a * 365 / 144:.0f}')

#Exercício 11
print (len(str(2**1000000)))
