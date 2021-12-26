import numpy as np
import librosa
import scipy
import statistics
from formantes import getFormantes


#---------------------------------------------------------------------------------------------
def analizaAudio(path):
    muestras, tasa_muestreo = librosa.load(path, sr=None, mono=True, offset=0.0, duration=None)
    info = dict()
    info['muestras'] = muestras
    info['tasa_muestreo'] = tasa_muestreo
    return info

#---------------------------------------------------------------------------------------------
def getAmplitudes(muestras):#Retorna arreglo con las amplitudes
    n = len(muestras)
    # print("len(muestras): "+str(n))
    fft = scipy.fft.fft(muestras)
    amplitudes = 2.0/n * np.abs(fft[:n//2])

    return amplitudes

#---------------------------------------------------------------------------------------------
def startAnalisis():
    carpetas = ['AH','EH','IH','OH','UH']
    promedios1 = {'AH':(0,0), 'EH':(0,0), 'IH':(0,0),'OH':(0,0), 'UH':(0,0)}
    # promedios2 = {'AH':0, 'EH':0, 'IH':0,'OH':0, 'UH':0}
    for carpeta in carpetas:
        formantes1 = []
        formantes2 = []
        for i in range(1,2,1):
            path = 'Audios/'+carpeta+'/'+carpeta+'_'+str(i)+'.wav'
            aux = getFormantes(path)
            if np.isnan(aux[0]):
                print('carpeta: '+carpeta+' range: '+str(i))
                print("aux: " + str(aux[0]))
                print("is nan")
                aux[0]=0
            
            formantes1.append(aux[0])
            formantes2.append(aux[1])
        promedios1[carpeta] = (statistics.mean(formantes1), statistics.mean(formantes2))
        # promedios2[carpeta] = (statistics.mean(formantes2))
    print("Promedios: ")
    print(promedios1)
    print('')
    return promedios1

# def frecuenciaFundamental():
    

# startAnalisis()