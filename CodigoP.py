# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

trayectoria="C:\\Users\\Mauricio de Ariño\\Documents\\Des. Aplicaciones\\Python\\Proyecto Python\\"
under5=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.CME_MRY0T4.._.csv",encoding='UTF-8')
lifexp=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.DM_LIFE_EXP.._.csv",encoding='UTF-8')
attendc=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.ED_ANAR_L2.._.csv",encoding='UTF-8')
vih=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.HVA_PMTCT_MTCT.._.csv",encoding='UTF-8')
marriage=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.PT_F_20-24_MRD_U15.._.csv",encoding='UTF-8')
poverty=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.PV_LEVEL.._.csv",encoding='UTF-8')
sanitation=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.WS_PPL_S-ALB.._.csv",encoding='UTF-8')
refugees=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.MG_RFGS_CNTRY_ORIGIN.._.csv",encoding='UTF-8')

print(under5)
print(lifexp)
print(attendc)
print(poverty)
print(sanitation)
print(refugees)

print(vih)
print(marriage)

#Brazil
brazilU5=under5.query("Geographicarea=='Brazil' & Sex=='Total' & (TIME_PERIOD=='2005' or TIME_PERIOD=='2010' or TIME_PERIOD=='2015' or TIME_PERIOD=='2018' )")
print(brazilU5[['TIME_PERIOD','OBS_VALUE']])     
m=brazilU5['OBS_VALUE'].max()
mb=brazilU5['TIME_PERIOD'][(brazilU5['OBS_VALUE']==m)]
mini=brazilU5['OBS_VALUE'].min()
mini2=brazilU5['TIME_PERIOD'][(brazilU5['OBS_VALUE']==mini)]
print("año: ",mb,"indicador: ",m)
print("año: ",mini2,"indicador: ",mini)


#Japon
japonU5=under5.query("Geographicarea=='Japan' & Sex=='Total' & (TIME_PERIOD=='2005' or TIME_PERIOD=='2010' or TIME_PERIOD=='2015' or TIME_PERIOD=='2018' )")
print(japonU5[['TIME_PERIOD','OBS_VALUE']]) 
m1=japonU5['OBS_VALUE'].max()
mj=japonU5['TIME_PERIOD'][(japonU5['OBS_VALUE']==m1)]
minij=japonU5['OBS_VALUE'].min()
minij2=japonU5['TIME_PERIOD'][(japonU5['OBS_VALUE']==minij)]
print("año: ",m1,"indicador: ",mj)
print("año: ",minij,"indicador: ",minij2)

