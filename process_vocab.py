import json
vocab = []
lines = []
with open('vocab') as f:
    cnt = 0
    for line in f:
        lines.append(line.strip())

cnt = 0
for index, line in enumerate(lines):
    if line.encode('UTF-8').isalpha(): 
        #vocab.append("{" + 'id: {}, word: "{}", definition: "{}"'.format(cnt, line, lines[index+1]) + "}")
        vocab.append({"id": cnt, "word": line, "definition": lines[index+1]})
        cnt += 1

for line in vocab:
    print(line)
'''
with open('gre_vocab.txt', 'w') as f:
    f.write("[")
    for line in vocab:
        f.write(line + ',')
    f.write("]")'''

j = json.dumps(vocab, ensure_ascii=False, indent=2)
with open('gre_vocab.json', 'w') as f:
    f.write(j)
