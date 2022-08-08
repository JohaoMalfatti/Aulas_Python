class media_aluno2:
    def media_aluno3():
        print("Sisema de media e aprovação rodando")
        nome = input("Digite seu nome")
        meteria = input("Digte o nome da materia")
        print(nome + "Digie suas 4 notas")
        n1 = float(input('Digite Sua primeira Nota '))
        n2 = float(input('Digite Sua segunda Nota '))
        n3 = float(input('Digite Sua terceira Nota '))
        n4 = float(input('Digite Sua quarta Nota '))
        media = (n1+n2+n3+n4) / 4 
        if media < 7:
            print('Aluno %s, você foi REPROVADO. Sua média em %s foi de %.2f.' % (nome, meteria, media))
        else:
            print('Parabéns!!!!')
            print('Aluno %s, você foi APROVADO. Sua média em %s foi %.2f.'% (nome, meteria, media))
            