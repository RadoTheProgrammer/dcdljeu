import random,mypkg,os,time
NOMBRES_POSSIBLES=(1,2,3,4,5,6,7,8,9,10,25,50,75,100)
FILE_BS="tt4.txt"
f=open(FILE_BS,"rb")
BS=[]
for b in f.read():
    BS.append(bytes([b]))
f.close()
#f=open("tt3.txt","wb")
#for b in range(32,256):
#    f.write(bytes([b]))
    #BS.append(bytes([b]))
#f.close()
OPS="+-x/"
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
def cebs_to_bytes(cebs,file=None):
    b=b""
    for ceb in cebs:
        pair=[]
        nbr_pairs=0
        nombres=ceb[0]
        for nombre in nombres:
            idn=NOMBRES_POSSIBLES.index(nombre)
            pair.append(idn)
            #print(idn)
            if len(pair)==2:
                ids=pair[0]*len(NOMBRES_POSSIBLES)+pair[1]
                print(ids)
                b+=BS[ids]
                nbr_pairs+=1
                pair.clear()
        assert nbr_pairs==3
        ids=ceb[1]-101
        pair=[int(ids/30)]
        pair.append(ids-pair[0]*30)
        b+=BS[pair[0]]+BS[pair[1]]
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
            print(nombres)
            cc=(cm1,OPS.index(signe),cm2)
            code=cc[0]*20+cc[1]*5+cc[2]
            b+=BS[code]
        b+=BS[-1]
    if file:
        f=open(file,"wb")
        f.write(b)
        f.close()
        mypkg.open_file_with_browser(file)
        time.sleep(0.2)
        os.remove(file)
    return b
#data=cebs_to_bytes(,"test"+str(random.randrange(1000,10000))+".txt")
cebs_to_bytes([([7,2,3,4,5,6], 101, ["7+3=10","10x2=20"])],file="test"+str(random.randrange(1000,10000))+".txt")
#cebs_to_bytes([([7, 5, 25, 50, 1, 2], 652, ['50x7=350', '25-1=24', '350-24=326', '326x2=652'])],file="test1.txt")
