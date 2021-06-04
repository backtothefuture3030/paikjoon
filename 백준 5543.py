burgers = []
sodas = []
j =0 
while j<3:
    j+=1
    burgers.append(int(input()))



i=0
while i<2:
    i+=1
    sodas.append(int(input()))

print(min(burgers)+min(sodas)-50)
