from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    primos = []
    numero = 0

    while len(primos) != 101:
        total = 0
        for n in range(1,numero+1):
            if numero % n == 0:
                total += 1

        if total == 2:
            primos.append(numero)
        numero += 1
    return primos0

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
