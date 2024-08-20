#Importing Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import ssl
import geopy.geocoders
#import os
#import geopy.geocoders
#from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import certifi
from math import radians, sin, cos, sqrt, atan2
#from geopy.geocoders import options
#import mapbox
#import cartoframes
#import requests

@st.cache_data

#function that calculates the distances of coordinates one (user's location) and coordinates two (food resources location) using latitude and longitude values
def calculate_distance(coord1, coord2):
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #Next two lines define radius of earth in miles
    radius_of_earth_in_miles = 3958.8
    distance = radius_of_earth_in_miles * c
    return distance

#defining function that filters the user's location, the desired radius they want to query, and the location of the food resource (defined in a dataframe)
def filter_resources(user_location, radius, resources_df):
    user_coord = (user_location.latitude, user_location.longitude)
    filtered_resources = []
    for index, row in resources_df.iterrows():
        resource_coord = (row['Latitude'], row['Longitude'])
        distance = calculate_distance(user_coord, resource_coord)
        if distance <= radius:
            filtered_resources.append(row)
    return pd.DataFrame(filtered_resources)

#accesses geographic data to define specific locations
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

#defining function that geocodes the user's address using the geographic data from ssl and geocoder/Nomatim. The point of this is to determine accurate exact coordinates/location when the user inputs their address
def geocode_user_address(address):
    geopy.geocoders.options.default_ssl_context = ssl_context
    geolocator = Nominatim(user_agent="food_resource_locator", scheme='https') #verify=False #ssl_context=context #cafile=cafile
    location = geolocator.geocode(address)
    if location:
        return location
    else:
        return None

#importing 3 different datasets and defining three different dataframes of all types of food resources
food_resources1_df = pd.read_csv('data/Crawford_County_Food_Resource_Locations_Radius.csv')
food_resources2_df = pd.read_csv('data/Supermarkets_and_Grocery_Stores_Located_within_Crawford_County_PA_Radius.csv')
food_resources3_df = pd.read_csv('data/Fast_Food_Establishments_Radius.csv')

#variables that combine the previously defined dataframes into one dataframe
all_resources_df = pd.concat([food_resources1_df, food_resources2_df, food_resources3_df])


#df = pd.read_csv("/Users/ryankennedy/Desktop/Food_Insecurity_Data/Food_Insecurity_Data_CSV_Files/Crawford_County_Food_Resource_Locations.csv")

#set_default_credentials('kennedy54', 'eyJhbGciOiJIUzI1NiJ9.eyJhIjoiYWNfeTUxeGM2dTYiLCJqdGkiOiJmNWQ2NGQ3NiJ9.Z4srcJKBoYBEcjbfZ5DGDp80KlthBi6ONC-Tx2Zt3qg')

#eyJhbGciOiJIUzI1NiJ9.eyJhIjoiYWNfeTUxeGM2dTYiLCJqdGkiOiJmNWQ2NGQ3NiJ9.Z4srcJKBoYBEcjbfZ5DGDp80KlthBi6ONC-Tx2Zt3qg

#def calculate_accessibility_score(user_location, food_resources, max_distance=20.0):
#    distances = [geopy.distance.geodesic(user_location, resource).km for resource in food_resources]
#    accessible_resources = sum(1 for distance in distances if distance <= max_distance)
#    total_resources = len(food_resources)
#    accessibility_score = accessible_resources / total_resources
#    return accessibility_score

#setting page configuration by initializing that this is the map's comparative analysis page, setting the emoji to the "map" emoji, and making the page a wide format 
st.set_page_config(page_title="Interactive Map", page_icon=":world_map:", layout='wide')

#creating sidebar to select compartive analysis subpages for when a user is on the Interactive Map's main page
options = st.sidebar.radio('Comparative Analysis of Map', options=['Map and Food Resource Radius', 'Map and Census Tract Data'])

#Importing Crawford County's Census Tract Data for second subpage and creating second dataframe
dataframe = pd.read_csv("data/Name_Census_Tract_Data.csv")

