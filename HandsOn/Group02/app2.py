#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:31:50 2022

@author: alexi
"""

import customtkinter
from tkintermapview import TkinterMapView 
import tkinter as tk
from SPARQLWrapper import SPARQLWrapper, JSON
from geopy.geocoders import Nominatim

customtkinter.set_default_color_theme("blue")

DISTRICTS = ['All','Hortaleza', 'Moncloa-Aravaca', 'Villa de Vallecas', 'Chamartín',
       'Moratalaz', 'Salamanca', 'Fuencarral-El Pardo', 'Centro',
       'Carabanchel', 'Arganzuela', 'Latina', 'Ciudad Lineal', 'Chamberí',
       'Retiro', 'San Blas', 'Tetuán', 'Puente de Vallecas', 'Vicálvaro',
       'Usera', 'Barajas', 'Villaverde']

TYPE_ACCIDENT = ['All', 'Frontal-lateral collision', 'Fall', 'Scope', 'Lateral collision',
       'Hitting a person', 'Crash against fixed obstacle',
       'Frontal collision', 'Other', 'Hitting an animal',
       'Multiple collision', 'Overturn', 'Track exit only']

IS_ELEC = ['Yes', 'No', 'All']

endpoint = "http://localhost:9000/sparql"
sparql = SPARQLWrapper(endpoint)

APP_NAME = "TkinterMapView with CustomTkinter"
geolocator = Nominatim(user_agent=APP_NAME)

class App(customtkinter.CTk):

    APP_NAME = "TkinterMapView with CustomTkinter"
    WIDTH = 800
    HEIGHT = 500
    geolocator = Nominatim(user_agent=APP_NAME)
    list_district = []
    list_type_accident = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(2, weight=1)
        
        self.menu_1_label = customtkinter.CTkLabel(self.frame_left, text="District :", anchor="w")
        self.menu_1_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu_1 = customtkinter.CTkOptionMenu(self.frame_left, values=DISTRICTS,
                                                                       command=self.change_district)
        self.map_option_menu_1.grid(row=0, column=1, padx=(20, 20), pady=(10, 0))
        
        self.menu_1_label = customtkinter.CTkLabel(self.frame_left, text="Type accident :", anchor="w")
        self.menu_1_label.grid(row=1, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu_1 = customtkinter.CTkOptionMenu(self.frame_left, values=TYPE_ACCIDENT,
                                                                       command=self.change_type_accident)
        self.map_option_menu_1.grid(row=1, column=1, padx=(20, 20), pady=(10, 0))
        
        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Clear Markers",
        #                                         command=self.clear_marker_event)
        # self.button_2.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)

        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Tile Server:", anchor="w")
        self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))
        
        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Madrid") 
        self.map_option_menu.set("OpenStreetMap")
        self.appearance_mode_optionemenu.set("Dark")

        self.marker_list.append(self.map_widget.set_marker(40.4167754, -3.7037902))
        self.marker_list.append(self.map_widget.set_marker(40.4167754, -3.8037902))

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()
        
    def change_district(self, new_district):
        print("change di")
        nd = new_district
        new_district = new_district.replace(' ', '')
        
        if new_district == "All":
            sparql.setQuery("""
                PREFIX ns0: <https://motools.sourceforge.net/event/event.html#> 
            PREFIX ns1: <http://bicycleaccident.com/group2/ontology/property#> 
            PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
            PREFIX time: <http://www.w3.org/2006/time#> 
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX place: <http://bicycleaccident.com/group2/resource/Place/>

            SELECT ?adress WHERE {
              ?place a <http://bicycleaccident.com/group2/ontology/class#SpatialThingUTM> .
              ?place rdfs:label ?adress .
            } 
            """)
            self.map_widget.set_address("Madrid")
            self.map_widget.set_zoom(14)
            
        else:
            sparql.setQuery("""
                PREFIX ns0: <https://motools.sourceforge.net/event/event.html#> 
            PREFIX ns1: <http://bicycleaccident.com/group2/ontology/property#> 
            PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
            PREFIX time: <http://www.w3.org/2006/time#> 
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX place: <http://bicycleaccident.com/group2/resource/Place/>

            SELECT ?adress WHERE {
              ?place a <http://bicycleaccident.com/group2/ontology/class#SpatialThingUTM> .
              ?place rdfs:label ?adress .
              ?place ns1:isDistrict place:"""+new_district+""" .
            } 
            """)
            self.map_widget.set_address("Madrid "+nd)
            self.map_widget.set_zoom(14)
        
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        self.list_district = []
        for result in results["results"]["bindings"]:
            adress = result['adress']['value']
            self.list_district.append(adress)  
        print("distr", self.list_district)
        self.update_marker()

    def change_type_accident(self, new_type_accident):
        print("change ac")
        
        if new_type_accident == "All":
            sparql.setQuery("""
            PREFIX ns0: <https://motools.sourceforge.net/event/event.html#> 
            PREFIX ns1: <http://bicycleaccident.com/group2/ontology/property#> 
            PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
            PREFIX time: <http://www.w3.org/2006/time#> 
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX res: <http://bicycleaccident.com/group2/resource/>
            
            SELECT ?adress WHERE {{
              ?acc ns0:term_place ?place .
              ?place rdfs:label ?adress .
            }}
            """)
            
        else:   
            sparql.setQuery("""
            PREFIX ns0: <https://motools.sourceforge.net/event/event.html#> 
            PREFIX ns1: <http://bicycleaccident.com/group2/ontology/property#> 
            PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
            PREFIX time: <http://www.w3.org/2006/time#> 
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX res: <http://bicycleaccident.com/group2/resource/>
            
            SELECT ?adress WHERE {
              ?acc ns1:hasType \""""+new_type_accident+"""\" .
              ?acc ns0:term_place ?place .
              ?place rdfs:label ?adress .
            }
            """)
        
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        self.list_type_accident = []
        for result in results["results"]["bindings"]:
            adress = result['adress']['value']
            self.list_type_accident.append(adress)
        print("type ", self.list_type_accident)
        self.update_marker()
        
    def update_marker(self):
        print("update")
        self.clear_marker_event()
        print("type ", self.list_type_accident)
        print("distr", self.list_district)
        liste = list(set(self.list_district) & set(self.list_type_accident))
        print(liste)
        for adr in liste:
            location = geolocator.geocode(adr)
            if location != None:
                lat = location.latitude
                lon = location.longitude
                self.marker_list.append(self.map_widget.set_marker(lat, lon))
            
        

if __name__ == "__main__":
    app = App()
    app.start()

#%%

from SPARQLWrapper import SPARQLWrapper, JSON, XML

endpoint = "http://localhost:9000/sparql"
sparql = SPARQLWrapper(endpoint)

TYPE_ACCIDENT = ['Frontal-lateral collision', 'Fall', 'Scope', 'Lateral collision',
       'Hitting a person', 'Crash against fixed obstacle',
       'Frontal collision', 'Other', 'Hitting an animal',
       'Multiple collision', 'Overturn', 'Track exit only']

for d in TYPE_ACCIDENT:
    print(d)
    distr = d
    
    sparql.setQuery("""
    PREFIX ns0: <https://motools.sourceforge.net/event/event.html#> 
    PREFIX ns1: <http://bicycleaccident.com/group2/ontology/property#> 
    PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
    PREFIX time: <http://www.w3.org/2006/time#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX res: <http://bicycleaccident.com/group2/resource/>
    
    SELECT ?adress WHERE {
      ?acc ns1:hasType \""""+distr+"""\" .
      ?acc ns0:term_place ?place .
      ?place rdfs:label ?adress .
    }
    """)
    
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    list_district = []
    for result in results["results"]["bindings"]:
        adress = result['adress']['value']
        list_district.append(adress)
    
    print(list_district)






