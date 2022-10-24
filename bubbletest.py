l1 = [20, 15, 23, 40 , 33, 3 , 5, 8, 12, 1]
n=0
#n utilizado como indice para posição na lista
sai = 0
#var sai utilizado na função while como break
troca = 0
tamanho = len(l1)
#var tamanho para salvar o valor da length da lista1

while tamanho > 1 and n < tamanho and sai == 0:
    #if bloco principal, onde iremos iterar pela lista e fazer as trocas de posição index, maior pelo menor
    if l1[n] > l1[n+1]:
        #Se a condição acima, onde o index acima é maior que o index inferior, a variavel X abaixo, ira salvar o valor do index maior e inverteremos dentro da função o valor
        x = l1[n+1]
        l1[n+1] = l1[n]
        #acima ocorreu a atribuição do valor de index maior para o valor de index menor.
        l1[n] = x
        #acima ocorreu a atribuição do valor guardado em x, para o index menor da questão.
        troca = 1
    n = n+1    
    if n >= tamanho - 1:
        #aqui resetamos a função para iterar novamenter por todos os itens da lista       
        n= 0       
        if troca == 0:
            #esta condição se aplica quando após todas as iterações não houver troca, o valor de sai, torna-se 1, dando break na função while
            sai = 1            
        troca = 0
        #a troca 0 sempre tem que ocorrer, toda vez que eu percorrer toda a lista
    
print (l1)     
