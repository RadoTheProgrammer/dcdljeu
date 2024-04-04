

import time,random,builtins,mypkg,os,sys
FILE_BS="bs.txt"
#f=open(FILE_BS,"rb")
"""
BS=[]
for b in f.read():
    BS.append(bytes([b]))
f.close()
"""
OPS="+-x/"
NOMBRES_POSSIBLES=(1,2,3,4,5,6,7,8,9,10,25,50,75,100)
def calculate(cn1,op,cn2):
    if op=="+":
        return cn1+cn2
    elif op=="-":
        return cn1-cn2
    elif op in "x*":
        return cn1*cn2
    elif op in "/:":
        try:
            return cn1/cn2
        except ZeroDivisionError:
            return 0
    else:
        raise ValueError("Invalid op :"+str(op))
class Calcul:
    def __init__(self,n1,op,n2):
        self.n1,self.op,self.n2=n1,op,n2
    def calculate(self):
        if self.op=="+":
            return self.n1+self.n2
        elif self.op=="-":
            return self.n1-self.n2
        elif self.op in "x*":
            return self.n1*self.n2
        elif self.op in "/:":
            try:return self.n1/self.n2
            except ZeroDivisionError:return 0
    def __repr__(self):
        return str(self.n1)+self.op+str(self.n2)+"="+str(self.calculate())
equal="="
space=" "
def solve(nombres,nat,printer=True,return_one_solution=False,allow_float=False,avoid_doubles=True,shortest_sol=True):
    try:
        tt=time.time()
        def info(txt):
            tt2=time.time()-tt
            i=int(tt2)
            f=str(tt2-i)
            f=str(int((tt2-i)*1000)).rjust(3,"0")
            print("["+str(i).rjust(2,"0")+"."+f+"] "+txt)

        if not printer:
            info=lambda *args:None
        nts=[]
        if nat in nombres:
            s=str(nat)+"="+str(nat)
            print("Le Compte Est Bon : "+s)
            return [s]
        nombres=sorted(nombres)
        nombres.reverse()
        pistes=[([],nombres)]
        solutions=[]
        npistes=[]
        m_a=nat
        a=1
        add=1
        two=2
        b=2
        while True:
            npistes=[]
            for cals,nbr in pistes:
                #print(nbr)
                if len(nbr)<two:return
                    #return (solutions,nts)
                #print("NBR2")
                for n1 in nbr:
                    #nbr2=nbr.copy()
                    #nbr2.remove(n1)
                    for n2 in nbr:
                        #print("HELLO")
                        if n1<n2:continue
                        nbr3=nbr.copy()
                        nbr3.remove(n2)
                        nbr3.remove(n1)
                        for op in OPS:
                            #cal2=Calcul(n1,op,n2)
                            resultat=calculate(n1,op,n2)
                            if not (allow_float or int(resultat)==resultat):continue
                            resultat=int(resultat)
                            cal=str(n1)+op+str(n2)
                            ncals=cals+[cal]
                            nma=abs(resultat-nat)
                            npistes.append((ncals,nbr3+[resultat]))
                            if nma<=m_a:
                                if nma<m_a:
                                    solutions.clear()
                                    nts.clear()
                                    m_a=nma
                                if resultat not in nts:
                                    nts.append(resultat)
                                if ncals in solutions and avoid_doubles:continue
                                solutions.append(ncals)
                                sncal=space.join(ncals)
                                yield (resultat,ncals)
            if not m_a and shortest_sol:return
                #return (solutions,nts)
            pistes=npistes
            a+=add
    except KeyboardInterrupt as err:
        raise err
        print("KeyboardInterrupt")
        return (solutions,nts)
def generer(n=6,solver=False,printer_solver=True,return_one_solution_solver=False,resoluble=False):
    n25=random.randrange(100)<71
    nondouble=random.randrange(100)<52
    nat=random.randrange(101,1000)

    tentative=0
    while True:
        nombres=[]
        for _ in range(n):
            nombres.append(random.choice(NOMBRES_POSSIBLES))
        if n25==(25 in nombres or 50 in nombres or 75 in nombres or 100 in nombres):
            idx=1
            max_count=1
            Breaker=False
            for nombre in nombres:
                count=nombres.count(nombre)
                if count>1:
                    if nombre>10:
                        Breaker=True
                        break
                    if count>max_count:
                        #nombre
                        #time.sleep(0.1)
                        max_count=count
            if Breaker:continue
            if max_count>2:
                accepted=False
            else:
                accepted=nondouble==(max_count==1)
            if accepted:
                
                if solver:
                    data=solve(nombres,nat,printer_solver,return_one_solution_solver)
                    if resoluble:
                        nat=data[1][0]
                    return (nombres,nat,data)
                return (nombres,nat)
            else:
                pass

        tentative+=1
        if tentative/10==int(tentative/10):
            pass
