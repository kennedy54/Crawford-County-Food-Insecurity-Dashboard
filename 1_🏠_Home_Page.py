# Importing Libraries
import streamlit as st
import os
import streamlit.components.v1 as components

#setting page configuration by initializing that this is the home page, setting the emoji to the "house" emoji, and making the page a wide format
st.set_page_config(page_title="Home", page_icon=":house:", layout='wide')


GA_TRACKING_CODE = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-EJ8WRG15YL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-EJ8WRG15YL');
</script>
"""

st.markdown(f'<head>{GA_TRACKING_CODE}</head>', unsafe_allow_html=True)

#Inserting Google tag configurator
#google_analytics_script = """
#<!-- Google tag (gtag.js) -->
#<script async src="https://www.googletagmanager.com/gtag/js?id=G-EJ8WRG15YL"></script>
#<script>
#  window.dataLayer = window.dataLayer || [];
#  function gtag(){dataLayer.push(arguments);}
#  gtag('js', new Date());

#  gtag('config', 'G-EJ8WRG15YL');
#</script>
#"""

#Injecting Google Analytics Google tag HTML code into header of the page
#st.markdown(f'<head>{google_analytics_script}</head>', unsafe_allow_html=True)

#Inserting Meta Tag to verify on Google
meta_tag = '<meta name="google-site-verification" content="V1_5EMiai8CgyLAwlhM8xCp-Onwe9oVseHi1hZ0RJBE" />'

#Injecting the Meta tag into the header of the page
st.markdown(f'<head>{meta_tag}</head>', unsafe_allow_html=True)

#HTML verification file if the "verification" query parameter is present
verification_file_path = 'googlebafe0a76f48bf64c.html'

#Defining query params variable
query_paramets = st.query_params()

#Checking for the verification of the query parameter
# Serve the HTML verification file
if query_paramets.get("verification") == ['true']:
    if os.path.exists(verification_file_path):
        with open(verification_file_path, 'r') as file:
            st.write(file.read(), unsafe_allow_html=True)
    else:
        st.error("Verification file not found.")

else:
    #making the page's title
    st.title(":house: Crawford County Food Insecurity Dashboard Home Page")
    #adding CSS codeblock to modify elements in the text
    st.markdown('<style>div.block-container{padding-top:irem;}</style>',unsafe_allow_html=True)
    #Adding markdown description that describes the purpose and functionality of the whole dashboard
    st.markdown('### Welcome to the Crawford County Food Insecurity Dashboard')
    st.markdown('The purpose of this dashboard is to educate policymakers and those struggling with food insecurity about the current state of this issue within Crawford County, Pennsylvania. This dashboard will visually display interactive food resources, food deserts, statistics, and trends.')
    st.markdown('According to the United States Department of Agriculture (USDA), Pennsylvania fell beneath the 11.2% national average of food insecure households from 2020 - 2022, with 10.1% of all households within the state being food insecure. However, not every county kept the state from breaching the national average. In 2021, Crawford County ranked eleven out of sixty-seven counties in PA for having high food insecurity. 9,830 people (11.8%) of the population was food insecure, according to Feeding America. By the end of 2023, 9,898 people (12%) of the population will be food insecure, according to the County Health Rankings and Roadmaps. This conveys that although PA as a whole has relatively low food insecurity (falling beneath the national average), there are still counties within the state that are continuing to suffer. Over time, counties such as Crawford may continue to rise in food insecurity percentages and cause PA to be pushed over the national average.  ')
    st.markdown('This dashboard will produce interactive plots, graphs, charts to display current trends of food insecurity variables such as: cost per meal, child food insecurity, or adult food insecurity.')
    st.markdown('An interactive map will also be used to visually display food support resources such as qualified food banks, supermarkets, fast food establishments, food deserts, low income areas, and low vehicle access areas.')
    st.markdown('The data used in the visualizations derive from the Crawford County Food Alliance (CCFA), USDA, County Health Rankings and Roadmaps, Stacker, Feeding America, and DATAUSA.')

    st.markdown('#### This dashboard includes pages of:')
    st.markdown('- General Comparative Analyses') 
    st.markdown('- The Food Insecurity Map')
    st.markdown('- A Contact Page')

    # Creating Sidebear to select different pages of dashboard
    st.sidebar.success("Page Navigation")

    #Creating sitemap for the dashboard
    #sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
    #<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    #    <url>
    #        <loc>https://crawford-county-food-insecurity-dashboard.streamlit.app/</loc>
    #        <lastmod>2024-08-20</lastmod>
    #        <changefreq>weekly</changefreq>
    #        <priority>1.0</priority>
    #    </url>
    #</urlset>
    #'''

    #if statement that serves the sitemap when the "sitemap" query parameter is present
    #if "sitemap" in query_paramets:
    #    st.write(sitemap_content)

    #Adding option to download the sitemap of the dashboard
    # st.markdown("## Download Sitemap")
    # st.download_button(label="Download sitemap.xml", data=sitemap_content, file_name="sitemap.xml", mime='text/xml')
