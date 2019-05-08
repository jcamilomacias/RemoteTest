#Imports
import scipy as sp
import numpy as np
from matplotlib.pyplot import plot as plt

#Global variables

S_orMax = 0.15 #cm^-3/cm^-3
z_aoMax = 150.0 #cm
z_owMin = 100.0 # cm
z_ow = z_owMin
alpha_ao = 0.124 # Falta revisar se es el mismo alpha en las dos interfases
alpha_ow = 0.124 # cm^-1
n = 2.28
m = 2.28 # falta buscar um m apropiado
rho_ro = 0.73 
z_oa = z_aoMax

##Head Colums

# Oil-water head
def h_ow(z):
    return (1 - rho_ro) * (z - z_ow)