#defining map function that calls the previously created first dataframe which combines the original first three dataframes defined. This function defines all information and food resource radius table that will be included within the first subpage
def map(all_resources_df):
    st.header('Crawford County Food Insecurity Map :world_map:')
    #markdown text that describes the data and what will be included on the map
    st.markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This map displays various types of food resource locations (i.e. food pantries, food banks, food charities; supermarkets, grocery stores, convenience stores; and fast food establishments). It also displays each census tract within Crawford County, and if they are considered to be a food desert, low income, or low vehicle access area.')
    st.markdown(' The map description is displayed directly to the side panel on the right of the map. This includes more information about the data and insights that may be noticed.')

    st.markdown('#### You can directly interact with this map by:')
    st.markdown('- Scrolling and zooming in and out')
    st.markdown('- Clicking or hovering over each food resource plot to display data')
    st.markdown('- Clicking on each census track (shaded or unshaded) to display data') 
    st.markdown('- Toggling between which layers of the map you want to be displayed using the legend')
    st.markdown('- Searching for a location in the search bar tool')
    st.markdown('- Creating a mask to select data within a certain region using the mask tool. This will allow the user to only look at data within a specific region of the map. Select the mode of the mask tool you want to use: polygon, rectangle, circle, and lasso.')
    st.markdown(' - - For the polygon mode, click on the map multiple times to create points and connect them together to create any shape.') 
    st.markdown(' - - For the rectangle and circle mode, click and move your cursor to how big you want the rectangle or circle to be, then click again to lock those shapes.') 
    st.markdown(' - - For the lasso mode, click, hold, and drag your cursor however you want and this will create multiple points. Connect these points to create a loose-shaped mask.')
    st.markdown('- Measuring distance between two points using the measure tool (ruler tool)') 
    st.markdown(' - - Click anywhere on the map and move your cursor to another location and the distance between those points will be displayed in kilometers. You can also click again to lock those points in place.')
    st.markdown('- Downloading the viewport data of everything that is plotted')

    #markdown html code that embeds the interactive CARTO map I made directly into the subpage
    st.markdown('<iframe width="100%" height="800" src="https://clausa.app.carto.com/map/3e0786c8-41ed-401e-afbe-da2fcdc26046"></iframe>', unsafe_allow_html=True)

#    context = ssl.SSLContext( ssl.PROTOCOL_TLS_CLIENT )
#    context.minimum_version = ssl.TLSVersion.TLSv1_2
#    context.maximum_version = ssl.TLSVersion.TLSv1_3

    #markdown text that tells the user to input their address below to see the food resources in their radius
    st.markdown('### Enter your address below to see the names, amount, and distance of food resources are in your selected radius!')
    #markdown text that tells the user exactly how to input their address in order for the code to work
    st.markdown('Address must be formatted as: <u>123 Main Street Anytown, PA 12345</u>', unsafe_allow_html=True)

    #creating a text input box for users to input their address
    user_address = st.text_input('Enter your address:')
    #creating a slider that allows the user to select the radius to find the nearest food resources
    radius_mi= st.slider('Select radius (mi)', min_value=1, max_value=20, step=1)

    #if statement that creates a button that initializes the process of finding all the food resources within the specified radius by the user, and the user's inputted address. This if statement will then visually display the outputted results
    if st.button('Find Food Resources'):
        user_location = geocode_user_address(user_address)
        if user_location:
            filtered_df = filter_resources(user_location, radius_mi, all_resources_df)
            filtered_df = filtered_df.reset_index(drop=True)
            filtered_df['Distance'] = filtered_df.apply(lambda row: calculate_distance((row['Latitude'], row['Longitude']), (user_location.latitude, user_location.longitude)), axis=1)
            filtered_df = filtered_df.sort_values(by='Distance')
            filtered_df.index = range(1, len(filtered_df)+1)
            st.write("Number of food resources:", len(filtered_df))
            st.dataframe(filtered_df[['Name', 'Distance', 'Address']], height=600)
        else:
            st.error('Invalid address. Please enter a valid address.')


