#Importing Libraries
import streamlit as st
import plotly.express as px
import pandas as pd

#setting page configuration by initializing that this is the general comparative analysis page, setting the emoji to the "chart with the upwards trend" emoji, and making the page a wide format 
st.set_page_config(page_title=" General Comparative Analysis", page_icon=":chart_with_upwards_trend:", layout='wide')

#creating sidebar to select comparative analysis subpages for when a user is on the Comparative Analysis main page
options = st.sidebar.radio('General Comparative Analysis of Crawford County, PA', options=['General Food Insecurity Data in PA Counties', 'General Crawford County Food Insecurity Data'])

#creating title for every subpage
st.title(":chart_with_upwards_trend: General Comparative Analysis of Crawford County's Food Insecurity Data")

#Importing data and creating first dataframe
df = pd.read_csv("data/Crawford_County_General_Food_Insecurity_Data.csv")

#Importing data for second subpage and creating dataframe
dataframe = pd.read_csv("data/General_Food_Insecurity_Data_Two.csv")

#defining the general function, which calls the first dataframe previously created and contains all information that will be displayed on the first subpage
def general(df):
    #adding CSS codeblock to modify elements in the text
    st.markdown('<style>div.block-container{padding-top:lrem;}</style>',unsafe_allow_html=True)
    # making title and bio for the dashboard
    st.markdown('### Comparing Crawford County to all other counties in Pennsylvania')
    #adding informative markdown text that describes the first graph
    st.markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The table below displays food insecurity data of all counties within Pennsylvania from 2021 - 2022. When looking at Crawford County, it ranks 46 out of 67 counties in PA of the highest child food insecurity rates (where 1 is the lowest rate and 67 is the highest rate), and 41 out of 67 counties of highest overall food insecurity rates (where 1 is the lowest rate and 67 is the highest rate).')
    st.markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pennsylvania has a child food insecurity rate of 13.1%, which ranks 32 highest among all states [(Stacker)](https://stacker.com/pennsylvania/counties-highest-rate-food-insecure-children-pennsylvania). Pennsylvania also had an overall food insecurity rate of 12%, which ranks 19 highest of all states [(America\'s Health Rankings)](https://www.americashealthrankings.org/explore/measures/food_insecurity_household/PA).')
    st.markdown(' #### **Variables in the table include:**') 
    st.markdown('- Counties in PA')
    st.markdown('- Child Food Insecurity Rate (%)')
    st.markdown('- Child Food Insecurity (Total)')
    st.markdown('- Percent of Child Food Insecurity Higher or Lower (-) than National Average')
    st.markdown('- Overall Food Insecurity Rate (%)')
    st.markdown('- Percent of Overall Food Insecurity Higher or Lower (-) than National Average')
    st.markdown('- Annual Food Budget Shortfall (in US dollars)')
    st.markdown('- Average Cost per Meal (in US dollars)')

    st.markdown('## Pennsylvania\'s County Food Insecurity Data')
    #Displaying the first dataframe of the food insecurity data within Pennsylvania collected by Stacker
    st.write(df)

    #adding html specification to markdown text to display where the data came from
    st.markdown('<span style="font-size: small;">This data was compiled by [Stacker](https://stacker.com/pennsylvania/counties-highest-rate-food-insecure-children-pennsylvania) who used data from [Feeding America](https://www.feedingamerica.org/research/map-the-meal-gap/overall-executive-summary).</span>', unsafe_allow_html=True)
    #markdown text that tells the user to select a variable. These variables are also the same ones found in the table previously displayed
    st.markdown('#### Select a variable to plot on the y-axis and any county to plot on the x-axis.')
    #adding markdown disclaimer text on how the graph is viewed if more than 25 counties are selected to view at once
    st.markdown('(If "Select All" is checked, or there are more than 25 counties selected, view the entire graph using the "View Fullscreen" tool located on the right of the screen aligning with the top of the graph)')

    #Creating the selectbox for the y-axis (other variables), and the multiselect box for the x-axis (counties)
    counties_options = df['Counties'].unique().tolist()
    variable = st.selectbox('Select Y-Axis Variable', options=df.columns)
    counties = st.multiselect('Choose a County to Compare with Crawford County', counties_options, ['Crawford'])

    #Defining a select all variable that selects all variables fro y-axis
    select_all_checkbox = st.checkbox("Select All")

    #if statement that will update the multiselect box based on if the user clicks on the "Select All" checbox
    if select_all_checkbox:
        counties = counties_options

    #Filtering the dataframe based on the selected counties and other variables
    df_selected = df[df['Counties'].isin(counties)]
    df_selected = df_selected.sort_values(by=variable)

    #Creating the bar chart using the px.bar function
    fig = px.bar(df_selected, x="Counties", y=variable, color="Counties")
    #, range_y=[0,67]
    #updating the layout of the bar chart

    #Changing title of chart if the "select all" checkbox is checked
    if select_all_checkbox:
        title_text = f'Comparing Crawford County to All Counties in PA of {variable}'
    else:
        title_text = f'Comparing to {",  ".join(counties)} in PA of {variable}'
    #updaiting bar chart layout
    fig.update_layout(
        title_text=title_text,
        xaxis_title='Counties'
    )
    #Displaying the bar chart on the dashboard
    st.write(fig)

# Code for getting county populations
#c = Census("8d17c59c29eb878185ab3218f2f0b5c2c5dc787d")

#def get_county_fips(county_name):
#    state_fips = '42'
#    counties = c.sf1.state_county('NAME', state_fips, Census.ALL)
#    for county in counties:
#        if county['NAME'] == county_name:
#            return county['state'] + county['county']
#    return None

#def get_population(county_names):
#    populations = {}
#    for county_name in county_names:
#        county_fips = get_county_fips(county_name)
#        if county_fips:
#            population_data = c.sf1.state_county(('NAME', 'P001001'), '42', county_fips)
#            if population_data:
#                populations[county_name] = population_data[0]['P001001']
#            else:
#                populations[county_name] = None
#    return populations


#st.markdown('# Searching Pennsylvania County Population')

#selected_counties = st.selectbox('Select a county in Pennsylvania', [
#    'Adams County',
#    'Allegheny County',
#    'Armstrong County',
#    'Beaver County',
#    'Bedford County',
#    'Berks County',
#    'Blair County',
#    'Bradford County',
#    'Bucks County',
#    'Butler County',
#    'Cambria County',
#    'Cameron County',
#    'Carbon County',
#    'Centre County',
#    'Chester County',
#    'Clarion County',
#    'Clearfield County',
#    'Clinton County',
#    'Columbia County',
#    'Crawford County',
#    'Cumberland County',
#    'Dauphin County',
#    'Delaware County',
#    'Elk County',
#    'Erie County',
#    'Fayette County',
#    'Forest County',
#    'Franklin County',
#    'Fulton County',
#    'Greene County',
#    'Huntingdon County',
#    'Indiana County',
#    'Jefferson County',
#    'Juniata County',
#    'Lackawanna County',
#    'Lancaster County',
#    'Lawrence County',
#    'Lebanon County',
#    'Lehigh County',
#    'Luzerne County',
#    'Lycoming County',
#    'McKean County',
#    'Mercer County',
#    'Mifflin County',
#    'Monroe County',
#    'Montgomery County',
#    'Montour County',
#    'Northampton County',
#    'Northumberland County',
#    'Perry County',
#    'Philadelphia County',
#    'Pike County',
#    'Potter County',
#    'Schuylkill County',
#    'Snyder County',
#    'Somerset County',
#    'Sullivan County',
#    'Susquehanna County',
#    'Tioga County',
#    'Union County',
#    'Venango County',
#    'Warren County',
#    'Washington County',
#    'Wayne County',
#    'Westmoreland County',
#    'Wyoming County',
#    'York County'
#])

#if st.button('Get Population'):
#    populations = get_population(selected_counties)
#    if populations:
#        for county, population in populations.items():
#            if population is not None:
#                st.write(f"The population of {county} is {population}.")
#            else:
#                st.write("The Population data is not available for this selected county.")

#defining environment function that will contain all information needed for the second subpage of the comparative analysis page. It will also contain the second graph, and it calls the second datafrmae previously defined.
def environment(dataframe):
    st.markdown('<style>div.block-container{padding-top:lrem;}</style>',unsafe_allow_html=True)
    st.markdown('### Comparing Very Low Food Insecurity, Regular Food Insecurity, and the Food Environmental Index in Crawford County, PA from 2014 - 2022. ')
    #markdown text that describes the data that will be presented on the graph
    st.markdown('The data below decribes the state of very low food insecurity, regular food insecurity, and the food environmental index within Crawford County. It specifically looks at the time frame between 2014 - 2022. This not only shows how much each variable has changed within almost a decade, but primarily the state of these variables pre and post the COVID-19 pandemic.')
    st.markdown('It can be seen that in pre-COVID years that the overall state of food insecurity in Crawford County has not been ideal, as there have been many positive and negative trends. However, as our society began to feel the effects of the pandemic in 2021, it is evident that very low food insecure and regular food insecure populations began to rise drastically, and the food environmental index had gone down. This proves that the state of food insecurity in Crawford County is increasingly becoming worse as our society continues to feel the after-effects of the pandemic.')
    st.markdown('#### **Variables in the table include:**')
    st.markdown('- Year')
    st.markdown('- Very Low Food Insecurity')
    st.markdown('- Food Insecurity')
    st.markdown('- Food Environment Index')

    st.markdown('## General Crawford County Food Insecurity Data')
    #sorting the dataframe so it shows from top to bottom the year from smallest to largest
    sorted_dataframe = dataframe.sort_values(by="Year")
    #sorting the dataframe so it is numbered correctly top to bottom, 1-9 (there are 9 rows excluding the row that displays the name of the variables)
    sorted_dataframe.reset_index(drop=True, inplace=True)
    sorted_dataframe.index += 1
    #Displaying the data table of the food insecurity data within Crawford County's Census Tracts originally collected by the USDA, and later manipulated by me
    st.write(sorted_dataframe)
    #using an html codeblock to overall fix the markdown text to display who originally made teh data
    st.markdown('<span style="font-size: small;">This data was compiled by [DATAUSA](https://datausa.io/profile/geo/crawford-county-pa?dietAndExerciseOptions=indicator_5&healthBehaviorsOptions=dietAndExerciseOption) Who used data from [County Health Rankings and Roadmaps](https://www.countyhealthrankings.org/).</span>', unsafe_allow_html=True)

    st.markdown('#### Select a variable using the box below (that is found in the table above) to plot on the y-axis.')

    options = [col for col in dataframe.columns if col != "Year"]
    #Creating the selectbox for the y-axis (other variables), and the multiselect box for the x-axis (counties)
    variable_one = st.selectbox('Select Y-Axis Variable', options=options)

    #Creating the bar chart using the px.line_chart function
    fig_one = px.line(dataframe, x="Year", y=variable_one)

    #Changing title of chart if the "select all" checkbox is checked
    title_text_one = f'Comparing {variable_one} from 2014 - 2022 in Crawford County, PA'
    #updating the layout of the interactive line chart
    fig_one.update_layout(
        title_text=title_text_one,
        xaxis_title='Year'
    )
    #Displaying the line chart on the dashboard
    st.plotly_chart(fig_one)

#if statement that serves as the 'main' function where the previously defined 'general' and 'environment' functions are called. Each one uses their own dataframes as paramters.
if options == 'General Food Insecurity Data in PA Counties':
    general(df)
elif options == 'General Crawford County Food Insecurity Data':
    environment(dataframe)
