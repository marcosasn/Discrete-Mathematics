#funcao calcular(cadeia1, cadeia2, operacao)
#recebe as cadeias e a operacao
#retorna o valor referente a operacao
def calcular(cadeia1, cadeia2, operacao):
	if operacao == "and":
		e = ""
		for i in range(len(cadeia1)):
			e += funcao_e(cadeia1[i], cadeia2[i])
		return e
	elif operacao == "or":
		ou = ""
		for i in range(len(cadeia1)):
			ou += funcao_ou(cadeia1[i], cadeia2[i])
		return ou
	elif operacao == "xor":
		xou = ""
		for i in range(len(cadeia1)):
			xou += funcao_xor(cadeia1[i], cadeia2[i])
		return xou
	elif operacao == "xnor":
		xnou = ""
		for i in range(len(cadeia1)):
			xnou += funcao_xnor(cadeia1[i], cadeia2[i])
		return xnou
	return "erro"

#funcao_e(i, j)
#recebe a parcela um e a parcela dois
#retorna o valor referente a funcao	
def funcao_e(i, j):
	if i == "0" and j == "0":
		return "0"
	elif (i == "0" and j == "1") or (i == "1" and j == "0"):
		return "0"
	return "1"

#funcao_ou(i, j)
#recebe a parcela um e a parcela dois
#retorna o valor referente a funcao	
def funcao_ou(i, j):
	if i == "0" and j == "0":
		return "0"
	elif (i == "0" and j == "1") or (i == "1" and j == "0"):
		return "1"
	return "1"

#funcao_xor(i, j)
#recebe a parcela um e a parcela dois
#retorna o valor referente a funcao	
def funcao_xor(i, j):
	if i == "0" and j == "0":
		return "0"
	elif (i == "0" and j == "1") or (i == "1" and j == "0"):
		return "1"
	return "0"

#funcao_xnor(i, j)
#recebe a parcela um e a parcela dois
#retorna o valor referente a funcao	
def funcao_xnor(i, j):
	if i == "0" and j == "0":
		return "1"
	elif (i == "0" and j == "1") or (i == "1" and j == "0"):
		return "0"
	return "1"
	

cadeia1 = raw_input("cadeia 1: ")
cadeia2 = raw_input("cadeia 2: ")
operacao = raw_input("operacao: ")

print "\n\nsaida: %s" % (calcular(cadeia1, cadeia2, operacao))

