dict = {'_Musica__nome':'henrique',
'_Musica__idade': '21'}



newData = []
for m in dict:
    n = {}
    for chave, valor in m.__dict__.items():
        chave = chave.replace('_Musica__', '')
        n[chave] = valor
    newData.append(n)  

print(dict)
print (newData)