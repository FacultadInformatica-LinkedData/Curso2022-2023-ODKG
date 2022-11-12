#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:31:50 2022

@author: alexi
"""

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

df = pd.read_csv("AccidentesBicicletas-2019-2022-updated-with-links.csv")


DISTRICTS = ['','Hortaleza', 'Moncloa-Aravaca', 'Villa de Vallecas', 'Chamartín',
       'Moratalaz', 'Salamanca', 'Fuencarral-El Pardo', 'Centro',
       'Carabanchel', 'Arganzuela', 'Latina', 'Ciudad Lineal', 'Chamberí',
       'Retiro', 'San Blas', 'Tetuán', 'Puente de Vallecas', 'Vicálvaro',
       'Usera', 'Barajas', 'Villaverde']

TYPE_ACCIDENT = ['', 'Frontal-lateral collision', 'Fall', 'Scope', 'Lateral collision',
       'Hitting a person', 'Crash against fixed obstacle',
       'Frontal collision', 'Other', 'Hitting an animal',
       'Multiple collision', 'Overturn', 'Track exit only']

IS_ELEC = ['Yes', 'No', 'Both']

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
sparql = SPARQLWrapper(endpoint)

class DemoWidget(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.champs = {
            'choix2': tk.StringVar(),
            'choix': tk.StringVar(),
        }
        self._create_gui()
        self.pack()

    def _create_gui(self):
        label = tk.Label(self, text="Un choix")
        label.grid(column=0, row=1)

        combo = ttk.Combobox(self, text="choix", values=DISTRICTS, 
                             textvariable=self.champs['choix'])
        combo.grid(column=1, row=1, columnspan=2)
        self.champs['choix'].set(combo.get())

        label = tk.Label(self, text="Un choix")
        label.grid(column=0, row=2)

        combo = ttk.Combobox(self, text="choix2", values=TYPE_ACCIDENT, 
                             textvariable=self.champs['choix2'])
        combo.grid(column=1, row=2, columnspan=2)

        label = tk.Label(self, text="elec bycicle ?")
        label.grid(column=0, row=3)

        for i, rb_label in enumerate(IS_ELEC):
            rb = ttk.Radiobutton(self, text=rb_label, value=i)
            rb.grid(column=i+1, row=3)

        checkButton = ttk.Checkbutton(self, text="Accepter les conditions")
        checkButton.grid(column=0, row=4, columnspan=3)

        button = tk.Button(self, text="Valider", command=self.valider)
        button.grid(column=1, row=5)


    def valider(self):
        for v, k in self.champs.items():
            print(f"{v} : {k.get()}")
        self.query()
    
    def query(self):

        sparql.setQuery("""
        SELECT ?item ?label WHERE {{
          ?item wdt:P31/wdt:P279* wd:Q178561 .
          ?item rdfs:label ?label . FILTER(LANG(?label) = "fr") .
          FILTER(STRSTARTS(?label, "Siège ")) .
        }}
        """)  # Link to query: http://tinyurl.com/z8bd26h
        
        # sparql.setQuery("""
        # SELECT ?item ?label WHERE {{
        #   
        # }}
        # """)

        sparql.setReturnFormat(JSON)

        results = sparql.query().convert()
        
        canvas = tk.Canvas(self, width=600, height=300)
        canvas.grid(row=6)
        i = 0

        for result in results["results"]["bindings"]:
            qid = result['item']['value'].split('/')[-1]
            label = result['label']['value']

            label = label[:1].lower() + label[1:]

            out = "{}\tLfr\t{}".format(qid, label)
            print(out)
            
            instructions = tk.Label(self, text=out, font='Raleway')
            instructions.grid(row=i)
            i+=1
            


app = tk.Tk()
app.title("Demo Widgets")
DemoWidget(app)
app.mainloop()

#%%

import folium
c = folium.Map(location=[40.4167, -3.70325], zoom_start=15) 
folium.Marker([40.4167, -3.70325],popup="La Romantica").add_to(c)
c.save('maCarte1.html')






