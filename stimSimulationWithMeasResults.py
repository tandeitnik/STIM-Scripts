#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:31:30 2022

@author: tandeitnik
"""

from stabilizer_functions import *
from utility_functions import *
import numpy as np

N = 10 #qubit overhead
T = 5 #how many gates are applied after each step
probMeasurement = 0.01 #probability of applying a measurement
steps = 100 #at each step T gates are applied and the von Neumann entropy s(x)
adjMat = linearAdjMat(N) #adj matrix
shots = 5 #number of times the circuit is sampled
qubitIdxs = range(N) #list of qubits that may receive a gate

#initialize system
s = stim.TableauSimulator()
#list that will contain the cumulative entropy after each step
cummulativeEntropy = []
#list with the index of the measured qubits
measurementList = []
#total circuit
circuitTotal = stim.Circuit()

for step in range(steps):

    #generate random circuit
    circuit, measurementListTemp = randomStimCircuit(N,T,adjMat,qubitIdxs,probMeasurement)
    circuitTotal = circuitTotal+circuit
    measurementList = measurementList + measurementListTemp
    #apply circuit
    s.do(circuit)
    #calculate the entropy
    cummulativeEntropy.append(sf.cummulativeEntropyStim(N,s))


#sample the circuit and store measurement results
#The measurementResults is an array where the first row contains the index of
#the measured qubits in chronological order and the subsequent rows the measurement
#results for each shot
measurementResults = np.zeros([shots+1,len(measurementList)])
measurementResults[0,:] = measurementList
sampler = circuitTotal.compile_sampler()
measurementResults[1:,:] = sampler.sample(shots)


#print evolution of cummulative entropy
for i in range(steps):
    
    nGates = str(T*N*(i+1))
    plt.plot(range(N+1),cummulativeEntropy[i], label = nGates+' gates')
    
plt.legend()