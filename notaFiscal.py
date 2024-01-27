
salario = float(input('Qual é o salário do mês? R$ '))
pis = (salario * 0.65 / 100)
csll = (salario * 1 / 100)
ir = (salario * 1.5 / 100)
cofins = (salario * 3 / 100)

print('O salário é R${:.2f}. O pis é {:.2f}. O csll é {:.2f}. O imposto de renda é {:.2f}. O cofins é {:.2f}.'.format(salario, pis, csll, ir, cofins))


