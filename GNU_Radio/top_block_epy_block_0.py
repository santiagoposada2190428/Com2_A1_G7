import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """
    Bloque embebido para convertir una señal modulada en coseno
    a una señal en base banda compleja.
    
    Parámetros:
        Samp_Rate : Frecuencia de muestreo (Hz)
        Fc        : Frecuencia de la portadora (Hz)
    
    Entrada:
        float32 (real)  → señal modulada en coseno (ej. AM, FM, etc.)
    
    Salida:
        complex64 (compleja) → señal equivalente en base banda
    """

    def __init__(self, Samp_Rate=32000, Fc=5000):
        # Llamada al constructor de la clase base 'sync_block' de GNU Radio.
        # Este tipo de bloque produce una muestra de salida por cada muestra de entrada.
        gr.sync_block.__init__(
            self,
            name='Upconverter to Complex Baseband',  # Nombre del bloque que aparece en GNU Radio Companion
            in_sig=[np.complex64],   # Tipo de señal de entrada (aquí está definido como compleja)
            out_sig=[np.complex64]   # Tipo de señal de salida (compleja)
        )

        # Almacena los parámetros de configuración del bloque
        self.samp_rate = float(Samp_Rate)  # Frecuencia de muestreo
        self.fc = float(Fc)                # Frecuencia portadora
        self.phase = 0.0                   # Fase inicial del oscilador local
        # Incremento de fase por muestra (en radianes)
        self.phase_inc = 2 * np.pi * self.fc / self.samp_rate

    def work(self, input_items, output_items):
        """
        Función principal del bloque.
        Recibe un vector de muestras de entrada y produce el vector de salida.
        """
        in0 = input_items[0]   # Señal de entrada (vector numpy)
        out = output_items[0]  # Vector donde se almacenará la salida

        n = len(in0)            # Número de muestras del bloque de trabajo actual
        t = np.arange(n)        # Vector de índices de muestra

        # Calcula la fase acumulada del oscilador local para cada muestra
        phases = self.phase + t * self.phase_inc

        # Genera una señal compleja de referencia e^{-j2πFc t}
        # (mezclador complejo para trasladar la señal a base banda)
        mixer = np.exp(-1j * phases).astype(np.complex64)

        # Multiplica la señal de entrada por el mezclador
        # Esto efectúa una conversión de frecuencia (demodulación)
        out[:] = in0 * mixer

        # Actualiza la fase del oscilador para mantener continuidad entre llamadas a 'work'
        self.phase = (self.phase + n * self.phase_inc) % (2 * np.pi)

        # Devuelve el número de muestras procesadas
        return len(out)
