# Algoritmo in Python
# controlla che le parentesi siano bilanciate

#programmo la funzione di controllo di una stringa(espressione) da noi passata 
def check(str):
	
	aperte = tuple('({[') #definisco i grafemi che andremo ad analizzare, par.aperte
	chiuse = tuple(')}]') #definisco... par. chiuse
	mappa = dict(zip(aperte, chiuse)) #combino i valori in un dizionario
	stack = [] #useremo una lista come stack che dovrà essere sempre vuota nel caso di par.bilanciate

	for i in str: #un semplice ciclo for per iterare su tutta la stringa da noi passata
		if i in aperte: 
			stack.append(mappa[i])
		elif i in chiuse:
			if not stack or i != stack.pop():
				return "Non bilanciate"
	if not stack:
		return "Bilanciate"
	else:
		return "Non bilanciate"
    #se nello stack non viene rinvenuto nulla, le parentesi sono bilanciate



'''Ora un po' di espressioni prese dal pdf della traccia e alla fine viene assegnato
input all'utente che può testare le sue espressioni'''


espressione1='(4+(2*2)-(2+(1+10)))'
espressione2='(4+(2*2)-(2+(1+10))'
espressione3='(4+{2*2}-(2+[1+10]))'
espressione4='(4+{2*2)-(2+[1+10]))'

espressione5=input('Oltre quelle del pdf tocca a te. \nDigita la tua espressione per il check: ')

print(check(espressione1)); print(check(espressione2)); print(check(espressione3)); print(check(espressione4))
print("L'espressione da te digitata", espressione5, '\nrisulta: ',check(espressione5))