#India
indiaU5=under5.query("Geographicarea=='India' & Sex=='Total' & (TIME_PERIOD=='2005' or TIME_PERIOD=='2010' or TIME_PERIOD=='2015' or TIME_PERIOD=='2018' )")
print(indiaU5[['TIME_PERIOD','OBS_VALUE']]) 
mi=indiaU5['OBS_VALUE'].max()
mi2=indiaU5['TIME_PERIOD'][(indiaU5['OBS_VALUE']==mi)]
minii=indiaU5['OBS_VALUE'].min()
minii2=indiaU5['TIME_PERIOD'][(indiaU5['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)

#Mexico
mexicoU5=under5.query("Geographicarea=='Brazil' & Sex=='Total' & (TIME_PERIOD=='2005' or TIME_PERIOD=='2010' or TIME_PERIOD=='2015' or TIME_PERIOD=='2018' )")
print(mexicoU5[['TIME_PERIOD','OBS_VALUE']]) 
mi=mexicoU5['OBS_VALUE'].max()
mi2=mexicoU5['TIME_PERIOD'][(mexicoU5['OBS_VALUE']==mi)]
minii=mexicoU5['OBS_VALUE'].min()
minii2=mexicoU5['TIME_PERIOD'][(mexicoU5['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)

#Sudafrica
sudafU5=under5.query("Geographicarea=='South Africa' & Sex=='Total' & (TIME_PERIOD=='2005' or TIME_PERIOD=='2010' or TIME_PERIOD=='2015' or TIME_PERIOD=='2018' )")
print(sudafU5[['TIME_PERIOD','OBS_VALUE']]) 
mi=sudafU5['OBS_VALUE'].max()
mi2=sudafU5['TIME_PERIOD'][(sudafU5['OBS_VALUE']==mi)]
minii=sudafU5['OBS_VALUE'].min()
minii2=sudafU5['TIME_PERIOD'][(sudafU5['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)


uganda=under5.query("Geographicarea=='Uganda' & Sex=='Total' & (TIME_PERIOD=='2005' or TIME_PERIOD=='2010' or TIME_PERIOD=='2015' or TIME_PERIOD=='2018' )")
print(ugandaU5[['TIME_PERIOD','OBS_VALUE']])
print(ugandaU5)
mi=ugandaU5['OBS_VALUE'].max()
mi2=ugandaU5['TIME_PERIOD'][(ugandaU5['OBS_VALUE']==mi)]
minii=ugandaU5['OBS_VALUE'].min()
minii2=ugandaU5['TIME_PERIOD'][(ugandaU5['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)













import matplotlib.pyplot as plt
import numpy as np

ugandaGraf=uganda[['TIME_PERIOD','OBS_VALUE']]
print(ugandaGraf)
setUgU5=set()
for i,j in ugandaGraf.itmes():
    print(j)


x=[]
y=[8,9,10,10]

plt.bar(x,y,color='green')
plt.xlabel("Alumnos")
plt.ylabel("Calificación")
plt.title("Calificaciones DAI")
plt.show()

refugees=pd.read_csv(trayectoria+"fusion_GLOBAL_DATAFLOW_UNICEF_1.0_.MG_RFGS_CNTRY_ORIGIN.._",encoding='UTF-8')
print(refugees)

#Brazil
brazilRef=refugees.query("Geographicarea=='Brazil'")
print(brazilRef[['TIME_PERIOD','OBS_VALUE']])     
m=brazilRef['OBS_VALUE'].max()
mb=brazilRef['TIME_PERIOD'][(brazilRef['OBS_VALUE']==m)]
mini=brazilRef['OBS_VALUE'].min()
mini2=brazilRef['TIME_PERIOD'][(brazilRef['OBS_VALUE']==mini)]
print("año: ",mb,"indicador: ",m)
print("año: ",mini2,"indicador: ",mini)


#Japon
japonRef=refugees.query("Geographicarea=='Japan'")
print(japonRef[['TIME_PERIOD','OBS_VALUE']]) 
m1=japonRef['OBS_VALUE'].max()
mj=japonRef['TIME_PERIOD'][(japonRef['OBS_VALUE']==m1)]
minij=japonRef['OBS_VALUE'].min()
minij2=japonRef['TIME_PERIOD'][(japonRef['OBS_VALUE']==minij)]
print("año: ",m1,"indicador: ",mj)
print("año: ",minij,"indicador: ",minij2)

#India
indiaRef=refugees.query("Geographicarea=='India'")
print(indiaRef[['TIME_PERIOD','OBS_VALUE']]) 
mi=indiaRef['OBS_VALUE'].max()
mi2=indiaRef['TIME_PERIOD'][(indiaRef['OBS_VALUE']==mi)]
minii=indiaRef['OBS_VALUE'].min()
minii2=indiaRef['TIME_PERIOD'][(indiaRef['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)

#Mexico
mexicoRef=refugees.query("Geographicarea=='Brazil'")
print(mexicoRef[['TIME_PERIOD','OBS_VALUE']]) 
mi=mexicoRef['OBS_VALUE'].max()
mi2=mexicoRef['TIME_PERIOD'][(mexicoRef['OBS_VALUE']==mi)]
minii=mexicoRef['OBS_VALUE'].min()
minii2=mexicoRef['TIME_PERIOD'][(mexicoRef['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)

#Sudafrica
sudafRef=refugees.query("Geographicarea=='South Africa'")
print(sudafRef[['TIME_PERIOD','OBS_VALUE']]) 
mi=sudafRef['OBS_VALUE'].max()
mi2=sudafRef['TIME_PERIOD'][(sudafRef['OBS_VALUE']==mi)]
minii=sudafRef['OBS_VALUE'].min()
minii2=sudafRef['TIME_PERIOD'][(sudafRef['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)

#Uganda
ugandaRef=refugees.query("Geographicarea=='Uganda'")
print(ugandaRef[['TIME_PERIOD','OBS_VALUE']])
print(ugandaRef)
mi=ugandaRef['OBS_VALUE'].max()
mi2=ugandaRef['TIME_PERIOD'][(ugandaRef['OBS_VALUE']==mi)]
minii=ugandaRef['OBS_VALUE'].min()
minii2=ugandaRef['TIME_PERIOD'][(ugandaRef['OBS_VALUE']==minii)]
print("año: ",mi,"indicador: ",mi2)
print("año: ",minii,"indicador: ",minii2)
