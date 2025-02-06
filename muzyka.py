import math


data = open("data.txt", "r")
instance = []
jea = []
#print(-1%4)
for row in data:
	dete = row.split()
	dato = []
	trued = [1]
	mat = []
	for i in range(len(dete)):
		dato.append(int(dete[(i - 1)%5]))
		#trued.append(int(dete[i]))
	for i in range(4):
		dato.append(6 - dato[i+1])
	for i in range(8):
		for j in range(i, 8):
			dato.append((math.sqrt(dato[i+1]*dato[j+1])))
			trued.append(dato[-1])
	trued.append(dato[0])
	#print(len(trued))
	for i in range(len(trued)-1):
		mate = []
		for j in range(len(trued)):
			mate.append((trued[i]*trued[j]))
		mat.append(mate)
	jea.append(trued)
	instance.append(mat)
	#print(mat)

trn = []
for row in instance[0]:
	trm = []
	for dte in row:
		trm.append(0)
	trn.append(trm)
	#print(trm)
#print(trn)
for ply in instance:
	for i in range(len(ply)):
		for j in range(len(ply[i])):
			trn[i][j] += ply[i][j]

	#print(trn[i])
#input()
for i in range(len(trn)):
	rel = trn[i][i]
	for j in range(len(trn[i])):
		trn[i][j] = trn[i][j] / rel
	#print(trn)
	#input()
	for j in range(len(trn)):
		if j != i:
			fak = -trn[j][i]
			for k in range(len(trn[j])):
				trn[j][k] += fak * trn[i][k]
	#	print(trn[j])
	#input()
	#for kle in trn:
	#	print(kle[-1])
print()
dane = []
for kle in trn:
	dane.append(kle[-1])
	print(kle[-1])
input()
err = 0
for j in range(len(jea)):
	print(j)
	print(jea[j][-1])
	los = 0
	for i in range(len(dane)):
		los += jea[j][i] * dane[i]
	print(los)
	print((jea[j][-1] - los) ** 2)
	err += (jea[j][-1] - los) ** 2
	print()
print(err)