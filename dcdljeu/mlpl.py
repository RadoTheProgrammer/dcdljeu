FILE_TLM="tlm_dcdl.txt"
FILE_TLM_SORT="tlm_dcdl_sort.txt"
LETTRES="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTRES_SCRABBLE=list("A"*9+"B"*2+"C"*2+"D"*3+"E"*15+"F"*2+"G"*2+"H"*2+"I"*8+"J"*1+"K"*1+"L"*5+"M"*3+
                      "N"*6+"O"*6+"P"*2+"Q"*1+"R"* 6+"S"*6+"T"*6+"U"*6+"V"*2+"W"*1+"X"*1+"Y"*1+"Z"*1)
VOYELLES="AEIOUY"
BS=[]
ID_BS=[]
FILE_BS="bs.txt"

import time
import random
import os

f=open(FILE_BS,"rb")
for b in f.read():
    BS.append(bytes([b]))
    ID_BS.append(b)
f.close()


def get_tlm():
    """Obtenir la liste des mots"""
    f=open(FILE_TLM)
    mots=f.read().splitlines()
    f.close()
    return mots

def renew_tlm_sort():
    mots=get_tlm()
    f=open(FILE_TLM_SORT,"w")
    f.write(
        "".join(
            map(lambda mot:"\n"+"".join(sorted(mot))+":"+mot,mots)).upper())
    f.close()
    
try:
    f=open(FILE_TLM_SORT)
except:
    renew_tlm_sort()
    
def tlm_to_scratch():
    mots=get_tlm()
    scratch="".join(map(lambda mot:mot.upper()+";",mots))
    print("Texte généré")
    return scratch

def solve(lettres,n=10,Printer=True):
    global mots_trouves,lmot
    tt=time.time()
    def info_with_timer(txt):
        ttt=str(int(round(time.time()-tt,3)*1000))
        ttt=ttt[:-3]+"."+ttt[-3:]
        ttt=("0"*(6-len(ttt)))+ttt      
        print("["+ttt+"] "+txt)
        
    if not Printer:
        info_with_timer=lambda *args:None
    info_with_timer("Tirage: "+lettres)
    mots_trouves=[]
    for _ in range(len(lettres)+1):
        mots_trouves.append([])
    all_lettres=[sorted(lettres.upper())]
    
    #print(all_lettres)
    #new_lettres=[]
    f=open(FILE_TLM_SORT)
    txt=f.read()
    f.close()
    Breaker=False
    max=0
    while True:
        new_lettres=[]
        l=len(all_lettres[0])
        if l+(n-1)<max or not l:
            return (mots_trouves,max)
        info_with_timer("Recherche pour "+str(l)+" lettres...")
        for lettres in all_lettres:
            #if lettres==list("ADEINNOSU"):print("CC")
            #print(list(map(len,all_lettres)))
            idx=0
            while True:
                try:
                    #print(len(lettres))
                    idx=txt.index("\n"+"".join(lettres)+":",idx)+1
                except:
                    break
                else:
                    idx+=len(lettres)+1
                    mot_trouve=txt[idx:txt.index("\n",idx)]
                    lmot=len(mot_trouve)
                    
                    if mot_trouve not in mots_trouves[lmot]:
                        #if lettres==list("ADEINNOSU"):print("NO")
                        if lmot>max:
                            max=lmot
                        info_with_timer(str(lmot)+" lettres: "+mot_trouve)
                        mots_trouves[lmot].append(mot_trouve)
            a_lettre=""
            for idx in range(len(lettres)):
                lettre=lettres[idx]
                if lettre==a_lettre:
                    continue
                a_lettre=lettre
                lettresc=lettres.copy()
                del lettresc[idx]
                new_lettres.append(lettresc)
            #print(new_lettres)
        #print(new_lettres)
        all_lettres=new_lettres
    print("WW")
    
def demo(n_solver=2,alternes_mlpl_dcdl=False):
    lettres=input("Lettres ?")
    if not lettres:
        lettres=generer()
        print("Lettres:"+lettres)
        time.sleep(1)
    d=solve(lettres,n_solver)
    
def generer(nbr_de_voyelles=5,n=10,solver=False,n_solver=2,Printer_solver=True):
    if nbr_de_voyelles=="random":
        nbr_de_voyelles=random.randrange(3,7)
    #print("nn",n_solver)
    while True:
        tirage=""
        voyelles=0
        Breaker=False
        lsc=LETTRES_SCRABBLE.copy()
        for _ in range(n):
            lettre=lsc.pop(random.randrange(len(lsc)))
            if lettre in VOYELLES:
                voyelles+=1
                if voyelles>nbr_de_voyelles:
                    break
            tirage+=lettre
        if voyelles==nbr_de_voyelles:
            if solver:
                return (tirage,solve(tirage,n_solver,Printer_solver))
            return tirage
        
def generer_bytes(nbr_de_voyelles=5,nbr_de_mlpls=1000,file=None):
    mlpls=[]
    b=b""
    for idx in range(nbr_de_mlpls):
        print(str(idx)+"/"+str(nbr_de_mlpls))
        data=generer(nbr_de_voyelles,solver=True,n_solver=1,Printer_solver=False)
        mlpls.append((data))
        b+=to_scratch(mlpls[-1])+BS[-1]
    if file:
        f=open(file,"wb")
        f.write(b)
        f.close()
        #mypkg.open_file_with_browser(file)
        if not input("Tapez Enter pour supprimer le fichier, tapez un texte pour le garder"):
            os.remove(file)
    return (b,mlpls)

