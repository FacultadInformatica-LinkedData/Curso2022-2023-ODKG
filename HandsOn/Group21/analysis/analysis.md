## Data Analysis
The following document presents the analysis made to the selected datasets.

### Datasets
The topic of the selected datasets are describe next:

* [200342-0-centros-dia.csv](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=22bceca8a5a03410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default): Municipal and subsidized day centers in the city of Madrid specialized in elderly care.
* [200761-0-parques-jardines.csv](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=7dda6a49c7105510VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default): Elderly homes and supervised apartments in the city of Madrid.
* [300048-0-ancianos-residencias-apartamento.csv](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=dc758935dde13410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default): Main municipal parks and gardens in the city of Madrid.

### Exploratory Data Analysis (EDA)
The exploratory data analysis can be found in the `analysis` folder. The notebook `analysis.ipynb` gathers the necessary code for creating the reports regarding the data types and ranges for each variable. From this analysis we can extract some conclusions as expressed next:

* The variables regarding the specifics attributes of the addresses like `PUERTA` and `ESCALERA` have a high percentage of nulity so they aren't going to be used in the ontology we are building.
* Variables like `HORARIO` and `TRANSPORTE` need to be preprocessed before being added to the ontology.

### Data Source's Licensing
Each of the selected datasets are edited by the City of Madrid, while the responsibles for the data are described next:

* `200761-0-parques-jardines.csv`: General Directorate of Water Management and Green Areas (*Dirección General de Gestión del Agua y Zonas Verdes*).
* `200342-0-centros-dia.csv`: General Directorate for the Elderly (*Dirección General de Mayores*).
* `300048-0-ancianos-residencias-apartamento.csv`: General Directorate of Attention to Citizenship (*Dirección General de Atención a la Ciudadanía*).

Regarding the [licences of each of the datasets and its conditions of use](https://datos.madrid.es/egob/catalogo/aviso-legal), all of them can be use for commercial and non-commercial purposes subject to the acknowledgment of source's authority.
