#!/bin/python

# Calculate u u~ -> d d~ (via photon)

# Import spinor library
from PySpinor import *

# Define momenta in the problem
p1 = Momenta(7.500000e+02, 0.000000e+00, 0.000000e+00, 7.500000e+02, incoming=True)  # Incoming positron
p2 = Momenta(7.500000e+02, 0.000000e+00, 0.000000e+00,-7.500000e+02, incoming=True)  # Incoming electron
p3 = Momenta(7.500000e+02, 1.663864e+02, 6.672462e+02,-2.993294e+02)		     # Outgoing up quark
p4 = Momenta(7.500000e+02,-1.663864e+02,-6.672462e+02, 2.993294e+02)		     # Outgoing anti-up quark

# Define quark charges
q_u = + 2.0 * e / 3.0
q_d = - 1.0 * e / 3.0

# Pick a polarisation to look at (None = all polarisation states)
pol = None

# Define spinors
u_1 = Spinor(p1)
v_2 = Spinor(p2, fermion=False)
u_3 = Spinor(p3)
v_4 = Spinor(p4, fermion=False)

# Momentum transfer vector
q = p1 + p2

# Value of the prefactors
prefactor = (q_u * q_d) ** 2 / q.dot(q) ** 2

cur_1 = Current(v_4.bar(), 'mu', u_3)
cur_2 = Current(u_1.bar(), 'mu', v_2)

# Perform the contraction
contraction = cur_1.dot(cur_2)

# Combine prefactors and the sum of helicity combinations and then average over spins
# Multiply by 3.0 for colour sum     of final states
# Divide   by 3.0 for colour average of initial states
Amplitude = prefactor * cur_1.dot(cur_2)(pol) * avgFactor() * 3.0 / 3.0

# Return the result
print Amplitude, 'GeV'