import requests
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

ACCESS_TOKEN = 'vk1.a.hu2r5omDJ_HzOsoypSNq4HQiO7y0jYnEGpc35ZI-FVvJ4fOPkfvTHUSaIywtASiv9DSVFYU00CGd1PYlPaezmIjduhBIFPdcOhh9cT76mWkYvFGi8lPr0SnZmXTrAFw-Bszeu7ipRZB6EVR1qBiKTk14n_KGNxG-zhaJPHvfULfK9CYGoWnaVwG9JY4NbNc5a-j09-j9UOw_tlScA3r3wQ'


@app.route('/')
def index():
    return send_from_directory('', 'index.html')


@app.route('/search')
def search():
    query = request.args.get('q', '')  # Получаем ключевое слово из URL параметра
    sort_order = request.args.get('sort', 'none')  # Получаем порядок сортировки
    params = {
        'access_token': ACCESS_TOKEN,
        'v': '5.131',
        'q': query,
        'count': 100
    }

    response = requests.get('https://api.vk.com/method/newsfeed.search', params=params)
    data = response.json()  # Преобразуем ответ в JSON

    # Для отладки выведем результат в консоль
    print(data)

    return jsonify(data)  # Возвращаем JSON-ответ


if __name__ == '__main__':
    app.run(debug=True)