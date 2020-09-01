import numpy as np
from random import uniform

def model(T=15,LAI=8,PAR = 500, CO2 = 400): 
    
    # add random noise to inputs
    T = T+uniform(-.1, .1)
    LAI = LAI+uniform(-.5, +.5)
    PAR = PAR+uniform(-25, +25)
    CO2 = CO2+uniform(5, +5)
    # empiral photosynthesis model simplified from
    # http://hiilipuu.fi/articles/how-model-photosynthesis
    #Mäkelä, A., Pulkkinen, M., Kolari, P., Lagergren, F., Berbigier, P., Lindroth, A., Loustau, D., Nikinmaa, E., Vesala, T., and Hari,
    #P. 2008. Developing an empirical model of stand GPP with the LUE approach: analysis of eddy covariance data at five contrasting
    #conifer sites in Europe. Global Change Biology, 14, 92-108.
    
    
    # parameters of model
    K = 0.18    # no unit
    B = 300      # µmol m–2 s–1 
    Pmax  = 9     # µmol m–2 s–1 
    CO2ref = 400 # ppm
    gamma = 50   # ppm
    KCO2 = 500   # ppm
    # Temperature dependence is based on:
    #https://biocycle.atmos.colostate.edu/shiny/photosynthesis/\
    # to account for a non boreal forest
    
    cTh= .4
    cTc = .25 
    Tmin = 0
    Tmax = 40


    # minimum and maximum temperature relationshio
    fTh = 1-np.exp(cTh*(T-Tmax))
    fTc = 1-np.exp(cTc*(Tmin-T))
    f_T = fTc*fTh 

    f_LAI= 1 / K * (1  - np.exp(-K * LAI))
    f_PAR = Pmax * PAR / (PAR + B)
    f_CO2 = (CO2 - gamma) / (CO2 + gamma + KCO2) * (CO2ref + gamma + KCO2 ) / (CO2ref - gamma)

    P = f_LAI * f_PAR *  f_T * f_CO2
    P = max(0,P)

    return  round(P,2)

