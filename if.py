num = int(input( ":" ))
A=0
B=0
while num >= 1 :
    if num%2 == 0 :
        A+=1
    elif num%2 != 0 :
        B+=1
    num = int(input( ":" ))
print(A,B)

    
