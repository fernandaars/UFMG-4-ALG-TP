# -*- coding: utf-8 -*-

import sys
import random
from math import log

NUM_TESTS = 10

def createCSV(nameCSV, string):
    csv = open(nameCSV, "a")
    csv.write(string)

def typeOfPrime(n):
    return True if n%4 == 1 else False

def erastosthenesSieve(n):
    i = 0
    num = []
    for i in range(n):
        num.append(True)
    
    num[0] = False

    i = 2
    for i in xrange(n):
        j = 2
        lim = n - i - 1
        for j in xrange(lim):
            if i*j < n:
                num[i*j] = False
                print(str(i*j)+"-> False")

    return num, n

def countPrimes(num, n):
    type1 = type3 = 0

    i = 0
    for i in xrange(n):
        if num[i]:
            if typeOfPrime(num[i]):
                type1 += 1
            else:
                type3 += 1


    return type1, type3


def main():
    print(".::::: Capítulo 03 - Exercício 12 :::::.\n")
    print("----------------------------------------\n")

    numTests = NUM_TESTS
    createCSV("cap03_exer12.csv", "Número de Testes,Número de Tipos 1,Número de Tipos 2,Proporção\n")
    
    num, n = erastosthenesSieve(numTests)
    i = 0
    for i in xrange(log(numTests)):
        type1, type3 = countPrimes(num, log(numTests)*(i+1))

        relation = float(type1)/float(type3)
        createCSV("cap03_exer12.csv", str(log(numTests)*(i+1))+","+str(type1)+","+str(type3)+","+str(relation)+"\n")

main()