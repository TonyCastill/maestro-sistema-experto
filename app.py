from flask import Flask, render_template, request
from rules import reglas

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        total = 0
        resultados = []

        for i, item in enumerate(reglas):
            cumple = request.form.get(f'cumple_{i}')
            puntos_otorgados = int(request.form.get(f'puntos_{i}', 0))
            retro = request.form.get(f'retro_{i}', '')

            if cumple == 'si':
                puntos = item["valor"]
                retro = "Cumple completamente."
            else:
                puntos = min(puntos_otorgados, item["valor"])

            total += puntos

            resultados.append({
                "criterio": item["criterio"],
                "cumple": cumple,
                "valor": item["valor"],
                "puntos": puntos,
                "retro": retro
            })

        return render_template('index.html', resultados=resultados, total=total, enviado=True, reglas=reglas)

    return render_template('index.html', enviado=False, reglas=reglas)

if __name__ == '__main__':
    app.run(debug=True)