def demo(times="inf"):

    if times=="inf":times=99999
    n=0
    while n<times:
        while True:
            try:
            #try:
                tirage=input("\nLe tirage de nombres : ")
                if not tirage:break
                tirage=list(map(int,tirage.split(" ")))
                #print("W")
                #print(repr(tirage))
            except Exception:pass
            else:break
        if not tirage:
            
            tirage,nat=generer(6)
            print("Tirage de nombres: "+str(" ".join(map(str,tirage))),"Recherche du nombre: "+str(nat))
            time.sleep(1)
        else:
            while True:
                try:
                    tirage.remove("")
                except:break
            while True:
                try:
                    nat=int(input("Recherche du nombre : "))
                except Exception:pass
                else:break
        tt=time.time()
        print("Solveur en cours...")
        d=solve(tirage,nat)
        print("\nFini en "+str(round(time.time()-tt,3))+" seconde(s), il y a "+str(len(d[0]))+" solutions pour trouver "+" et ".join(map(str,d[1]))+(" (Le Compte est bon)" if d[1]==[nat] else "")+".")
        time.sleep(1)
        n+=1
        #if not while_true:break
def _demo():
        while True:
            try:
            #try:
                tirage=input("\nLe tirage de nombres : ")
                if not tirage:break
                tirage=list(map(int,tirage.split(" ")))
                #print("W")
                #print(repr(tirage))
            except Exception:pass
            else:break
        if not tirage:
            
            tirage,nat=generer(6)
            print("Tirage de nombres: "+str(" ".join(map(str,tirage))),"Recherche du nombre: "+str(nat))
            time.sleep(1)
        else:
            while True:
                try:
                    tirage.remove("")
                except:break
            while True:
                try:
                    nat=int(input("Recherche du nombre : "))
                except Exception:pass
                else:break
        tt=time.time()
        print("Solveur en cours...")
        d=solve(tirage,nat)
        print("\nFini en "+str(round(time.time()-tt,3))+" seconde(s), il y a "+str(len(d[0]))+" solutions pour trouver "+" et ".join(map(str,d[1]))+(" (Le Compte est bon)" if d[1]==[nat] else "")+".")
        time.sleep(1)
def ceb_to_bytes(ceb,file=None):
    bceb=b""
    pair=[]
    nbr_pairs=0
    ceb=(list(ceb[0]),ceb[1],ceb[2])
    nombres=ceb[0].copy()
    for nombre in nombres:
        idn=NOMBRES_POSSIBLES.index(nombre)
        pair.append(idn)
        #print(idn)
        if len(pair)==2:
            #print(pair)
            ids=pair[0]*len(NOMBRES_POSSIBLES)+pair[1]
            #print(ids)
            bceb+=BS[ids]
            nbr_pairs+=1
            pair.clear()
    assert nbr_pairs==3
    ids=ceb[1]-101
    pair=[int(ids/30)]
    pair.append(ids-pair[0]*30)
    bceb+=BS[pair[0]]+BS[pair[1]]
    #calcode=[]
    #nombres=ceb[0].copy()
    for calcul in ceb[2]:
        calcul,reponse=calcul.split("=")
        reponse=int(reponse)
        for signe in OPS:
            if signe in calcul:
                bsigne=signe
                break
        cn1,cn2=calcul.split(bsigne)
        cm1=nombres.index(int(cn1))
        del nombres[cm1]
        cm2=nombres.index(int(cn2))
        del nombres[cm2]
        nombres.append(calculate(int(cn1),bsigne,int(cn2)))
        #print(nombres)
        cc=(cm1,OPS.index(signe),cm2)
        code=cc[0]*20+cc[1]*5+cc[2]
        bceb+=BS[code]
    try:
        nceb=bytes_to_ceb(bceb)
    except Exception as err:
        print(err,file=sys.stderr)
    else:
        if ceb!=nceb:
            print("ERROR ceb:",ceb,"nceb:",nceb,file=sys.stderr)
                
        return bceb
    return b
