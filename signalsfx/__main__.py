import sys
import webview
from signalsfx.signals import Signal
from signalsfx.util import scrap
import click

class Api:
    def search_active(self, active, timeframe):
        """
        {
            "_active": "EURUSD",
            "_price": "1.3423"
        }
        """
        return scrap(timeframe, active).__dict__



def start_desktop():
    api = Api()
    webview.create_window('SignalsFX', './static/index.html', width=400, height=550, resizable=False, js_api=api)
    webview.start(debug=True)

# python3 signalsfx --active EUR/USD --timeframe 1
@click.command()
@click.option('--active', help='Nome do Ativo: Ex.: EUR/USD USD/JPY')
@click.option('--timeframe', help='O timeframe que deseja analisar: EX.: 1 5 15 30 60 ')
def main(active, timeframe):

    if not active and not timeframe:
        start_desktop()

    # invocando a função de scrap
    sig = scrap(timeframe, active)
    print(sig.__dict__)

if __name__ == '__main__':
    main()