import os
import time
from flask import request, Flask

primos = Flask(__name__)

@primos.route('/numerosPrimos')
# /numerosPrimos?total=10
def primo():
    qtd_primos = int(request.args.get('total'))
    tempo = time.time()
    numeros_primos = '2'
    qtd_primo = 1
    numero = 3
    while qtd_primo < qtd_primos:
        for i in range(2, numero):
            if numero % i != 0:
                primo = True
            else:
                primo = False
        if primo:
            numeros_primos += f'{str(numero)}\n'
            qtd_primo += 1
        numero += 1
    print(f'\nTempo de execução: {time.time() - tempo:.2f} seg.\n')
    return numeros_primos

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    primos.run(host='0.0.0.0', port=port)