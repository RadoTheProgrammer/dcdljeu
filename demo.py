import mlpl, ceb2 as ceb
import time

def demo():
    while True:
        r=None
        
        while True:
            r=input("Lettres/nombres : ")
            if not r:
                try:ism
                except:print("Spécifiez le mode svp")
                else:
                    if ism:r="mlpl"
                    else:r="ceb"
            if r=="mlpl":
                ism=True
                r=mlpl.generer()
                print("Tirage: "+r)
                time.sleep(1)
            elif r=="ceb":
                ism=False
                r,nat=ceb.generer()
                print("Tirage: "+str(r)+", Nombre à trouver:"+str(nat))
                time.sleep(1)
            else:
                try:
                    r=[int(number) for number in r.split(" ")]
                    ism=False
                except:
                    if r.isalpha():ism=True
                    else:r=None
                else:
                    while True:
                        try:
                            nat=int(input("Nombre à trouver : "))
                            break
                        except:pass
            if r:
                print("Solveur en cours...")
                tt=time.time()
                if ism:d=mlpl.solve(r)
                else:d=ceb.solve(r,nat)
                    #raise err
                print("Fini en "+str(round(time.time()-tt,3))+"\n\n")

demo()
