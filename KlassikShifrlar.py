# Sezar shifrlash algoritmi
def shifrlash(key,Matn,n):
    C=""
    for i in Matn:
        C=C+chr((ord(i)+key)%n)
    return C
def deshifrlash(key,C,n):
    M=""
    for i in C:       
        M=M+chr((ord(i)-key+n)%n)            
    return M

M=input("Ochiq matnni kiriting: ")
key=int(input("Kalitni kiriting key="))
n=65535
C=shifrlash(Matn=M,key=key,n=n)
print("C=",C)
DM=deshifrlash(C=C,n=n,key=key)
print("DM=",DM)

