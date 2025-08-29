"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="Promedios_de_tiempos",
            in_sig=[np.float32],
            out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32],
        )
        # Acumulados globales
        self.N = 0                          # número total de muestras acumuladas
        self.S1 = np.float64(0.0)           # suma de x
        self.S2 = np.float64(0.0)           # suma de x^2

    def work(self, input_items, output_items):
        x = input_items[0].astype(np.float32, copy=False)
        y0 = output_items[0]  # media
        y1 = output_items[1]  # media cuadrática
        y2 = output_items[2]  # RMS
        y3 = output_items[3]  # potencia promedio
        y4 = output_items[4]  # desviación estándar

        Nchunk = len(x)
        if Nchunk == 0:
            return 0

        # Usamos float64 para evitar errores numéricos en acumulados
        x64 = x.astype(np.float64, copy=False)

        # Acumulados parciales del chunk
        csum1 = np.cumsum(x64)          # sumas parciales de x
        csum2 = np.cumsum(x64 * x64)    # sumas parciales de x^2

        # Conteo acumulado en cada muestra del chunk
        n_vec = self.N + np.arange(1, Nchunk + 1, dtype=np.int64)

        # Estadísticos instantáneos (corrientes) en cada índice del chunk
        S1_inst = self.S1 + csum1
        S2_inst = self.S2 + csum2

        mean = S1_inst / n_vec
        mean_sq = S2_inst / n_vec
        rms = np.sqrt(mean_sq)
        # potencia promedio = E[x^2] (igual a mean_sq)
        pavg = mean_sq
        # var = E[x^2] - (E[x])^2
        var = np.maximum(mean_sq - mean * mean, 0.0)
        std = np.sqrt(var)

        # Escribimos salidas (como float32)
        y0[:] = mean.astype(np.float32, copy=False)
        y1[:] = mean_sq.astype(np.float32, copy=False)
        y2[:] = rms.astype(np.float32, copy=False)
        y3[:] = pavg.astype(np.float32, copy=False)
        y4[:] = std.astype(np.float32, copy=False)

        # Actualizamos estado global para próximas llamadas
        self.S1 += csum1[-1]
        self.S2 += csum2[-1]
        self.N += Nchunk

        return Nchunk