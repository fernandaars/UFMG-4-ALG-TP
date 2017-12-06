# -*- coding: utf-8 -*-

import sys
import random

NUM_TESTS = 1000
NUM_RANGE = 100

def createCSV(nameCSV, numTests, results):
    csv = open(nameCSV, "a")
    csv.write(str(numTests)+","+str(results)+"\n")

def greatestCommonDivisor(a, b):
    if a == 0: return b;
    if b == 0: return a;
    return greatestCommonDivisor(a, a%b);

def main():
    print(".::::: Capítulo 01 - Exercício 08 :::::.\n")
    print("----------------------------------------\n")

    numTests = NUM_TESTS
    numRange = NUM_RANGE
    createCSV("cap01_exer08.csv", "Número de Testes", "Relação entre Falhas e Acertos")
    
    i = 1
    results = 0
    numFailCases = 0
    while i in range(numTests):
        a = random.randint(1,numRange)
        b = random.randint(1,numRange)
        c = random.randint(1,numRange)

        gcd = greatestCommonDivisor(a,b);
        if c%gcd != 0:
            numFailCases += 1
            print("SIM")
        else:
            print("NÃO")


        if(i%100 == 0):
            results = numFailCases - results
            relation = 0 if (numFailCases == 0) else float(numFailCases)/float(i)  
            createCSV("cap01_exer08.csv", i, relation)
            numTests *= 10
        i += 1

main()