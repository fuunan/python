with open('dna2.txt','w+') as t:
    with open('dna.txt') as d:
        lines=d.readlines()
        for line in lines:
            t.write(line)
with open('dna2.txt') as t:
    context=t.read()
print(context.rstrip())