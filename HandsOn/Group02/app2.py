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
import tkintermapview 
import folium
import customtkinter


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
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        
        self.frame_left.grid_rowconfigure(2, weight=1)
        
        label = tk.Label(master=self.frame_left, text="Un choix")
        label.grid(column=0, row=1)

        combo = ttk.Combobox(master=self.frame_left, text="choix", values=DISTRICTS, 
                             textvariable=self.champs['choix'])
        combo.grid(column=1, row=1, columnspan=2)
        self.champs['choix'].set(combo.get())

        label = tk.Label(master=self.frame_left, text="Un choix")
        label.grid(column=0, row=2)

        combo = ttk.Combobox(master=self.frame_left, text="choix2", values=TYPE_ACCIDENT, 
                             textvariable=self.champs['choix2'])
        combo.grid(column=1, row=2, columnspan=2)

        label = tk.Label(master=self.frame_left, text="elec ?")
        label.grid(column=0, row=3)

        for i, rb_label in enumerate(IS_ELEC):
            rb = ttk.Radiobutton(master=self.frame_left, text=rb_label, value=i)
            rb.grid(column=i+1, row=3)

        checkButton = ttk.Checkbutton(master=self.frame_left, text="Accepter les conditions")
        checkButton.grid(column=0, row=4, columnspan=3)

        button = tk.Button(master=self.frame_left, text="Valider", command=self.valider)
        button.grid(column=1, row=5)
        
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)


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
        
        i = 0

        for result in results["results"]["bindings"]:
            qid = result['item']['value'].split('/')[-1]
            label = result['label']['value']

            label = label[:1].lower() + label[1:]

            out = "{}\tLfr\t{}".format(qid, label)
            print(out)
            
            instructions = tk.Label(self.frame_left, text=out, font='Raleway')
            instructions.grid(row=i)
            i+=1
        
        map_widget = tkintermapview.TkinterMapView(self.frame_right, width=800, height=600, corner_radius=0)
        map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        map_widget.set_position(40.4167, -3.70325) 
        map_widget.set_zoom(15)
        marker_1 = map_widget.set_address("calle gran via, 36, madrid, spain", marker=True)
        marker_1.set_text("place sol")
            

app = tk.Tk()
app.title("Demo Widgets")
DemoWidget(app)
app.mainloop()

#%%
c = folium.Map(location=[40.4167, -3.70325], zoom_start=15) 
folium.Marker([40.4167, -3.70325],popup="La Romantica").add_to(c)
c.save('maCarte1.html')




