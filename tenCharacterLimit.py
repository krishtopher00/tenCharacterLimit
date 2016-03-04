f = open("input.txt","r")
terms = f.read().splitlines()
f.close()

f = open("output.txt","w")
for character in terms:
    f.write(character[0:10] + "\n")
    
f.close()