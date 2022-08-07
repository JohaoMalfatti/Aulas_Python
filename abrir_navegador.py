import webbrowser
import time
class abrir_navegador2:
    def abrir_navegador3():
        #Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h Trabalho inicia de 8h as 12'''
        intervalos = 2
        contador = 0
        print('O programa de controle de descanso foi ativado ')

        while contador < intervalos:
            time.sleep(10)
            webbrowser.open('https://www.youtube.com/watch?v=JRVD-pndqY0')
            contador = contador + 1