def cebs_to_print(fichier_exercices,fichier_corrige,cebs_or_nbr_cebs=3,n=6,solver=True,resoluble=True):
    cebs=cebs_or_nbr_cebs
    if not isinstance(cebs,(list,tuple)):
        new_cebs=[]
        for id in range(cebs):
            print(str(id)+"/"+str(cebs))
            #print("n",n,"solver",solver)
            data=generer(n,solver,False,True,resoluble)
            new_cebs.append(data)
            #print("wwwww")
        cebs=new_cebs
    print("Construction du fichier")
    txt_debut=" "*41+"Prénom:{}\n\n\n"
    txt_debut,txt_debut_corr=txt_debut.format("________"),txt_debut.format("Corrigé")
    espace_page="\n"*3
    pages=[]
    pages_corr=[]
    idx=0
    Breaker=False
    while True:
        page=txt_debut
        page_corr=txt_debut_corr
        for _ in range(12):
            try:
                ceb=cebs[idx]
            except:
                break
            idx2=str(idx+1)
            txt_tirage="0"*(len(str(len(cebs)))-len(idx2))+idx2+") "+" ".join(map(str,ceb[0]))+" -> "+str(ceb[1])+"\n{}\n\n\n"
            page+=txt_tirage.format("_"*56)
            print(ceb[2][0][0])
            page_corr+=txt_tirage.format(" ".join(ceb[2][0][0] if len(ceb)>2 else []))
            idx+=1
        pages.append(page)
        pages_corr.append(page_corr)
        if idx>=len(cebs):break
    f=open(fichier_exercices,"w")
    f.write(espace_page.join(pages))
    f.close()
    f=open(fichier_corrige,"w")
    f.write(espace_page.join(pages_corr))
    f.close()
    mypkg.open_file_with_browser(fichier_exercices)
    mypkg.open_file_with_browser(fichier_corrige)
    time.sleep(1)
    os.remove(fichier_exercices)
    os.remove(fichier_corrige)
def bytes_to_ceb(ceb):
    b=ceb
    bs=list(map(lambda b:b[0],BS))
    nombres=[]
    idx=0
    for _ in range(3):
        idx_nn=bs.index(b[idx])
        n1=int(idx_nn/14)
        n2=idx_nn-(n1*14)
        idx+=1
        nombres.append(NOMBRES_POSSIBLES[n1])
        nombres.append(NOMBRES_POSSIBLES[n2])
    n1=bs.index(b[idx])
    idx+=1
    n2=bs.index(b[idx])
    idx+=1
    nat=n1*30+n2+101
    solution=[]
    nombres_copy=nombres.copy()
    while idx<len(b):
        #print("AAA")
        idx_nn=bs.index(b[idx])
        cm1=int(idx_nn/20)
        opm=int((idx_nn-cm1*20)/5)
        cm2=idx_nn-(cm1*20+opm*5)
        cn1=nombres_copy.pop(cm1)
        op=OPS[opm]
        cn2=nombres_copy.pop(cm2)
        resultat=int(calculate(cn1,op,cn2))
        nombres_copy.append(resultat)
        idx+=1
        solution.append(str(cn1)+op+str(cn2)+"="+str(resultat))
    return (nombres,nat,solution)
def generer_bytes(nbr_de_cebs=1000,file=None,resoluble=True):
    cebs=[]
    b=b""
    for idx in range(nbr_de_cebs):
        print(str(idx)+"/"+str(nbr_de_cebs))
        data=generer(6,True,False,True,resoluble=resoluble)
        #print(data[2][0])
        cebs.append((data[0],data[1],data[2][0][0]))
        b+=ceb_to_bytes(cebs[-1])+BS[-1]
    if file:
        f=open(file,"wb")
        f.write(b)
        f.close()
        mypkg.open_file_with_browser(file)
        if not input("Tapez Enter pour supprimer le fichier, tapez un texte pour le garder"):

            os.remove(file)
        #print("w")
    #print(cebs)
    #print(cebs)
    return (b,cebs)

#id=str(random.randrange(1000))
#cebs_to_print("ceb_ex"+id+".txt","ceb_corr"+id+".txt",24)
def test():
    tt=time.time()
    g=generer()
    print(g)
    for result in solve(*g):print(result)
    print(time.time()-tt)
#tt=time.time()
def atest():
    tt=time.time()
    try:
        for result in solve([8, 10, 75, 5, 100, 3],646):pass
    except Exception as err:raise err
    finally:
        print(time.time()-tt)

"""
for a in range(30):
    tt=time.time()
    for result in solve([8, 10, 75, 5, 100, 3],646):pass
    print(str(a)+": "+str(time.time()-tt))
while True:
    input()
    test()
"""
atest()
