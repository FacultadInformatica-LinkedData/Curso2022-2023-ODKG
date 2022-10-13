#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


# Data load and manipulation
import io
 
# DataFrame librery
import pandas as pd
 
# Visualization 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
 
# Basic Operations
import numpy as np
from collections import defaultdict
from numpy import corrcoef, transpose
import itertools
import operator


# In[2]:


df = pd.read_csv('/mnt/c/Users/Ofeucor/Downloads/EstudioPatiosEscolares2022.csv', ';')
display(df.head(), df.shape, df.isnull().sum())


# In[3]:


df['TRANSPORTE'] = df['TRANSPORTE'].apply(lambda x: x.title().replace('Bus ', 'Bus: ') if x == x else x).replace('Desconocido', np.nan)
df['TRANSPORTE'].value_counts()
transportes = []
for v in df['TRANSPORTE']:
    d = {}
    if v == v:
        print(v)
        a = v.split(':')

        for k in range(1, len(a)-1):
            d[a[k-1].split()[-1]] = ' '.join(a[k].split()[:-1])
            #print(a[k-1].split()[-1], ':', ' '.join(a[k].split()[:-1]))
        
        d[a[-2].split()[-1]] = a[-1]
        #print(a[-2].split()[-1], ':', a[-1])

    transportes.append(d)
#transportes

bus = []
renfe = []
metro = []

for v in transportes:
    bus.append(v.get('Bus'))
    renfe.append(v.get('Renfe'))
    metro.append(v.get('Metro'))
    
df['TRANSPORTE_BUS'] = bus
df['TRANSPORTE_RENFE'] = renfe
df['TRANSPORTE_METRO'] = metro
df = df.fillna(value=pd.np.nan)


# In[4]:


df['DIRECCION'] = df['CLASE-VIAL'] + ' ' + df['NOMBRE-VIA'] + ' ' + df['NUM'].astype(str)

df.drop(['TRANSPORTE', 'HORARIO', 'DESCRIPCION-ENTIDAD', 'CLASE-VIAL', 'NOMBRE-VIA', 'NUM', 'TIPO-NUM', 'LATITUD', 'LONGITUD', 'TIPO'], axis=1, inplace=True)
df.dropna(how='all', axis=1, inplace=True)


# In[5]:


df.replace(np.nan, 'NaN', inplace=True)

for c in df.columns:
    if df[c].dtype == object:
        df[c] = df[c].apply(lambda x: x.capitalize())
        #print(c, str(df[c][0]),  str(df[c].dtype))

for c in ['BARRIO', 'DISTRITO']:
    df[c] = df[c].apply(lambda x: x.title())
    
    
df.replace('NaN', pd.np.nan, inplace=True)


# In[6]:


def removing(x):
    if '' in x:
        x.remove('')
    return ', '.join(x)


# In[7]:


df['EQUIPAMIENTO'] = df['EQUIPAMIENTO'].apply(lambda x: x.replace('.', ' - ').replace('  ', ' ').split(' - ') if x == x else np.nan).apply(lambda x: removing(x) if x == x else x)
df['JORNADA\n(días de apertura)'] = df['JORNADA\n(días de apertura)'].apply(lambda x: x.replace('.', ' ').replace('  ', ' ') if x == x else np.nan)
df['Nº PATIOS'] = df['Nº PATIOS'].replace('-', 0).replace('?', np.nan)
df['SERVICIOS\nAlumbrado, fuentes'] = df['SERVICIOS\nAlumbrado, fuentes'].replace('-', 'No').replace('?', np.nan)
df['ASEOS ACCESIBLES DESDE PATIO'] = df['ASEOS ACCESIBLES DESDE PATIO'].replace('-', 'No').replace('?', np.nan)
df['SOMBRA'] = df['SOMBRA'].replace('-', 'No').replace('?', np.nan)


# In[8]:


df.columns = ['pk',
 'name',
 'equipment',
 'description',
 'typeAccessibility',
 'contentURL',
 'locality',
 'province',
 'postalCode',
 'neighborhood',
 'district',
 'coordX',
 'coordY',
 'phone',
 'fax',
 'email',
 'titularity',
 'laborDay',
 'schedule',
 'extraUses',
 'otherUses',
 'yardCategory',
 'yardNumber',
 'accessibilityComment',
 'directAccess',
 'otherAccess',
 'wcAccessibles',
 'shade',
 'furniture',
 'services',
 'surface',
 'conservationState',
 'greenZonesProximity',
 'facilitiesProximity',
 'obserbations',
 'bus',
 'renfe',
 'metro',
 'address']


# In[9]:


for i in range(len(df.columns)):
    if i%2==0:
        c1=["tg-6e8n", df.columns[i]]
        c2=["tg-5w3z"]
        c3="tg-cjtp"
    else:
        c1=["tg-6e8n", df.columns[i]]
        c2=["tg-c4ww"]
        c3="tg-61xu"
        
    type_STR = (type(df[df.columns[i]].loc[0]).__name__).replace('str', 'String').replace("int64",'Decimal').replace("int64",'Decimal')
        
    if df[df.columns[i]].isnull().sum() == 249:
        c2.append("Empty")
    if (df[df.columns[i]].isnull().sum() > 0) and (df[df.columns[i]].isnull().sum() < 249):
        c2.append("Empty values")
    if type_STR == 'Decimal':
        c2.append("["+str(df[df.columns[i]].min())+"-"+str(df[df.columns[i]].max())+"]")
        
    if len(set(df[df.columns[i]])) == 1:
        c2.append("One value")
    elif len(set(df[df.columns[i]])) == len(df[df.columns[i]]):
        c2.append("Unique values")
    else:
        c2.append("NOT Unique")
        
        
    print("<tr>\n<td class=\"{}\">{}</td>\n".format(c1[0], c1[1])+
              "<td class=\"{}\">{}</td>\n".format(c2[0], type_STR)+
              "<td class=\"{}\">{}</td>\n".format(c2[0], ', '.join(c2[1:]))+
              "<td class=\"{}\">{}</td>\n</tr>".format(c3, "")
             )


# In[10]:


display(df.head(), df.shape, df.isna().sum())


# In[11]:


for c in df.columns:
    display(c, df[c].value_counts(),  str(df[c].dtype).replace('TIPO-NUM', 'Enumeration').replace('object', 'String').replace('int64','Decimal'))


# In[12]:


df.groupby(['district']).count().plot(kind='pie', y='pk', autopct='%1.0f%%')


# In[13]:


display(df.head(), df.columns)


# In[14]:


df.to_csv('EstudioPatiosEscolares2022-updated.csv')


# In[ ]:




