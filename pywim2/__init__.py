# -*- coding: utf-8 -*-
"""
This is the python version of WINNER phase II channel model, this model 
could be used for both system and link simulation. If for system simulation
usage, you can create the toplogy with generated correlation states. 
>>> sc = scenario.B3()
>>> nl = NetworkLayout(4, AntennaArray(), 200, AntennaArray(), 'Equal')
>>> links = nl.create_progration(sc)
>>> input = np.randn(1000, 1) + np.randn(1000, 1)i
>>> output = links[0].filter(input)

You can also use it in the link level simulation with the specific states. 
>>> h = LinkModel(scenario.B3())
>>> input = np.randn(1000, 1) + np.randn(1000, 1)i
>>> output = h.filter(input)
"""
from __future__ import division

import numpy as np



