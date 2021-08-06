import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(nota)

# id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].id')
# print(id)


# Todos os nomes das pessoas que avaliaram o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)

# Todos os avaliacoes das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)
