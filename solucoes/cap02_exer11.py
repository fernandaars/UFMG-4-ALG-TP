# -*- coding: utf-8 -*-

import sys
import random

def createCSV(nameCSV, numTests, results):
    csv = open(nameCSV, "a")
    csv.write(str(numTests)+","+str(results)+"\n")

def main():
    print(".::::: Capítulo 02 - Exercício 11 :::::.\n")
    print("----------------------------------------\n")

    numTotalTests = 5000
    createCSV("cap02_exer11.csv", "Intervalo", "Total de Números Altamente Compostos")
    
    numAltCompostos = 0
    maiorDivisor = 1
    results = 0
    i = 0

    while i in range(numTotalTests):
        j = 1
        numDivisores = 0;
        while j in range(i):
            if i%j == 0:
                numDivisores += 1
            j += 1

        if(numDivisores > maiorDivisor):
            maiorDivisor = numDivisores
            numAltCompostos += 1
            print(i)

        if(i%100 == 0):
            results -= numAltCompostos     
            createCSV("cap01_exer09.csv", i, results)
            
        i += 1

main()