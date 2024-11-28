c = d = e = 0
e = int(input("digite o numero:"))
if (e == 0):
    print(1)
else: 
    d = e
    c = 1 
    while(c < e):
        d = d * (e - c)
        c = c + 1
print (d)        
