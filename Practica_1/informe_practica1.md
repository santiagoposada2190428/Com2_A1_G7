 \documentclass{journal}[IEEEtran, twocolumn]             % No modificar
\usepackage{float}
\usepackage{graphicx}
% PASO 1. Reemplace "Práctica 1" por el número de la práctica que corresponda
\newcommand{\dochead}{Práctica 1}     

% PASO 2. Reemplace "TÍTULO PRÁCTICA" por el título de la práctica que corresponda.
\newcommand{\docsubhead}{GNU radio}  

% PASO 3. Reemplace "B1A - 02" por el grupo de la asignatura y el número de su grupo de laboratorio
\newcommand{\teamname}{A1}     

% PASO 4. OPCIONAL: Reemplace "\docsubhead \docsubhead" por el título del documento en caso de requerirse.
\newcommand{\titulo}{\dochead: \docsubhead}      

% PASO 5. Reemplace "31 de diciembre de 2030" por la fecha de su documento
\newcommand{\fecha}{31 de Agosto de 2025}      

\input{./plantilla.tex}             % No modificar

\begin{document}                    % No modificar

\title{\textbf{\titulo}}            % No modificar

% PASO 6. Agregar aquí el nombre y código de los autores.  
\author{
Santiago Hernando Posada Bayona-2190428
Juan Camilo González Leal - 2184682
}

\affil{\small{Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones} \\ % No modificar
\small{Universidad Industrial de Santander}} % No modificar

\date{\fecha}                       % No modificar

\maketitle                          % No modificar
\thispagestyle{fancy}               % No modificar

%---------------------------------------------------------------
% PASO 7. **..**...****INICIE SU DOCUMENTO DESDE AQUI***...**...
%%%%% A PARTIR DE AQUÍ EDITE EL DOCUMENTO PARA AGREGAR TODO EL CONTENIDO REQUERIDO PARA EL ENTREGABLE CORRESPONDIENTE
%%%%  Todo el contenido a partir de este punto es SOLAMENTE ILUSTRATIVO.
%
% Para sus imformes, BORRE TODO el contenido de aquí en adelante  EXCEPTO la última línea que contiene el comando: \end{document}

\color{black}

\begin{multicols}{2}

\begin{abstract}
    En esta práctica, se implementarán tres bloques en GNU Radio: un bloque Acumulador, que realizará la suma acumulativa de las muestras de la señal, un bloque Diferenciador, encargado de calcular la diferencia entre las muestras consecutivas, y un bloque de Promedios de Tiempo, que calculará estadísticas clave como media, media cuadrática, RMS, potencia promedio y desviación estándar. Se hará un análisis de cómo estos bloques procesan la señal de entrada, permitiendo visualizar tanto sus formas de onda como sus estadísticas. Además, se hará uso de conceptos de estadística para abordar el problema del ruido blanco y se aplicarán herramientas como la densidad espectral de potencia para mitigar sus efectos en las señales, mejorando así la calidad en sistemas de comunicación.
\end{abstract}

\section{Introducción}

  En el presente informe se detallan los procedimientos realizados durante la práctica de análisis de señales empleando el entorno GNU Radio, herramienta ampliamente utilizada en el campo de las telecomunicaciones y procesamiento de señales. El objetivo principal de esta práctica fue implementar un conjunto de bloques personalizados para realizar un análisis profundo de una señal, enfocándose en operaciones de acumulación, diferenciación y el cálculo de estadísticas de la señal. La práctica abarcó tres bloques fundamentales: el bloque Acumulador, el bloque Diferenciador y el bloque Promedios de tiempo, cada uno con su respectiva función en el procesamiento y análisis de las señales.
 
  Además de la implementación de estos bloques, se propuso estudiar cómo el ruido afecta el análisis de señales, y cómo conceptos estadísticos avanzados pueden ser utilizados para mitigar los efectos de este ruido. Conceptos de promedios en tiempo real, densidad espectral de potencia, envolvente compleja de una señal en banda base, y ruido blanco fueron explorados durante la práctica para proporcionar un enfoque técnico profundo que permita abordar problemas comunes en sistemas de comunicación modernos.