#defining function that will describe all information included in the second subpage of the Interactive map page. This function will also refer to the second dataframe defined previously
def census(dataframe):
    #Providing header for the second subpage
    st.header('Comparing Food Insecurity Data of Crawford County\'s Census Tracts :world_map:')
    #embedding same CARTO interactive map I previously embedded in the first subpage using html codeblock.
    st.markdown('<iframe width="100%" height="800" src="https://clausa.app.carto.com/map/3e0786c8-41ed-401e-afbe-da2fcdc26046"></iframe>', unsafe_allow_html=True)

    st.markdown('<style>div.block-container{padding-top:lrem;}</style>',unsafe_allow_html=True)
    #adding markdown text describing the data in the second dataframe
    st.markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The table below displays food insecurity data within all census tracks of Crawford County, PA.')

    st.markdown(' #### **Some of the many types of variables in this table include:**') 
    st.markdown('- Total Population')
    st.markdown('- Housing Units')
    st.markdown('- Low income levels')
    st.markdown('- low access to food levels ')
    st.markdown('- low vehicle access levels')
    st.markdown('- Various types of populations')
    st.markdown('- Housing without SNAP benefits')

    st.markdown('## Crawford County\'s Census Tracts\' Food Insecurity Data')
    #Displaying the data table of the food insecurity data within Crawford County's Census Tracts originally collected by the USDA, and later manipulated by me
    st.write(dataframe)
    #using an html codeblock to overall fix the markdown text to display who originally made teh data
    st.markdown('<span style="font-size: small;">This data was compiled by the [USDA](https://www.ers.usda.gov/data-products/food-access-research-atlas/go-to-the-atlas/).</span>', unsafe_allow_html=True)
    #markdown text that tells the user disclaimers about how to use the interactive graph 
    st.markdown('#### Select a variable using the box below that (this is found in the table above) to plot on the y-axis, and any census tract name to plot on the x-axis.')
    st.markdown('<u>Click on any census track outlined on the map to find its Census Tract Name', unsafe_allow_html=True)
    st.markdown('<u>The variables geoid and CensusTract refer to the identification number to each census tract. These variables should be ignored.', unsafe_allow_html=True)
    st.markdown('(View an enhanced version of the graph using the "View Fullscreen" tool located on the right of the screen aligning with the top of the graph)')

    #Creating the selectbox for the y-axis (other variables), and the multiselect box for the x-axis (counties)
    tract_options = dataframe['CensusTractName'].unique().tolist()
    variable_two = st.selectbox('Select Y-Axis Variable', options=dataframe.columns)
    tracts = st.multiselect('Choose Census Tract Name to Compare with each other', tract_options, ['Census_Tract_One'])


    #Defining a select all variable that creates a checkbox for the user to select all census tract names
    select_all_checkbox_two = st.checkbox("Select All")

    #if statement that will update the multiselect box based on if the user clicks on the "Select All" checkbox
    if select_all_checkbox_two:
        tracts = tract_options

    #Filtering the dataframe based on the selected counties and other variables
    dataframe_selected = dataframe[dataframe['CensusTractName'].isin(tracts)]
    dataframe_selected = dataframe_selected.sort_values(by=variable_two)

    #Creating the bar chart using the px.bar function
    fig_two = px.bar(dataframe_selected, x="CensusTractName", y=variable_two, color="CensusTractName")

    #Changing title of chart if the "select all" checkbox is checked
    if select_all_checkbox_two:
        title_text_two = f'Comparing All Census Tracts Crawford County, PA of {variable_two}'
    else:
        title_text_two = f'Comparing  {" to ".join(tracts)} in Crawford County of {variable_two}'
    #updating the layout of the interactive bar chart
    fig_two.update_layout(
        title_text=title_text_two,
        xaxis_title='Census Tracts Names'
    )
    #Displaying the bar chart on the dashboard
    st.write(fig_two)
#if statement that serves as the 'main' function where the previously defined 'map' and 'census' functions are called. Each one uses its own dataframes as parameters.
if options == 'Map and Food Resource Radius':
    map(all_resources_df)
elif options == 'Map and Census Tract Data':
    census(dataframe)
