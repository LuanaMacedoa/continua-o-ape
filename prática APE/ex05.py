cont=0
for i in range(6):
    a = int(input('Digite o Valor do lado a: '))
    b = int(input('Digite o Valor do lado b: '))
    c = int(input('Digite o Valor do lado c: '))
    
    if a<b+c and b<a+c and c<a+b:
        cont=cont+1
print(f'{cont} medidas foram validas')