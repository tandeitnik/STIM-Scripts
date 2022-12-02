#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:45:17 2022

@author: tandeitnik
"""

import stabilizer_functions as sf
import utility_functions as uf
import stim
import matplotlib.pyplot as plt

N = 100 #qubit overhead
adjMat = uf.linearAdjMat(N) #linear adj matrix
T = 30 #how many gates are applied after each step
steps = 10 #at each step T gates are applied and the von Neumann entropy s(x) is evaluated
qubitIdxs = range(N) #list of qubits that may receive a gate

#initialize system
s = stim.TableauSimulator()
#list that will contain the cumulative entropy after each step
cummulativeEntropy = []

for step in range(steps):

    #draw circuit
    circuit = sf.randomStimCircuit(N,T,adjMat,qubitIdxs)
    #apply circuit
    s.do(circuit)
    #calculate the entropy
    cummulativeEntropy.append(sf.cummulativeEntropyStim(N,s))
    

for i in range(steps):
    
    nGates = str(T*N*(i+1))
    plt.plot(range(N+1),cummulativeEntropy[i], label = nGates+' gates')
    
plt.legend()


            

        
    
            
