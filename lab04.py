#funcao partesUm(partes)
#recebe o conjunto das partes
#retorna o conjunto das partes inicial
def partesUm(partes):
	for i in range(len(conjunto)):
		if conjunto[i].isdigit():
			partes += "[" + conjunto[i] + "],"
			elementos.append(int(conjunto[i]))
	return partes

#funcao partesDois(partes)
#recebe o conjunto das partes
#retorna o conjunto das partes final
def partesDois(partes):
	for i in range(len(elementos)):
		for j in range(len(elementos)):
			partes += "[" + str(elementos[i]) + "," + str(elementos[j]) + "],"
			
	for i in range(len(elementos)):
		if i == len(elementos)-1:
			partes += str(elementos[i]) + "]]"
		else:
			partes += "[" + str(elementos[i]) + ","
	return partes


print "Digite 1 para conjunto das partes na saida"
print "Digite 2 para o array do conjunto dado"
opcao = raw_input()

if opcao == "1":
	conjunto = raw_input("Conjunto: ")
	partes = "[[],"
	elementos = []
	partes = partesUm(partes)
	print "Conjunto das partes: %s" % partesDois(partes)

elif opcao == "2":
	conjunto = raw_input("Conjunto das partes: ")
	print "Conjunto: %s" % conjunto
	
