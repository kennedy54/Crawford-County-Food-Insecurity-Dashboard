# Crawford-County-Food-Insecurity-Dashboard
Official Repository for the Crawford County Food Insecurity Dashboard. This is an app deployed through Stremlit. This dashboard was created by Ryan Kennedy for his Senior Project at Allegheny College.

# Link to Dashboard- 
[Crawford County Food Insecurity Dashbord](https://crawford-county-food-insecurity-dashboard.streamlit.app/)

## Introduction and Motivation-
**Summary of Project:** I have created an interactive dashboard (using Streamlit.io) that uses collected health data, specifically relating to food insecurity in Crawford County, PA, to produce interactive plots, graphs, and charts (using Plotly.express). I have also created an interactive map (using CARTO) that will reside on its own page on the dashboard. I intend for this dashboard to reside on the internet on its own app to be the most accessible to the public, especially for policymakers and food-insecure individuals to access it. The goal of the dashboard is to understand the variables affecting food insecurity, which parts of the county are being affected the most, who is being affected, where resources are located, how have food insecurity trends changed over time, possible methods that could resolve what leads to food insecurity, and to finally educate policymakers and food insecure individuals.


## Related Work-
[Beyond Food Deserts](https://www.brookings.edu/articles/beyond-food-deserts-america-needs-a-new-approach-to-mapping-food-insecurity)

[The Hidden Resilience of ‘Food ‘Desert’ Neighborhoods](https://civileats.com/2018/09/14/the-hidden-resilience-of-food-desert-neighborhoods/)

[Washington DC Food Deserts](https://jennyminich.carto.com/builder/d8836780-dbea-42f7-a5e6-0e3883fa570d/embed?state=%7B%22map%22%3A%7B%22ne%22%3A%5B38.75595740859807%2C-77.31113433837892%5D%2C%22sw%22%3A%5B38.974624157287955%2C-77.00317382812501%5D%2C%22center%22%3A%5B38.865374851611634%2C-77.15715408325197%5D%2C%22zoom%22%3A12%7D%7D)

[Access to Affordable and Nutritious Food: Measuring and Understanding Food Deserts and Their Consequences: Report to Congress](https://ageconsearch.umn.edu/record/292130/)

[Desert Wonderings: Reimagining Food Access Mapping](https://doi.org/10.1007/s10460-019-09914-5)

[Where Do Americans Usually Shop for Food and How Do They Travel To Get There? Initial Findings From the National Household Food Acquisition and Purchase Survey](https://www.ers.usda.gov/webdocs/publications/43953/eib138_errata.pdf?v=5900.1)

[Access to Affordable and Nutritious Food: Measuring and Understanding Food Deserts and Their Consequences: Report to Congress](https://ageconsearch.umn.edu/record/292130/)

[Understanding Accessibility to Snap-Accepting Food Store Locations: Disentangling the Roles of Transportation and Socioeconmoic Status](https://link.springer.com/article/10.1007/s12061-015-9138-2#citeas)

[Driving to save time or saving time to drive? The enduring appeal of the private car](https://www.sciencedirect.com/science/article/abs/pii/S0965856414000962?via%3Dihub)

[Comparing two distance measures in the spatial mapping of food deserts: The case of Petržalka, Slovakia](https://www.geonika.cz/EN/research/ENMGRClanky/2017_2_BILKOVA.pdf)

[Redefining the food desrt: combining GIS with direct observation to measure food access](https://link.springer.com/article/10.1007/s10460-014-9501-y)

[Identifying food insecurity in food sharing networks via machine learning](https://www.sciencedirect.com/science/article/pii/S0148296320306123?casa_token=p8HRyU2POioAAAAA:9hsJjvkdaPxDjB4c72Uchs1iJIJaY_KitSuOqcZcwb6Ez52z1ele2DOQ9zG8pPP0ExU49k9J4CA#b0205)


## Technical Details-
I use the programming language "Python" to create an interactive Streamlit dashboard. On this dashboard, there will be different pages which include: a Home Page, a General Comparative Analysis Page, a Food Insecurity Map Page, and a Contact Page. On the Home Page, I create text that describes what will be included in the rest of the dashboard, and the overall purpose of the dashboard. I also include text on each page to describe each dataset being used, each graph I have included, and the food insecurity map. To do this I use markdown built into Streamlit. To actually create each graph, I import the libraries "Pandas" and "Plotly", which I can then create data frames using my imported data and customize how I want each graph to be presented. The General Food Insecurity Comparative Analysis Graphs include a graph that compares Crawford County to every other county in Pennsylvania, and a graph that describes the past 8 years of Very Low Food Insecurity, Regular Food Insecurity, and the Food Environment Index specifically in Crawford County. On the Food Insecurity Map, I use the software CARTO and import various CSV, shapefile, and geojson files directly into CARTO, which the software can interpret and plot accordingly. Simultaneously, CARTO relies on the programming language SQL to create queries and manipulate each data table in order to overall determine which data from those files to plot on the map.  I also include a tool that allows each user to find the nearest food resources to them based on an inputted radius. This tool refers to the same data used in the map but also refers to imported libraries: ssl, geopy.geocoders, Nominatim, certifi, math, radians, sin, cos, sqrt, atan2. I finally included a Contact page which allows the user to directly send any feedback, give suggestions, or report an issue with my dashboard. This uses the software "FormSubmit". I also use some CSS to further format the input text boxes and submit button.
