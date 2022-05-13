with open('dna.txt') as t:
    content=t.read()
print(content.upper().rstrip())