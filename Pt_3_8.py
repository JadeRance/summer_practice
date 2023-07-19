alphabet = {}
letter = lambda x: chr(1040+x)
Alphabet = {letter(x): x+1 for x in range(32)}
alphabet = {letter(x+32): x+1 for x in range(32)}
Alphabet.update(alphabet)
print(Alphabet)