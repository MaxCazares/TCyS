# import easygui as eg
from scipy.spatial import distance

def identificar(formante, promedios):
    a = (formante[0], formante[1])
    if formante[0] == 0 and formante[1] == 0:
        return ' '
    ans = ''
    aux = 1000000
    for val in promedios:
        distancia = distance.euclidean(a, promedios[val])
        print("val: ",val, " distancia: ", distancia)
        if distancia < aux:
            if val == 'AH':
                ans = 'A'
            elif val == 'EH':
                ans = 'E'
            elif val == 'IH':
                ans = 'I'
            elif val == 'OH':
                ans = 'O'
            elif val == 'UH':
                ans = 'U'
            aux = distancia

    return ans

# def distancia():
  

  # vocal = ''
  # promediosH = [x * 1000 for x in promediosH]#Se hace ampliación de promedios
  # frecFund = frecFund * 1000#Se hace ampliación
  
  # tolerancia1 = 0.95
  # tolerancia2 = 0.13
  
  # AH=promediosH[0]; AHminor=AH*(1-tolerancia1); AHmayor=AH*(1+0.10)
  # EH=promediosH[1]; EHminor=EH*(1-tolerancia1); EHmayor=EH*(1+0.13)
  # IH=promediosH[2]; IHminor=IH*(1-tolerancia1); IHmayor=IH*(1+tolerancia1)
  # OH=promediosH[3]; OHminor=OH*(1-0.93); OHmayor=OH*(1+tolerancia2)
  # UH=promediosH[4]; UHminor=UH*(1-tolerancia2); UHmayor=UH*(1+tolerancia2)
  
  # print("A:",AH,"(",AHminor,",",AHmayor,")")
  # print("I:",IH,"(",IHminor,",",IHmayor,")")
  # print("E:",EH,"(",EHminor,",",EHmayor,")")
  # print("U:",UH,"(",UHminor,",",UHmayor,")")
  # print("O:",OH,"(",OHminor,",",OHmayor,")")
  # print("Frecuencia Fundamental: ",frecFund)
  
  # if frecFund>=AHminor and frecFund<=AHmayor:
  #   vocal = 'A'
  #   #eg.msgbox(msg='Es A (Hombre)',title='Identificado', ok_button='Aceptar')
  # elif frecFund>=EHminor and frecFund<=EHmayor:
  #   vocal = 'E'
  #   #eg.msgbox(msg='Es E (Hombre)',title='Identificado', ok_button='Aceptar')
  # elif frecFund>=IHminor and frecFund<=IHmayor:
  #   vocal = 'I'
  #   #eg.msgbox(msg='Es I (Hombre)',title='Identificado', ok_button='Aceptar')
  # elif frecFund>=UHminor and frecFund<=UHmayor:
  #   vocal = 'U'
  #   #eg.msgbox(msg='Es U (Hombre)',title='Identificado', ok_button='Aceptar')
  # elif frecFund>=OHminor and frecFund<=OHmayor:
  #   vocal = 'O'
  #   #eg.msgbox(msg='Es O (Hombre)',title='Identificado', ok_button='Aceptar') 
  # else:
  #   vocal = '   '
  #   #eg.msgbox(msg='Vocal no identificada',title='Atención', ok_button='Aceptar')
  # return vocal
