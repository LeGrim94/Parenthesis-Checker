"A cosa serve questo algoritmo?"

La sua funzione principale è di controllare che una espressione aritmetica abbia il giusto numero di parentesi, ovvero che non ci siano errori di formattazione (ad esempio parentesi in più, o mancanti). 
Inoltre presenta come funzionalità aggiuntiva la supervisione che tali parentesi siano appropriamente usate. 

Il codice è scritto in Python 3, opportunamente commentato qualora non fosse chiaro e viene lasciato all'utente
la possibilità di testarlo con una funzione di input.
Viene utilizzata una lista stack, combinata all'uso di un dizionario (ottenuto dalla combinazione dei valori di parentesi aperte e chiuse) sui quali, dopo un processo di iterazione dell'espressione passata alla funzione,
si controlla che lo stack sia vuoto. Nel caso non fosse così vorrebbe dire che ci troviamo in un caso di parentesi non bilanciate e quindi di errore.




