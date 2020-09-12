import sys
from .signals import Signal
from .util import scrap


def main():
    # le os argumentos passados na invocação do comando
    args = sys.argv[1:]

    # verifica se possui os argumentos obrigatórios
    if len(args) != 2:
        raise Exception("O ativo e o timeframe são obrigatórios - scrapfx EURUSD 5")
    
    # atribuindo o ativo e o timeframe   
    active = args[0]
    timeframe = int(args[1])

    # invocando a função de scrap
    sig = scrap(timeframe, active)

    print(sig.__dict__)

if __name__ == '__main__':
    main()
