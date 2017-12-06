# -*- coding: utf-8 -*-

import sys
import random

NUM_TESTS = 10
NUM_TESTS_TOTAIS = 10

def createCSV(nameCSV, numTests, results):
    csv = open(nameCSV, "a")
    csv.write(str(numTests)+","+str(results)+"\n")

def main():
    print(".::::: Capítulo 01 - Exercício 09 :::::.\n")
    print("----------------------------------------\n")

    numTests = NUM_TESTS
    numTotalTests = NUM_TESTS_TOTAIS
    createCSV("cap01_exer09.csv", "Número de Testes", "Resultados")
    
    i = 0
    while i in range(numTotalTests):
        j = 0
        numCoPrimos = 0
        while j in range(numTests):
            a = random.randint(1,numTests)
            b = random.randint(1,numTests)
    
            mdc = a
            while (a % mdc != 0) or (b % mdc != 0): 
                mdc = mdc - 1

            if mdc == 1:
                numCoPrimos += 1;

            j += 1

        results = float(numCoPrimos)/float(numTests)    
        createCSV("cap01_exer09.csv", numTests, results)
        numTests *= 10
        i += 1

main()