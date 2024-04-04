from mypkg import timetake
class Terme:
    def __init__(self, val, expr="", niv=0):
        self.val=val # valeur
        self.expr=expr if expr else str(val) # expression
        self.niv=niv # niveau de priorité pour l’opération à la racine
    def group(self):
        return Terme(self.val, "("+self.expr+")", self.niv)
class Operation:
    def __init__(self, sym, calc, niv, test=None): 
        self.sym=sym      # symbole de l’opération
        self.calc=calc    # fonction de calcul
        self.niv=niv      # niveau de priorité
        self.test=test    # test vérifiant la pertinence de l’opération
    def ev(self, a, b):   # fonction d’évaluation du terme résultat
        if self.test:
            if not self.test(a.val,b.val):
                if self.test(b.val,a.val):
                    a,b=b,a # renversement des opérandes
                else:
                    return None
        # adjonction de parenthèses au besoin
        if a.niv//2 > self.niv//2: 
            a=a.group()
        if 2*(b.niv//2) >= self.niv:
            b=b.group()
        return Terme(self.calc(a.val,b.val), a.expr+self.sym+b.expr, self.niv)
operations = [Operation("+", lambda a,b: a+b, 5),
    Operation("−", lambda a,b: a-b, 4, lambda a,b:a>b),
    Operation("×", lambda a,b:a*b, 3, lambda a,b:a>1 and b>1),
    Operation("/", lambda a,b:a//b, 2, lambda a,b: b>1 and a%b==0)]
def resolution(plaquettes, objectif):
    L=[[Terme(k) for k in sorted(plaquettes, reverse=True)]]
    n=0
    solutions=[]
    while(n<len(L)):
        P=L[n]
        for j in range(len(P)):
            for f in operations:
                for i in range(j):
                    t=f.ev(P[i],P[j])
                    if t:
                        if t.val==objectif:
                            solutions.append(t.expr)
                        else:
                            Q=[(t if k==j else P[k])
                                for k in range(len(P)) if k!=i]
                            L.append(Q)
        n+=1
    return solutions
def resolution2(plaquettes, objectif):
    L=[([Terme(k) for k in sorted(plaquettes, reverse=True)],0)]
    n=0
    solutions=[]
    while(n<len(L)):
        P,debut=L[n]
        for j in range(debut,len(P)):
            for f in operations:
                if P[j].niv//2 != f.niv//2 or P[j].niv > f.niv:
                    for i in range(j):
                        if P[i].niv//2 != f.niv//2 or P[i].niv%2:
                            t=f.ev(P[i],P[j])
                            if t:
                                if t.val==objectif:
                                    solutions.append(t.expr)
                                else:
                                    Q=[(t if k==j else P[k])
                                        for k in range(len(P)) if k!=i]
                                    L.append((Q,j-1))
        n+=1
    return list(set(solutions))
class Resultat:
    def __init__(self, plaquettes, objectif, calculs, solutions, minoration, majoration):
        self.plaquettes=plaquettes
        self.objectif=objectif
        self.calculs=calculs
        self.solutions=solutions
        self.minoration=minoration
        self.majoration=majoration
def resolution3(plaquettes, objectif):
    L=[([Terme(k) for k in sorted(plaquettes, reverse=True)],0)]
    N=1
    n=0
    solutions=[]
    c=0
    minoration = Terme(max(plaquettes))
    majoration = None
    while(n<N):
        P,debut=L[n]
        for j in range(debut,len(P)):
            for f in operations:
                if P[j].niv//2 != f.niv//2 or P[j].niv > f.niv:
                    for i in range(j):
                        if P[i].niv//2 != f.niv//2 or P[i].niv%2:
                            t=f.ev(P[i],P[j])
                            if t:
                                c+=1
                                if t.val==objectif:
                                    solutions.append(t.expr)
                                else:
                                    Q=[(t if k==j else P[k])
                                        for k in range(len(P)) if k!=i]
                                    L.append((Q,j-1))
                                    N+=1
                                    if t.val < objectif:
                                        if minoration.val < t.val:
                                            minoration = t
                                    elif not majoration or majoration.val > t.val:
                                            majoration = t
        n+=1
    return Resultat(plaquettes, objectif, c, list(set(solutions)), minoration, majoration)

#timetake(lambda:resolution3([1,2,3,4,5,6],7))
