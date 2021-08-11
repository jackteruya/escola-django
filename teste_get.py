import requests

headers = {'Authorization': 'Token 051c2a7d736bfed0d03ebe0698baf4b937cb7812'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

assert resultado.status_code == 200
