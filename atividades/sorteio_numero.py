import random
class sorteio_numero2:
    def sorteio_numero3():
        chute = 0
        chances = 5
        tentativas = 1
        jogador = ''
        # sistema sorteará um número entre 1 e 100
        numero_secreto = random.randint(1, 100)

        print('#################################################')
        print('Bem vindo ao jogo de advinha')
        print('Você terá sete chances para adivinhar o número')
        print('#################################################')

        # programa solitica o nome do jogador
        jogador = input('Digite seu nome: ')
        print('Chute um número entre 1 e 100')
        
        while tentativas <= 5:
            chute= int(input('Digite o número: '))
            if chute < numero_secreto:
                print('Você errou. Seu número é menor que o sorteado,'' tente novamente.)')
                print('Tentativa %d de %d' % (tentativas, chances))
            elif chute == numero_secreto:
                print('PARABÉNS!!!!!', jogador)
                print('Você acertou com %d tentativcas' % tentativas)
                tentativas = 5
            else:
                print('Você errou, Seu número é maior que o sorteado,'' tente novamente')
                print('Tentativa %d de %d' % (tentativas, chances))
            if tentativas == 4:
                print('Última tentativa')
            elif tentativas == 5:
                print('### Fim de jogo Numero sorteado %d ###' % (numero_secreto) )
            tentativas = tentativas + 1
        
        
        