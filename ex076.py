print('->' * 6, 'ESTATÍSTICAS', '<-' * 6)
pessoas = list()
dicionario = dict()
soma = media = 0
mulheres = list()
while True:
    dicionario['nome'] = str(input('digite um nome: '))
    while True:
        dicionario['sexo'] = str(input('digite o sexo: ')).upper().strip()[0]
        if dicionario['sexo'] in 'MF':
            break
        print('resposta inválida!')
    dicionario['idade'] = int(input('digite a idade: '))
    if dicionario['sexo'] in 'F':
        mulheres.append(dicionario.copy())
    soma += dicionario['idade']
    pessoas.append(dicionario.copy())
    dicionario.clear()
    print('=-=-' * 6)
    while True:
        res = str(input('quer continuar? ')).lower().strip()[0]
        if res in 'sn':
            break
        print('resposta inválida.')
    if res in 'n':
        break
media += soma / len(pessoas)
print('---' * 10)
print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'a média de idade do grupo é {media:.0f}')
print('---' * 10)
print('Mulheres cadastradas:')
print()
for m in mulheres:
    print(f'nome: {m["nome"]}')
    print(f'sexo: {m["sexo"]}')
    print(f'idade: {m["idade"]}')
    print()
print('---' * 10)
print("Pessoas com idade acima da média:")
print()
for p in pessoas:
    if p['idade'] > media:
        print(f'nome: {p["nome"]}')
        print(f'sexo: {p["sexo"]}')
        print(f'idade: {p["idade"]}')
        print()
