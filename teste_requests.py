import requests

# GET Avaliacoes

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de resgistros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta pagina
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultado
# print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultado
# print(avaliacoes.json()['results'][-1])

# Acessando o nome da ultima pessoa que fez a avaliação
#print((avaliacoes.json()['results'][-1]['nome']))


# GET Avaliacao

# avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/61/')

# print(avaliacao.json())


# GET Cursos

headers = {'Authorization': 'Token 051c2a7d736bfed0d03ebe0698baf4b937cb7812'}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