def to_scratch(mlpl,file=None):
    """To turn for scratch"""
    """mlpl_to_bytes(("ABCDEFGHIJ",([[],[],[],[],[],[],[],["FICHAGE"]],7)),"YOUR_FILE.txt")"""
    bs=b''
    lettres=sorted(mlpl[0].upper())
    solutions,max=mlpl[1]
    max-=1
    int1=int(max/5)
    int2=max-int1*5
    max+=1
    bs+=BS[len(LETTRES)*int1+LETTRES.index(lettres[0])]+BS[len(LETTRES)*int2+LETTRES.index(lettres[1])]
    for idx in range(2,len(lettres)):
        bs+=BS[LETTRES.index(lettres[idx])]
    #tirages_mc=[]
    mots=[]
    for mot in solutions[max]:
        mot=sorted(mot)
        if mot in mots:
            continue
        mots.append(mot)
        tirage_mc=[]
        lettresc=lettres.copy()
        #print(len(lettresc))
        if max>5:
            for _ in range(len(lettres)-max):
                for idx in range(len(lettresc)):
                    #if idx>=len(mot):
                    #    print("l",len(mot))
                    #    print("Hello")
                    #    break
                    if idx>=len(mot) or mot[idx]!=lettresc[idx]:
                        #print("Trouvé")
                        del lettresc[idx]
                        tirage_mc.append(idx)
                        break
                        
        else:
            for char in mot:
                idx=lettresc.index(char)
                del lettresc[idx]
                tirage_mc.append(idx)
        b=0
        try:
            b+=tirage_mc[0]
            b+=tirage_mc[1]*10
            b+=tirage_mc[2]*10*9
            b+=tirage_mc[3]*10*9*8
            b+=tirage_mc[4]*10*9*8*7
        except:pass
        #print("b",b)
        b1=int(b/(len(BS)-1))
        b2=b-b1*(len(BS)-1)
        bs+=BS[b1]+BS[b2]
        #print(tirage_mc)
        #tirages_mc.append(tirage_mc)
    if file:
        f=open(file,"wb")
        f.write(bs+BS[-1])
        f.close()
        #mypkg.open_file_with_browser(file)
    return bs

def from_scratch(bs):
    """From scratch to python"""
    f=open(FILE_TLM_SORT)
    tfts=f.read()
    f.close()
    b1=ID_BS.index(bs[0])
    b2=ID_BS.index(bs[1])
    int1=int(b1/len(LETTRES))
    int2=int(b2/len(LETTRES))
    #print(b1)
    max=int1*5+int2+1
    lettres=LETTRES[b1-int1*len(LETTRES)]+LETTRES[b2-int2*len(LETTRES)]
    #print(lettres)
    for idx in range(2,10):
        lettres+=LETTRES[ID_BS.index(bs[idx])]
    lettres=sorted(lettres)
    print(lettres)
    #motsc=[]
    idx=10
    mots=[]
    while True:
        b1=ID_BS.index(bs[idx])
        b2=ID_BS.index(bs[idx+1])
        print("b1",b1,"b2",b2)
        b=b1*(len(BS)-1)+b2
        print("b",b)
        tirage=[]
        fois=10*9*8*7
        tirage.append(int(b/fois))
        print("pt",tirage)
        b-=tirage[-1]*fois
        fois=10*9*8
        tirage.append(int(b/fois))
        b-=tirage[-1]*fois
        fois=10*9
        tirage.append(int(b/fois))
        b-=tirage[-1]*fois
        print("b2",b)
        fois=10
        tirage.append(int(b/fois))
        b-=tirage[-1]*fois
        tirage.append(b)
        tirage.reverse()
        print(tirage)
        idx+=2
        if max>5:
            lettresc=lettres.copy()
            for idxt in range(len(lettres)-max):
                del lettresc[tirage[idxt]]
        else:
            lettrescc=lettres.copy()
            lettresc=[]
            for idxt in range(max):
                lettresc.append(lettrescc.pop(tirage[idxt]))
        smot="".join(lettresc)
        #print("i")
        while True:
            try:
                idxt=tfts.index("\n"+smot+":",idxt)+len(smot)+2
                #print("o")
            except:break
            mot=tfts[idxt:tfts.index("\n",idxt)]
            #print(mot)
            mots.append(mot)
        #print(idx>=len(bs))
        if idx>=len(bs):break
    print(bs)
    solutions=[]
    for _ in range(max):
        solutions.append([])
    solutions.append(mots)
    return ("".join(lettres),(solutions,max))
        #print("YO")
#tt=time.time()
#LETTRES="abcdefghij"
#d=solve(LETTRES,len(LETTRES)-5)
#print("Fin en : "+str(time.time()-tt))
#d=mlpl_to_bytes(("ABCDEFGHIJ",(([],[],[],[],[],[],[],["FICHAGE"]),7)),"f.txt")
