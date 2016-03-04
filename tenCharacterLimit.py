f = open("input.txt","r")
terms = f.readlines().splitlines()
f.close()

f = open("output.txt","w")
for character in terms:
    f.write(character[1:10])
    
f.close()