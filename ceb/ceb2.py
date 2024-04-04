from mypkg import timetake
id=0
OPS="+-*/"

def ev(n1,op,n2):
    if op is "+":n=n1+n2
    elif op is "-":n=n1-n2
    elif op is "*":n=n1*n2
    elif op is "/":
        if n2==0:n=0
        else:
            n=n1/n2

def solve(nombres,nat):
    global pdp
    pdp=[]
    #if 1:


    def getpiste():
        for piste in pistes:
            #print(piste)
            for i1 in r:
                #pdp.append(0)
                n1,e1=piste[i1]
                #n1,e1=piste[i1]
                piste1=piste.copy()
                del piste1[i1]
                for i2 in rgs[i1]:
                    
                    n2,e2=piste[i2]
                    piste2=piste1.copy()
                    del piste2[i2]
                    for op in OPS:
                        #pdp.append(0)
                        
                        if op is "+":n=n1+n2
                        elif op is "-":
                            n=n1-n2
                        elif op is "*":n=n1*n2
                        elif op is "/":
                            if n2==0:n=0
                            else:
                                n=n1/n2
                        
                        #n=ev(n1,op,n2)
                        e="(%s%s%s)"%(e1,op,e2)
                        if n>nat:
                            solutions.append("%s=%s"%(e,int(n) if isinstance(n,float) and not n.is_integer() else n))
                            
                            #if l==2:
                            #    print(sol)
                        else:pass
                            #piste3=[(n if n==i1 else piste[k]) for k in t if k!=i2]
                            #piste3=piste2.copy()
                            #piste3.append((n,e))
                        npistes.append(piste2+[(n,e)])
                            #npistes.append([((n,e) if k==i1 else piste[k]) for k in t if k!=i2])

    global p
    #piste=set()
    #for nombre in nombres:
    #    add(piste,nombre,str(nombre))
    #print(piste)
    pistes=[[(n,n) for n in sorted(nombres)]]
    #idx=0
    solutions=[]
    rgs=tuple((tuple(range(n)) for n in range(len(nombres)+1)))
    #for n in range(len(nombres)+1):

    #print(rgs)
    #oo
    for l in range(len(nombres),1,-1):
        #print(l)
        r=tuple(range(1,l))
        t=tuple(range(l))
        npistes=[]
        #for piste in pistes:
        #    getpiste()
        getpiste()
        pistes=npistes
    return solutions
#timetake(lambda:solve((1,2,3,4,5,6),7))
#timetake(lambda:solve((5,100,4,3,7,75),600))
timetake(lambda:solve((5,6,7,8,9,100),(99999999999999999)))            
