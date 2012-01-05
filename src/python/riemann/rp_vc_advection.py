#!/usr/bin/env python
# encoding: utf-8
r"""
Variable coefficient 1D advection Riemann solver

.. math::
    q_t + u(x) q_x = 0.

Note that this is the color equation, not the conservative advection equation.
"""

import numpy as np

# Riemann solver constants
meqn = 1
mwaves = 1

def rp_vc_advection_1d(q_l,q_r,aux_l,aux_r,aux_global):
    r"""Basic 1d advection riemann solver
    
    *aux(i)* should contain -
     - *u(x_i)* - (float) advection speed
    
    See :ref:`petclaw_rp` for more details.
    
    :Version: 1.0 (2010-10-10)
    """
    
    # Number of Riemann problems we are solving
    nrp = q_l.shape[1]
    
    # Return values
    wave = np.empty( (meqn,mwaves,nrp) )
    s = np.empty( (mwaves,nrp) )
    amdq = np.zeros( (meqn,nrp) )
    apdq = np.zeros( (meqn,nrp) )
    
    wave[0,0,:] = q_r[0,:] - q_l[0,:]

    s[0,:] = aux_l[0,:]

    apdq[0,:] = (aux_l[0,:]>0)*s[0,:] * wave[0,0,:]
    amdq[0,:] = (aux_l[0,:]<0)*s[0,:] * wave[0,0,:]

    return wave, s, amdq, apdq