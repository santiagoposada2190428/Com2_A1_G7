"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, Ts=1.0):
        gr.sync_block.__init__(
            self,
            name="e_Diff",
            in_sig=[np.float32],
            out_sig=[np.float32],
        )
        self.Ts = float(Ts)
        self.x_prev = np.float32(0.0)
        self.have_prev = False  # para saber si ya tenemos muestra previa

    def work(self, input_items, output_items):
        x = input_items[0].astype(np.float32, copy=False)
        y = output_items[0]
        N = len(x)
        if N == 0:
            return 0

        # Diferenciación discreta por diferencia hacia atrás:
        # y[n] = (x[n] - x[n-1]) / Ts
        if not self.have_prev:
            # primera llamada: asumimos diferencia 0 en la primera muestra
            y[0] = np.float32(0.0)
            self.have_prev = True
        else:
            y[0] = (x[0] - self.x_prev) / self.Ts

        if N > 1:
            y[1:N] = (x[1:N] - x[0:N-1]) / self.Ts

        # guardar última muestra para la próxima llamada
        self.x_prev = x[-1]

        return len(y)