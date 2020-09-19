from signalsfx.signals import Signal
import requests

def get_data(timeframe):
    cookies = {
        'geoC': 'BR',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/plain, */*',
        'Sec-Fetch-Dest': 'empty',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://ssltsw.forexprostools.com/index.php?timeframe=900&referer=https://ssltsw.forexprostools.com/index.php?timeframe=300%20%20%20%20%20&selectedTabId=QBS_1',
        'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    }

    params = (
        ('action', 'refresher'),
        ('pairs', '1,2,3,4,5,6,7,8,9,10'),
        ('timeframe', timeframe * 60),
    )

    response = requests.get('https://ssltsw.forexprostools.com/api.php', headers=headers, params=params, cookies=cookies)
    api = response.json()

    return api

def scrap(timeframe, active):
    signals = []

    # le os dados da API
    api = get_data(timeframe)


    # para cada key, criamos um objeto Signal
    for idx, value in api.items():
        if idx != 'time':
            signals.append(Signal(value['summaryName'], value['row']['last'], value['summaryChange'], value['row']['ma'], api['time']))

    """
    signal = None
    for s in signals:
        if s.active == active 
            signal = s
    vs
    [ variavel for variavel in lista <CONDICIONAL>] if variavel.campo == condicao  
    """

    # filtragem
    signal = [s for s in signals if s.active.replace("/","") == active.replace("/","")]
    return signal.pop()