from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pokedex():
    if request.method == 'POST':

        poke = request.form.get('poke').lower()

        url = f'https://pokeapi.co/api/v2/pokemon/{poke}'
        response = requests.get(url)
        data = json.loads(response.text)
        poke_types = []
        try:
           for item in data['types']:
        # Se o pokemon tiver mais de um tipo é adicionado na lista
            poke_types.append(item['type']['name'])

            poke_name = data['name']
            poke_number = data['id']
            poke_img = data['sprites']['other']['official-artwork']['front_default']
        except:
            poke_types.append('nenhum')
            poke_name = 'não encontrado'
            poke_number = 'não encontrado'
            poke_img = ''
        return render_template('pokemon.html', poke=poke_name, numero=poke_number, tipo=poke_types, image=poke_img)
    else:
        return render_template('pokemon.html')


if __name__ == '__main__':
    app.run(debug=True)
