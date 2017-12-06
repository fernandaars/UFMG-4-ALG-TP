# -*- coding: utf-8 -*-

from math import sqrt

def fermat(n):
	x = int(sqrt(n))
	if x*x == n:
		return int(x),int(x)

	while x in range((n+1)/2):
		x += 1
		y = sqrt(x*x - n)

		if y - int(y) == 0:
			return int(x+y), int(x-y)
	return 1,int(n)

def createCSV(nameCSV, numTests, results):
    csv = open(nameCSV, "a")
    csv.write(str(numTests)+","+str(results)+"\n")

def main():
    print(".::::: Capítulo 02 - Exercício 12 :::::.\n")
    print("----------------------------------------\n")

    numTotalTests = pow(2,32)
    createCSV("cap02_exer12.csv", "Intervalo", "Número de Primos")
    
    numPrimos = 0
    results = 0
    i = 0

    while i in xrange(numTotalTests):
    	if(i%2 != 0):
        	a,b = fermat(i)

        	if(a == i) and (b == 1):
        		numPrimos = numPrimos + 1

        if(i%10 == 0):
        	results = numPrimos
        	createCSV("cap02_exer12.csv", i, results)
            
        i += 1

main()