# -*- coding: utf-8 -*-

import sys
import random
from math import log
from math import pow

NUM_TESTS = 10000

def createCSV(nameCSV, string):
    csv = open(nameCSV, "a")
    csv.write(string)

def typeOfPrime(n):
    if n%4 == 1:
        return True
    else:
        return False

def erastosthenesSieve(n):
    i = 0
    num = []
    for i in range(n):
        num.append(True)
    
    num[0] = False
    num[1] = True
    num[2] = True

    i = 2
    while i < n:
        j = 2
        while j < n:
            if i*j < n:
                num[i*j] = False
            else:
                break
            j += 1
        i += 1

    return num, n

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
    createCSV("cap03_exer12.csv", "Número de Testes,Número de Tipos 1,Número de Tipos 2,Proporção\n")
    
    num, n = erastosthenesSieve(numTests)
    i = 1
    while i <= (int(log(numTests, 10))):
        type1, type3 = countPrimes(num, pow(10,i))
        relation = float(type1)/float(type3)
        createCSV("cap03_exer12.csv", str(int(pow(10, i)))+","+str(type1)+","+str(type3)+","+str(relation)+"\n")
        i += 1
main()