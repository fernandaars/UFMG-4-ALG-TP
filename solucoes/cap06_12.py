# -*- coding: utf-8 -*-

import sys
import random
from math import log
from math import pow

NUM_TESTS = 10000
NUM_RANGE = 100

def createCSV(nameCSV, string):
    csv = open(nameCSV, "a")
    csv.write(string)

def greatestCommonDivisor(a, b):
    if a == 0: return b;
    if b == 0: return a;
    return greatestCommonDivisor(a, a%b);

def hasInverse(a, p):
    if greatestCommonDivisor(a,p) == 1:
        return True
    else:
        return False

def calculateInverse(a, p):


def countPrimes(num, n):
    type1 = type3 = 0

    i = 0
    while i < n:
        if num[i] == True:
            if typeOfPrime(i) == True:
                type1 += 1
            else:
                type3 += 1
        i += 1


    return type1, type3


def main():
    print(".::::: Capítulo 03 - Exercício 12 :::::.\n")
    print("----------------------------------------\n")

    numTests = NUM_TESTS
    numRange = NUM_RANGE
    createCSV("cap03_exer12.csv", "Número de Testes, Proporção entre Possuir e Não Possuir Inverso\n")
    
    i = 1
    count = 0
    while i <= (numTests):
        a = random.randint(numRange)
        b = random.randint(numRange)
        p = random.randint(numRange)

        if hasInverse(a, p) == True:
            inverse = calculateInverse(a, p)
            x = calculateSolution(a, b, p)
            count += 1

        createCSV("cap03_exer12.csv", str(numTests)+str(float(numTests)/float(count)))
        i += 1
main()