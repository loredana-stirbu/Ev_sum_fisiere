with open('lista_clasei_.txt','rt') as f:
    l=list(f)

with open('lista_clasei_.txt','r') as f:
    with open('rezerva.txt','w') as x:
        for i in f:
            x.write(i)
        x.close()
    f.close()

print('Numar   Nume    Prenume        Nota1   Nota2   Nota3')

for i in l:
    z=i.split()
    nota=((float(z[3])+float(z[4])+float(z[5])))
    media=(nota/3)
    med=(round(media,2))
    z[3]=str(med)
    g=open('medii.txt','a')
    g.write(z[0])
    g.write('\t')
    g.write(z[1])
    g.write('\t')
    g.write(z[2])
    g.write('\t')
    g.write(z[3])
    g.write('\n')
    print(z[0],z[1],z[2],z[3],z[4],z[5],sep='\t')

print('Numar   Nume    Prenume        Media')
with open('medii.txt','rt') as g:
    print(g.read())