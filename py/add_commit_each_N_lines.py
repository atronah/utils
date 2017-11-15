import sys

with open(sys.argv[1], 'r', encoding='utf-8') as inp, open('out_' + sys.argv[1], 'w', encoding='utf-8') as out:
    row = 0
    for line in inp:
        if (row % 5000 == 0): 
            out.write('commit;\n')
            print(row)
        out.write(line)
        row += 1
        
        