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
    print(".::::: Capítulo 03 - Exercício 13 :::::.\n")
    print("----------------------------------------\n")

    numTests = NUM_TESTS
    createCSV("cap03_exer13.csv", "Número Mínimo Que Tipo1 > Tipo3\n")
    
    i = 10
    while True:
        num, n = erastosthenesSieve(i)
        type1, type3 = countPrimes(num, i)
        print(i)
        if(type1 > type3):
            print("VIVA")
            createCSV("cap03_exer13.csv", str(i)+"\n")
            break;
        i += 10
main()