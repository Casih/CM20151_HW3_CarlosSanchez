import os as os

#tener en cuenta que ambos estan haciendo lo mismo... les tocaria comentar alguno de los dos para ver el output.

#con python
with open('Notas.csv',) as infile:
 with open('Notas.dat', 'w+') as outfile:
   for line in infile:
     fields = line.split(',')
     outfile.write('+'.join(fields))


#desde la terminal
os.system("sed 's/,/+/g' Notas.csv > Notas.dat")