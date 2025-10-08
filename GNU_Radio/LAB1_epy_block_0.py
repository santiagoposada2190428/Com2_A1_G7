"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
class blk ( gr . sync_block ) :
    def __init__ ( self ) : # only default a r g u m e n t s here
        gr . sync_block . __init__ (
            self ,
            name = "e_Diff" ,
            # will show up in GRC
            in_sig =[ np . float32 ] ,
            out_sig =[ np . float32 ]
        
        )
        self . acum_anterior = 0
    def work ( self , input_items , output_items ) :
        x = input_items [0]# Senial de entrada .
        y0 = output_items [0] # Senial a c u m u l a d a d i f e r e n c i a l
        N = len ( x )
        for i in range(N):
            y0 [i] = x[i]  - self.acum_anterior
            self.acum_anterior = x [i]


        
        return len ( y0 )
