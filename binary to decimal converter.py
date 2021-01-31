n_org=int(input("Enter Bin :  "))
n_=str(n_org)
dec,n=0,n_[::-1]
for i in range(len(str(n))) :
    dec+=(int(n[i])*(2**i))
print("decimal :",dec)    
    
