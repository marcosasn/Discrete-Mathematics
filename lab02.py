#funcao calcular(cadeia1, cadeia2, operacao)
#recebe as cadeias e a operacao
#retorna o valor referente a operacao
def calcular(cadeia1, cadeia2, operacao):
	if operacao == "+":
		print binarioParaDecimal(cadeia1)
		print binarioParaDecimal(cadeia2)
		print binarioParaDecimal(cadeia1) + binarioParaDecimal(cadeia2)
		
		soma = binarioParaDecimal(cadeia1) + binarioParaDecimal(cadeia2)
		
		if (soma > 127):
			return "overflow"
		return "%08d" % int(decimalParaBinario(soma))
		
	elif operacao == "-":
		print binarioParaDecimal(cadeia1)
		print binarioParaDecimal(cadeia2)
		print complementode2(cadeia2)
		print binarioParaDecimal(cadeia1) + complementode2(cadeia2)

		subtracao = binarioParaDecimal(cadeia1) + complementode2(cadeia2)
		
		if (subtracao < -126):
			return "overflow"
		return "%08d" % int(decimalParaBinario(subtracao))
		
	return "erro"

#funcao complementode2(cadeia2)
#recebe a cadeia2
#retorna o valor decimal referente ao complemento de 2
def complementode2(cadeia2):
	complementode2 = ""
	for i in range(len(cadeia2)):
		if cadeia2[i] == "0":
			complementode2 += "1"
		else:
			complementode2 += "0"				
	return binarioParaDecimal(complementode2) + 1

#funcao binarioParaDecimal(binario)
#recebe o binario
#retorna o decimal referente a conversao
def binarioParaDecimal(binario):
	cont = 0
	decimal = 0
	for i in range(len(binario)-1,-1,-1):
		if binario[i] == "1":
			decimal += 1 * (2**cont)
		cont += 1 
	return decimal

#funcao decimalParaBinario(decimal)
#recebe o decimal
#retorna o binario referente a conversao
def decimalParaBinario(decimal):
	binario = ""
	while decimal > 0:
		binario = "%d%s" % (decimal % 2,binario)
		decimal /= 2
	return binario
	
operacao = raw_input("operacao: ")
cadeia1 = raw_input("cadeia1: ")
cadeia2 = raw_input("cadeia2: ")

print calcular(cadeia1, cadeia2, operacao)

