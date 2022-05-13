with open('dna.txt') as d:
    lines=d.readlines()
#for line in lines:
    #print(line)
dna_string=''
for line in lines:
    dna_string+=line.strip()
print(dna_string)
print(len(dna_string))

