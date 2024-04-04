id=0
OPS="+-*/"
def add(piste,n,e):
    global id
    piste.add((n,e,id))
    id+=1
def solve(nombres,nat):
    piste=set()
    for nombre in nombres:
        add(piste,nombre,str(nombre))
    print(piste)
    pistes=[piste]
    idx=0
    solutions=[]
    while True:
        piste=pistes[idx]
        idx1=0
        #print(piste)
        for nei1 in piste:
            print(nei1)
            n1,e1,_=nei1
            idx2=1
            piste1=piste.copy()

            piste1.remove(nei1)
            for nei2 in piste:
                if idx2>idx:
                    break
                n2,e2,_=nei2
                piste2=piste.copy()
                piste2.remove(nei2)
                for op in OPS:
                    if op=="+":n=n1+n2
                    elif op=="-":n=n1-n2
                    elif op=="*":n=n1*n2
                    elif op=="/":n=n1/n2
                    #n=func(n1,n2)
                    e="(%s)%s(%s)"%(n1,sym,n2)
                    print(e)
                    if r==nat:
                        print(expr)
                        solutions.append(expr)
                    else:
                        add(piste2,n,e)
                        pistes.append(piste2)
                
                idx2+=1
            idx1+=1

s=solve((1,2,3,4,5,6),7)
                    
