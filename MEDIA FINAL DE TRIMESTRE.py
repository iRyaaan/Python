print("Olá Professor, Seja muito Bem-Vindo ao Caderno de Notas da Sua Sala! ")
nome_aluno = input("Digite o Nome do Aluno: ")
port = float (input("Qual a Nota em Português? "))
mat = float (input("Qual a Nota em Matemática? "))
geo = float(input("Qual a Nota em Geografia? "))
cien = float (input("Qual a Nota em Ciencias? "))
hist = float (input("Qual a Nota em História? "))
soma = (port + mat + geo + cien + hist)/5
print ('A média final de ' + nome_aluno + ' foi {}'.format(soma))
if soma >= 7.5:
    print ("Aluno APROVADO")
elif soma >=5:
    print ("Aluno em RECUPERAÇÃO")
else:
    print ("Aluno REPROVADO")
print ("Obrigado por utilizar nossos serviços.")