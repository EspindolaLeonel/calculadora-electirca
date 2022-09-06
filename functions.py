import math
from cmath import sqrt
from math import acos
        #DECLARACION DE LAS FUNCIONES PARA CORRIENTE ALTERNA
def calcular_corriente_trifasica(potencia_trifasica, tension, cos_fi):
    if cos_fi == "":
        cos_fi = 0.98
        c_t = (potencia_trifasica*1000)/(math.sqrt(3) * tension * cos_fi)
        return( "No se ingreso el cos de fi. Se tomo como valor 0.98", round(c_t))
    else:
        cos_fi = float(cos_fi) 
        c_t = (potencia_trifasica*1000)/(math.sqrt(3) * tension * cos_fi)
        return(round(c_t))
       
def calcular_corriente_monofasica(potencia_monofasica, tension, cos_fi):
        c_m = (potencia_monofasica*1000)/(tension * cos_fi)
        return(c_m)    

def calcular_potencia_activa_trifasica(corriente_trifasica, tension, cos_fi):
        p_a_t = (corriente_trifasica * tension * cos_fi * math.sqrt(3))
        return(round(p_a_t))

def calcular_potencia_activa_monofasica(corriente_monofasica, tension, cos_fi):
        p_a_m = (corriente_monofasica * tension * cos_fi)
        return(round(p_a_m))

def calcular_potencia_reactiva_trifasica(corriente_trifasica, tension, cos_fi):
        sen_fi = math.sin(acos(cos_fi))
        p_r_t = (corriente_trifasica * tension * sen_fi * math.sqrt(3))
        return(p_r_t)

def calcular_potencia_reactiva_monofasica(corriente_trifasica, tension, cos_fi):
        sen_fi = math.sen(acos(cos_fi))
        p_r_m = (corriente_monofasica * tension * sen_fi)
        return(p_r_m)
def correccion_factor_potencia(potencia_activa, potencia_reactiva):
        cos_fi2 = 0.98
        tang_fi = math.tan(acos(cos_fi2))
        q_prima = (tang_fi * potencia_activa*1000)
        c_f_p = (potencia_reactiva*1000 - q_prima)
        return(c_f_p)
def VAr_a_faradio(tension, frecuencia, q_reactiva):
        c = (((tension * tension)/(2 * 3.1416 * frecuencia * q_reactiva*1000)))/1000000
        return(round(c))

            #DECLARACIONES DE FUNCIONES PARA CORRIENTE CONTINUA

def corriente(tension, resistencia):
        corriente = (tension / resistencia)
        return(corriente)

def tension(corriente, resistencia):
        tension= corriente*resistencia
        return(tension)

def resistencia(tension, corriente):
        resistencia = tension/corriente
        return(resistencia)

def potencia(tension, corriente):
        potencia = tension * corriente
        return(potencia)
