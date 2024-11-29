#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:41:17 2020

The input file to run MC-EMMA with RLCSP for YBa2Ca2Fe5O13

@author: Elena Zamaraeva
"""
from mcemma_rl.mc_emma import *
import numpy
import sys
""" Cubic structures """

rep=[1,1,1]
ap=3.9

#Make A blocks
A1=Atoms("Ba4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A1.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5],
                         [0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5]])
A1=A1.repeat(rep)
#view(A1)
A2=Atoms("Ca4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A2.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5],
                         [0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5]])
A2=A2.repeat(rep)
#view(A2)
A3=Atoms("Y4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A3.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5]])
A3=A3.repeat(rep)
#view(A3)
A4=Atoms("Y4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A4.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5],
                         [0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5]])
A4=A4.repeat(rep)
#view(A4)
A5=Atoms("YCa2YO4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A5.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5],
                         [0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5]])
A5=A5.repeat(rep)
#view(A5)
A6=Atoms("YCa3O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A6.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5],
	[0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5]])
A6=A6.repeat(rep)
#view(A6)
A7=Atoms("CaY3O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A7.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5],
                         [0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5]])
A7=A7.repeat(rep)
#view(A7)
A8=Atoms("YCa2Y",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A8.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5]])
A8=A8.repeat(rep)
#view(A8)
A9=Atoms("YCa3",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A9.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5]])
A9=A9.repeat(rep)
#view(A9)
A10=Atoms("CaY3",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
A10.set_scaled_positions([[0.,0.,0.5],[0.5,0.,0.5],[0.,0.5,0.5],[0.5,0.5,0.5]])
A10=A10.repeat(rep)
#view(A10)





#Make B blocks
B1=Atoms("Fe4O8",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
B1.set_scaled_positions([[0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5],
                         [0.25,0.,0.5],[0.25,0.5,0.5],[0.75,0.,0.5],[0.75,0.5,0.5],
                         [0.,0.25,0.5],[0.5,0.25,0.5],[0.,0.75,0.5],[0.5,0.75,0.5]])
B1=B1.repeat(rep)
#view(B1)

B2=Atoms("Fe4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
B2.set_scaled_positions([[0.25,0.25,0.5],[0.75,0.25,0.5],[0.25,0.75,0.5],[0.75,0.75,0.5],
                         [0.25,0.5,0.5],[0.75,0.,0.5],[0.,0.25,0.5],[0.5,0.75,0.5]])
B2=B2.repeat(rep)
#view(B2)

B3=Atoms("Fe4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
B3.set_scaled_positions([
       [ 0.25   ,  0.25   ,  0.5    ],
       [ 0.75   ,  0.25   ,  0.5    ],
       [ 0.25   ,  0.75   ,  0.5    ],
       [ 0.75   ,  0.75   ,  0.5    ],
       [ 0.5    ,  0.25   ,  0.5    ],
       [ 0.0    ,  0.75   ,  0.5    ],
       [ 0.25   ,  0.0    ,  0.5    ],
       [ 0.75   ,  0.5    ,  0.5    ]])

B3=B3.repeat(rep)
#view(B3)

B4=Atoms("Fe4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
B4.set_scaled_positions([
       [ 0.25   ,  0.25   ,  0.5    ],
       [ 0.75   ,  0.25   ,  0.5    ],
       [ 0.25   ,  0.75   ,  0.5    ],
       [ 0.75   ,  0.75   ,  0.5    ],
       [ 0.25   ,  0.00   ,  0.5    ],
       [ 0.50   ,  0.75   ,  0.5    ],
       [ 0.75   ,  0.50   ,  0.5    ],
       [ 0.00   ,  0.25   ,  0.5    ]])

B4=B4.repeat(rep)
#view(B4)

B5=Atoms("Fe4O4",cell=[2.*ap,2.*ap,0.5*ap],pbc=[1,1,1])
B5.set_scaled_positions([
       [ 0.25   ,  0.25   ,  0.5    ],
       [ 0.75   ,  0.25   ,  0.5    ],
       [ 0.25   ,  0.75   ,  0.5    ],
       [ 0.75   ,  0.75   ,  0.5    ],
       [ 0.00   ,  0.75   ,  0.5    ],
       [ 0.25   ,  0.50   ,  0.5    ],
       [ 0.50   ,  0.25   ,  0.5    ],
       [ 0.75   ,  0.00   ,  0.5    ]])

B5=B5.repeat(rep)
#view(B5)


AMods=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10]
BMods=[B1,B2,B3,B4,B5]

if len(sys.argv) > 1:
    dir_num = sys.argv[1]
else:
    dir_num = '1'

mc(
#gulp parameters
kwds=['opti conp','opti conp'],
opts=[
['\nlibrary lib2.lib\ndump temp.res'],
['\nlibrary lib2.lib\ndump temp.res'],
],
shel=["Ba","Ca","O"],
lib = 'lib2.lib',
#compositionparameters
A_Mods={'orthorhombic':AMods},
B_Mods={'orthorhombic':BMods},
charges={"O":-2,"Ca":2,"Fe":3,"Y":3,"Ba":2},
composition={"Y":1.0,"Ba":2.0,"Ca":2.0,"Fe":5.0,"O":13},
sl=[5,10],

#mc run parameters
startup=3,
smax=1000,
rmax=100,
smin=500,
ratt_dist=0.1,
red_T=0.025,
delay = 0,
graph_out='T',
pert=(
['T1',29],
['T2',21],
['T3',21],
['T4',14],
['T5',7],
['T6',7],),
tmax=100000,
gulp_command='gulp < gulp.gin > gulp.got',
params_db={'host': 'HOST',
            'database': 'reinforce_mcemma',
            'user': 'USERNAME',
            'password': 'PASSWORD'},
alpha=0.01,
reinforce_table='reinforce',
theta_table='reinforce_theta',
reinforce_id=dir_num,
reg_params={'e_threshold': 0.8, 'beta': 1, 'free_term': 0, 'h_type': 'linear'}
)

