#!/usr/bin/env python
# encoding: utf-8
r"""
Variable coefficient 1D advection Riemann solver

.. math::
    q_t + u(x) q_x = 0.
"""
# ============================================================================
#      Copyright (C) 2008 Kyle T. Mandli <mandli@amath.washington.edu>
#
#  Distributed under the terms of the Berkeley Software Distribution (BSD) 
#  license
#                     http://www.opensource.org/licenses/
# ============================================================================

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

    #print "test: aux_l size", aux_l.shape
    #print "test: s size", s[0,:].shape

    # Amal: it was s[0,:] = aux_l, you need to figure it out
    s[0,:] = aux_l[0,:]

    # Amal: it was  aux_l in both lines, you need to figure it out
    apdq[0,:] = (aux_l[0,:]>0)*s[0,:] * wave[0,0,:]
    amdq[0,:] = (aux_l[0,:]<0)*s[0,:] * wave[0,0,:]

    return wave, s, amdq, apdq
