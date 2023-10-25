def clause(s):
    L = s.split()
    return [int(v) for v in L[:-1]]

def parseur(nom):
    with open(nom) as f:
        F = []
        n = 0
        for ligne in f:
            if ligne[0] == 'c': continue
            if ligne[0] == 'p':
                L = ligne.split()
                n = int(L[-2])
            else: 
                F.append(clause(ligne))
    return F, n

def affiche(F):
    s=''
    for j in range(0,len(F)):
        C=F[j]
        s=s+'('
        for i in range(0,len(C)):
            if C[i]<0:
                s=s+'Non'
            s=s+'x'+str(abs(C[i]))
            if i==len(C)-1:
                s=s+')'
            else:    
                s=s+' \/ '
        if j!=len(F)-1:
            s=s+' /\ '
    return s

################################################################

def valide(F, A):
    # first = F[0][0]
    # second = F[0][1]
    # val_first=A[abs(first)-1]
    # val_second=A[abs(second)-1]
    i=0
    valeurs_ou = 1
    while valeurs_ou and i<len(F):
        first = F[i][0]
        second = F[i][1]
        val_first=A[abs(first)-1]
        val_second=A[abs(second)-1]
        if first<0:
            val_first = -1*val_first
        if second<0:
            val_second = -1*val_second
        if val_first==1 or val_second==1:
            valeurs_ou = 1
        else:
            return False
        i+=1

    return True

def valide(F, A):
    for i in range(0,len(F)):
        ok=False
        for j in range(0,len(F[i])): 
            if F[i][j]*A[abs(F[i][j])-1]>0:
                ok=True
            if ok==False :
                return False 
    return True

################################################################

def aff_suivante(A):    
    i = 0
    n=len(A)
    while i<len(A) and A[i]==1:
        A[i]=-1
        i+=1
    if i==n:
        return "Fin"
    A[i]=1
    return A

def test_aff_suivante(n):
    #
    # A COMPLETER       
    #
    return None
        
#########################################################################

def sat_exhau(F, n):
    A = [-1] * n
    i=0
    while not(valide(F,A)):
        A = aff_suivante(A)
        i+=1
        if A == None:
            return "insat"
    return A

def elimination(F, n, b):
#    "Formule psi = F(x_1, …, x_{n-1}, b)"
    psi=[]
    return psi

def sat_backtrack(F, n):

    return None

###############################################################################

print("-------------------------------------------------------")
Fichier="cnf/cnf/simple_v3_c2.cnf"
print("Formule du fichier: "+Fichier)
F,n=parseur(Fichier)
print("Récupérée sous forme de tableau: ",F)
print("Nombre de variables: ",n)
print("Formule SAT: ",affiche(F).encode('utf-8'))
print("-------------------------------------------------------")
print(valide(F, [-1,-1,-1]))
print(valide(F, [-1,-1,1]))
#print("-------------------------------------------------------")
# print(test_aff_suivante(4))
# print("-------------------------------------------------------")
# print(sat_exhau(F, n))
# print(sat_backtrack(F, n))
# try:
#     print(valide(F,[False,False,True]))
# except Exception as e:
#     print(e)


# A=[-1,-1,-1,-1]
# for i in range(2**len(A)-1):
#     print(aff_suivante(A))

print(sat_exhau(F,n))