romanos = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XX": 20, "XXX": 30, "XL": 40, 
"L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D":500 , "DC": 600, "DCC": 700,
"DCCC": 800, "CM": 900, "M": 1000, "MM": 2000, "MMM": 3000, "IV": 4000}

arabico = "";
romano = "";

print "Digite 1 para converter de romano para arabico"
print "Digite 2 para converter de arabico pra romano"
opcao = raw_input()
if opcao == "1":
	arabico = int(raw_input("Numero arabico: ")) 
	# percorre o dicionario atraves das chaves
	# retorna o romano correspondente ao arabico
	for i in romanos.keys():
		if romanos[i] == arabico:
			romano = i
	print "Numero romano: %s" % (romano)
	
elif opcao == "2": 
	romano = raw_input("Numero romano: ")
	# percorre o dicionario atraves das chaves
	# retorna o arabico correspondente ao romano
	for i in romanos.keys():
		if i == romano.upper():
			arabico = romanos[i]
	print "Numero arabico: %s" % (arabico)

else:
	print "erro"