\section{Descripción de los bloques implementados}
\begin{itemize}
    \item \textbf{Bloque Acumulador:}

   
  El bloque Acumulador tiene la tarea de acumular las muestras de la señal de entrada. La operación que realiza es la suma acumulativa, un proceso fundamental en el análisis de señales, ya que permite obtener el historial de una señal a lo largo del tiempo. Este tipo de operación es relevante en sistemas de procesamiento de señales en los que se requiere llevar un registro continuo de las señales, como en sistemas de integración o en la acumulación de energía en aplicaciones de energía renovable.

Entrada: La señal de entrada es de tipo float32, representando valores numéricos de la señal analizada.

Proceso: Utiliza la función np.cumsum(), que realiza la suma acumulativa de las muestras de la señal. Este proceso es fundamental para obtener una visión integral de la señal a lo largo de su tiempo de existencia.

Salida: La señal acumulada se pasa como salida, permitiendo observar el comportamiento acumulativo de la señal.

Este tipo de procesamiento es relevante cuando se analiza el comportamiento de una señal a largo plazo, como en el análisis de energía en sistemas de generación.

\end{itemize}
\begin{itemize}
    \item \textbf{Bloque Diferenciador}

    El Diferenciador calcula la diferencia entre las muestras consecutivas de la señal, una operación crucial en muchos sistemas de control y análisis de señales, ya que permite detectar cambios rápidos y transitorios en la señal. Este bloque implementa una diferenciación discreta utilizando el enfoque de diferencias hacia atrás, un método simple pero efectivo para calcular la tasa de cambio entre muestras consecutivas.
\item \textbf{Entrada:} Señal de tipo float32
\item \textbf{Proceso:} La diferencia entre cada muestra x[n] y su predecesora x[n-1] se calcula de forma discreta, normalizando por el tiempo de muestreo T_s:

\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{ecuation.jpg}
    
    \label{fig:placeholder}
\end{figure}
Esta operación es esencial para determinar la velocidad de cambio de una señal, útil en aplicaciones como la detección de bordes en imágenes o la identificación de transitorios en señales.

    \item \textbf{Salida:} La señal diferenciada, que proporciona una representación de la velocidad de cambio de la señal original.

    
\end{itemize}
Este proceso es comúnmente utilizado en sistemas donde se debe controlar o analizar el comportamiento dinámico de una señal, como en sistemas de control adaptativos o en la medición de aceleraciones.

    \item \textbf{Bloque de Promedios: }
    El bloque de Promedios de tiempo es probablemente uno de los más útiles en la práctica de señales, ya que permite calcular estadísticas clave que describen el comportamiento de una señal en el tiempo. Este bloque realiza acumulaciones estadísticas de las muestras de la señal y calcula cinco métricas fundamentales:
\begin{itemize}
    \item \textbf{ Media: }El promedio simple de las muestras de la señal.
\item \textbf{Media cuadrática (o Media de los Cuadrados): }El promedio de los cuadrados de las muestras, útil para entender la potencia de la señal.
\item \textbf{RMS (Root Mean Square): }La raíz cuadrada de la media cuadrática, una medida estándar de la amplitud efectiva de la señal.
\item \textbf{Potencia promedio: }El promedio de los cuadrados de las muestras, que representa la potencia media de la señal.
\item \textbf{Desviación estándar: }Mide la dispersión de las muestras respecto a la media, útil para conocer la estabilidad y la variabilidad de la señal.

\end{itemize}
Este bloque acumula información estadística en tiempo real
\begin{itemize}
    \item \textbf{ Entrada: }Señal de tipo float32,
\item \textbf{Proceso: }Utiliza acumulaciones parciales (np.cumsum) para calcular las estadísticas en tiempo real. La estadística se actualiza a medida que nuevas muestras son procesadas.
\item \textbf{Salida: }El bloque genera cinco salidas, cada una correspondiente a una de las estadísticas mencionadas: media, media cuadrática, RMS, potencia promedio y desviación estándar.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{promedio.jpg}
    \caption{Bloque de promedios}
    \label{fig:placeholder}
