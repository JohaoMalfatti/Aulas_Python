class saida_de_dados_exp12:
    def saida_de_dados_exep13():    
# Função print()

        dia = 19
        mes = 4
        ano = 2018
        nome = 'José'
        sobrenome = 'Silva'
        altura = 1.9

# %s para strings
# %d inteiros
# %f decimais
# sep=`/´ separador por barra



        print('O aluno ' + nome + ' ' + sobrenome)
        print('O aluno', nome, sobrenome)
        print(dia, mes, ano, sep='/')
        print('Aluno %s foi aprovado ' % nome)
        print('Bem vindo %s' % nome)
        print('O aluno %s %s, tem altura igual a %f ' % (nome, sobrenome, altura))
#
# #Funções de conversão
# int('3')
# float('3.14')
# str(2.3)
        print('Aluno ' + nome + ' Tem altura igual a ' + str(altura))

