# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:59:41 2016

@author: José Arcos Aneas

Introducción a la librería de python Pandas
"""

# Importación de librerías
import pandas as pd 
import numpy as np
from pandas import DataFrame 


#Indexación de columnas

df = DataFrame ( { 'int_col' : [1,2,3,4,5], 'float_col' : [0.1,0.2,0.3,0.4,None], 'str_col' : ['a','b',None,'c','d']})
print "*"*15
print " DataFrame"
print df 
print " Columna Float"
print df[['float_col']]
print " Valores columna int mayores que uno o menores que 4"
print df [(df['int_col'] > 1) | (df['int_col'] < 4) ]
print "*"*15

##Renombarndo columans
print "Renombramiento de columnas"
print df
df2 = df.rename(columns={'int_col' : 'otra_col'})
print df
df2.rename(columns={'otra_col' : 'int_col'}, inplace = True)
print df
print "*"*15
"""
El programa pandas toma como columnas cada elemtno del dataFrame 
haciendo que sea posible formar filas 
"""

df2.dropna() ## borra cualquier entrada que no este completa
df3 = df.copy() ## copiamos un datagrama
df3['float_col'].fillna(np.mean) # Rellena el elmento vacio de la columna con la media 

print "Df rellenando el elemento vacio de las columnas con la media"
print df3
print "*"*15
print "Definimos la función F"
def f(x):
   if type(x) is str:
       return 'applymap_' + x
   elif x:
       return 100 * x
   else:
       return

print "Aplicamos F al dataframe"
df.applymap(f)
print df
print "*"*15

print "Definimos de nuevo el dataframe"
df = pd.DataFrame(data={"A":[1,2], "B":[2.6,1.3]})
print df
print "añadimos columnas combinando las actuales"
df["C"] = df["A"]+df["B"]
df["D"] = df["A"]*3
df["E"] = np.sqrt(df["A"])
print df
print "*"*15
print "Datos disponibles de un dataframe"
print " descripcion del dataframe"
print df.describe()
print " covarianza "
print df.cov()
print " correlación "
print df.corr()
print "*"*15

print " Creamos otro dataframe con valores aleatorios (1000 filas y 2 columnas "
print " DataFrame(np.random.randn(1000,2),columns=['x','y'])"
plot_df = DataFrame(np.random.randn(1000,2),columns=['x','y'])
print plot_df
print "Mostramos las graficas"
plot_df.plot()
plot_df.hist()







    