\end{figure}

\section{Conexiones en el flujo de trabajo}
La arquitectura de la práctica se basa en la interconexión de los bloques para realizar el análisis de la señal de entrada. A continuación se describe cómo fluye la señal a través del sistema:
\begin{itemize}
    \item \textbf{Señal de entrada: }Se alimenta a cada uno de los bloques: acumulador, diferenciador y bloque de promedios de tiempo.
\item \textbf{Salida del acumulador: }Se conecta a un visualizador de tiempo, permitiendo observar cómo se acumula la señal a lo largo del tiempo.
\item \textbf{Salida del diferenciador: }También se conecta a un visualizador de tiempo, mostrando cómo varía la señal a lo largo del tiempo.
\item \textbf{Salida de los promedios: }Cada una de las estadísticas generadas (media, RMS, etc.) se conecta a un visualizador numérico, permitiendo monitorear estas métricas en tiempo real.

\end{itemize}


Este flujo de trabajo permite realizar un análisis exhaustivo de las características dinámicas de la señal.





\section{Aplicaciones de los conceptos vistos}
Uno de los aspectos más relevantes de esta práctica es su aplicabilidad en el análisis de señales en sistemas de comunicación. El uso de bloques de acumulación y diferenciación es fundamental en el análisis de modulaciones y demodulaciones de señales, ya que permite extraer información clave de las variaciones de la señal a lo largo del tiempo.

Además, el uso de estadísticas como la media, RMS y desviación estándar es crucial en el análisis de ruido en sistemas de comunicación. Estas métricas permiten medir la calidad de la señal y la estabilidad, aspectos que son fundamentales para garantizar la eficiencia y fiabilidad de las comunicaciones.



\section{Análisis de ruido y solución estadística}
Para agregar un componente de ruido en el análisis, se puede añadir ruido blanco gaussiano a la señal de entrada. Este tipo de ruido es común en sistemas de comunicación y puede ser modelado como un proceso estocástico con media cero y una varianza determinada.

El análisis de densidad espectral de potencia (PSD) se puede aplicar para estudiar cómo la potencia de la señal se distribuye a través de diferentes frecuencias, lo que es fundamental para comprender la eficiencia espectral de la señal. Además, la envolvente compleja de la señal puede ser utilizada para estudiar cómo la señal se modula a lo largo del tiempo, especialmente en sistemas de modulación en amplitud.

 
\section{Conclusiones}
Esta práctica proporciona una comprensión más profunda de cómo procesar y analizar señales utilizando herramientas avanzadas como GNU Radio. A través de la implementación de bloques personalizados para la acumulación, diferenciación y cálculo de estadísticas, se demostró cómo analizar en tiempo real las características de una señal y cómo utilizar conceptos estadísticos para manejar el ruido y mejorar la calidad de las señales. Además, se evidenció cómo estos conceptos son esenciales en el diseño y la optimización de sistemas de comunicaciones en tiempo real, donde la precisión y la robustez frente a interferencias son fundamentales.

\section{GitHub}
Puedes encontrar el proyecto en GitHub: \url{https://github.com/santiagoposada2190428/Com2_A1_G7}.

 Teorema de Nyquist \cite{referencia1}.
GNU Radio \cite{referencia2} 
Comunicaciones Digitales basadas en radio definida por software \cite{referencia3} 





% NO MODIFIQUE NI ELIMINE ESTA PARTE PARA QUE LE APAREZCAN LAS REFERENCIAS
\bibliographystyle{IEEEtran}
\bibliography{bibliografia.bib}
\documentclass{article}
\usepackage{hyperref}
\hypersetup{
  colorlinks   = true,
  urlcolor     = blue,
  linkcolor    = blue
}

\begin{document}



\end{document}

\end{multicols}
\end{document}

