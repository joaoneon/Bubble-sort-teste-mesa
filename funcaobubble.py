def bubble (l1):
    n=0
    sai = 0
    troca = 0
    tamanho = len(l1)
    
    while tamanho > 1 and n < tamanho and sai == 0:  
        if l1[n] > l1[n+1]:        
            x = l1[n+1]
            l1[n+1] = l1[n]        
            l1[n] = x        
            troca = 1
        n = n+1    
        if n >= tamanho - 1:               
            n= 0       
            if troca == 0:            
                sai = 1            
            troca = 0
    return l1

items=[]
i=0
while 1:
    i+=1
    item=input('Enter item %d: '%i)
    if item=='':
         break
    items.append(int(item))


print (bubble(items))       
    
     