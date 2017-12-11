# -*- coding: utf-8 -*-

import sys
import random
from math import log
from math import pow

NUM_TESTS = 1000000

def createCSV(nameCSV, string):
    csv = open(nameCSV, "a")
    csv.write(string)

def s(n):
    s = i = 0
    coefficients = [22916850747390, -4294497206839, 19933041355048, 2822622049280, 0, 0, -3471281875914, 0, 3382010886195, -2537982656589, 838614942934, -136044512548, 8914545378] 
    while i < 12:
        s += coefficients[i]*(pow(log(log(n)),i))
        i += 1
    s = pow(s, -1/4) + 1
    s = s*(float(n)/float(log(n)))
    return s


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
    numPrimes = 0

    i = 0
    while i < n:
        if num[i] == True:
            numPrimes += 1
        i += 1

    return numPrimes


def main():
    print(".::::: Capítulo 03 - Exercício 11 :::::.\n")
    print("----------------------------------------\n")

    numTests = NUM_TESTS
    createCSV("cap03_exer11.csv", "Número de Testes, Aproximação Simples , Fórmula S, Número Real\n")
    
    num, n = erastosthenesSieve(numTests)
    count = 0
    i = 1
    while i <= (int(log(numTests, 10))):
        count = countPrimes(num, pow(10,i))
        createCSV("cap03_exer11.csv", str(pow(10,i))+","+str(float(pow(10,i))/float(log(pow(10,i))))+","+str(s(pow(10,i)))+","+str(count)+"\n")
        i += 1
main()