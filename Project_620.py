#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


st.title('DS620 FINAL PROJECT')


# In[3]:


@st.cache
def load_data(nrows):
    data = pd.read_csv('Average Temperature Anomalies.csv',nrows=nrows)
    return data

@st.cache
def load_Rice2_data(nrows):
    data = pd.read_csv('Rice2.csv',nrows=nrows)
    return data

@st.cache
def load_Wheat2_data(nrows):
    data = pd.read_csv('Wheat2.csv',nrows=nrows)
    return data


# In[4]:


df1 = pd.read_csv('Average Temperature Anomalies.csv',index_col=0)
df2 = pd.read_csv('Rice2.csv',index_col=0)
df3 = pd.read_csv('Wheat2.csv',index_col=0)
df4 = pd.read_csv('4 Countries Bar.csv',index_col=0)
df6 = pd.read_csv('Morocco Wheat vs Temp.csv',index_col=0)
df7 = pd.read_csv('Morocco Rice vs Temp.csv',index_col=0)
df8 = pd.read_csv('Morocco Potato vs Temp.csv',index_col=0) 
df9 = pd.read_csv('Senegal Rice vs Temp.csv',index_col=0)
df10 = pd.read_csv('Senegal Potato vs Temp.csv',index_col=0)
df11 = pd.read_csv('South Africa Wheat vs Temp.csv',index_col=0)
df12 = pd.read_csv('South Africa Rice vs Temp.csv',index_col=0)
df13 = pd.read_csv('South Africa Potato vs Temp.csv',index_col=0)
df14 = pd.read_csv('Niger Wheat vs Temp.csv',index_col=0)
df15 = pd.read_csv('Niger Rice vs Temp.csv',index_col=0)
df16 = pd.read_csv('Niger Potato vs Temp.csv',index_col=0)
df17 = pd.read_csv('Potato2.csv',index_col=0)


# In[5]:


df5 = pd.DataFrame({
    'Countries': ['Morocco','Senegal','South Africa', 'Niger'],
            'Potato':[30.13,22.11,31.07,22.69],
            'Rice':[7.79,4.38,2.79,2.960],
            'Wheat':[2.58,2.42,3.71,3.39]
})


# In[6]:


if st.checkbox('Abstract'):
    st.markdown('Although climate change could occur naturally based on weather patterns and solar cycles, it is a consensus amongst the scientific community that the vast majority of climate change has occurred because of human activities. Three of the most basic necessities a human needs to survive are shelter, food, and water. With temperatures rising annually, what type of effect will it have on our survival? This research focuses on the aspect of crop production in the continent of Africa which is the second largest continent based on population as well as size.', unsafe_allow_html=False)
    st.markdown('The first step in conducting our research was to visualize global temperatures. The GISTEMP index is an estimate of global surface temperature change. Once the data was visualized, it is visible that average temperature anomalies were below 0 prior to 1939. However it rose sharply until 1944 which surprisingly is within the time span of World War 2. After 1939, the anomalies decreased to -0.18 in 1950 but since then there has been a gradual rise in temperature anomalies. ')


#st.subheader('Raw data')
    #st.write(df1.head(),df2.head(),df3.head(),df4.head(),df5.head(),df6.head(),df7.head(),df8.head(),df9.head(),
             #df10.head(),df11.head(),df12.head())


# In[7]:


#st.markdown('Although climate change could occur naturally based on weather patterns and solar cycles, it is a consensus amongst the scientific community that the vast majority of climate change has occurred because of human activities. Three of the most basic necessities a human needs to survive are shelter, food, and water. With temperatures rising annually, what type of effect will it have on our survival? This research focuses on the aspect of crop production in the continent of Africa which is the second largest continent based on population as well as size.', unsafe_allow_html=False)


# In[8]:


#st.markdown('The first step in conducting our research was to visualize global temperatures. The GISTEMP index is an estimate of global surface temperature change. Once the data was visualized, it is visible that average temperature anomalies were below 0 prior to 1939. However it rose sharply until 1944 which surprisingly is within the time span of World War 2. After 1939, the anomalies decreased to -0.18 in 1950 but since then there has been a gradual rise in temperature anomalies. ')


# # 1st

# In[9]:


st.markdown('The continent of Africa produces many crops across 54 counties. This research focuses on the crops Rice, Wheat, and Potatoes. Data was collected on which countries produce the most tonnes of the crops per hectare which is a unit of measure equal to 100 acres.')


# In[10]:


st.subheader('Average Temperature Anomalies from 1880 - 2016')


# In[11]:


st.markdown('Looking at the total annual production of Wheat, Rice, and Potatoes from 1961 - 2016, it was found that even though there were some years where production had decreased, for the most part production for each crop has increased.')


# In[12]:



df1.reset_index(inplace =True)


# In[13]:


df1.head()


# In[14]:


fig = px.line(df1,
        x='Year',
        y=['Mean'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 2nd

# In[15]:


st.subheader('Top 5 Rice Producing Countries in Africa - 2018')


# In[16]:


st.markdown('Looking at the production of Rice, the top 5 countries in 2018 production were Morocco (7.79), Senegal (4.38), Madagascar (4.34), Kenya (4.25), and Rwanda (3.51). These 5 countries make up almost 32% of all Rice production in Africa.')


# In[17]:


df2.reset_index(inplace =True)
df2.head(6)


# In[18]:


fig = px.pie(df2, values='Rice - Tonnes per Hectare', names='Entity')
st.plotly_chart(fig)


# # 3rd

# In[19]:


st.subheader('Top 5 Wheat Producing Countries in Africa - 2018')


# In[20]:


st.markdown('Looking at the production of Wheat, the top 5 countries in 2018 production were Egypt (4.65), Zambia (4.57), South Africa (3.71), Niger (2.96), and Sudan (2.63). These 5 countries make up almost 39% of all Wheat production in Africa. ')


# In[21]:


df3.reset_index(inplace =True)
df3.head()


# In[22]:


fig = px.pie(df3, values='Wheat - Tonnes per Hectare', names='Entity')
st.plotly_chart(fig)


# # 4th

# In[23]:


st.subheader('Top 5 Potato Producing Countries in Africa - 2018')


# In[24]:


st.markdown('Looking at the production of Potatoes, the top 5 countries in 2018 production were Algeria (31.09), South Africa (31.07), Morocco (30.13), Niger (22.69), and Senegal (22.11). These 5 countries make up almost 37% of all Potato production in Africa')


# In[25]:


df17.reset_index(inplace =True)
df17.head()


# In[26]:


fig = px.pie(df17, values='Potato - Tonnes per Hectare', names='Entity')
st.plotly_chart(fig)


# # 5th

# In[27]:


st.subheader('Crop Production by Country - 2018')


# In[28]:


st.markdown('')


# In[29]:


df4.reset_index()
df4.head()


# In[30]:


fig = px.bar(df5,
        x='Countries',
        y=['Potato','Rice','Wheat'],
             barmode='group')
st.plotly_chart(fig)


# In[31]:


st.markdown('The hypothesis for this experiment was that as temperature anomalies increased, there would be a negative impact on crop production. However it was realized that many other socioeconomic factors would play a role in crop production.')


# In[32]:


st.markdown('Looking at the total annual production of Wheat, Rice, and Potatoes from 1961 - 2016, it was found that even though there were some years where production had decreased, for the most part production for each crop has increased. ')


# In[33]:


st.subheader('In the line charts below you can see the behavior of the average temperature spanned 55 years and how it affected the production of the crops.')


# # 6th

# In[34]:


st.subheader('Morocco Wheat Production vs Temperature Anomalies 1961 - 2016')


# In[35]:


st.markdown('In Morocco, the production of wheat gradually increases throughout the years although you can see many ups and downs in production.')


# In[36]:


df6.reset_index(inplace =True)
df6.head()


# In[37]:


fig = px.line(df6,
         x='Year',
        y=['Mean Temp','Morocco Wheat - tonnes per hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
)
st.plotly_chart(fig)


# # 7th

# In[38]:


st.subheader('Morocco Rice Production vs Temperature Anomalies 1961 - 2016')


# In[39]:


st.markdown('For the production of rice in Morocco, in the late 60s the production increased almost double then went back down in the 70s & 80s. In the late 80s you can see it start going back up gradually, ultimately having a positive increase in the 2000’s.  ')


# In[40]:


df7.reset_index(inplace =True)
df7.head()


# In[41]:


fig = px.line(df7,
        x='Year',
        y=['Mean Temp','Rice - Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 8th

# In[42]:


st.subheader('Morocco Potato Production vs Temperature Anomalies 1961 - 2016')


# In[43]:


st.markdown('Production of potatoes in Morocco had a slow steady growth throughout the years but ended up producing 3 times its products by 2010 again as the temperature slowly increased.')


# In[44]:


df8.reset_index(inplace =True)
df8.head()


# In[45]:


fig = px.line(df8,
        x='Year',
        y=['Mean Temp','Potatos Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 9th

# In[46]:


st.subheader('Senegal Rice Production vs Temperature Anomalies 1961 - 2016')


# In[47]:


st.markdown('In Senegal, Rice production increased gradually throughout the years when in 2010 it multiplied its production by 4. ')


# In[48]:


df9.reset_index(inplace =True)
df9.head()


# In[49]:


fig = px.line(df9,
         x='Year',
        y=['Mean Temp','Rice - Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 10th

# In[50]:


st.subheader('Senegal Potato Production vs Temperature Anomalies 1961 - 2016')


# In[51]:


st.markdown('Production of potatoes’ in Senegal started with a decrease for the first decade until the late 70s when it began to gradually build its production quickly. ')


# In[52]:


df10.reset_index(inplace =True)
df10.head()


# In[53]:


fig = px.line(df10,
        x='Year',
        y=['Mean Temp','Potatos Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 11th

# In[54]:


st.subheader('South Africa Wheat Production vs Temperature Anomalies 1961 - 2016')


# In[55]:


st.markdown('In South Africa, with the temperature dropping and rising gradually, the production of wheat followed similarly to the behavior of the weather. While ultimately increasing its production almost 4 times. ')


# In[56]:


df11.reset_index(inplace =True)
df11.head()


# In[57]:


fig = px.line(df11,
        x='Year',
      y=['Mean Temp','Wheat - tonnes per hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 12th

# In[58]:


st.subheader('South Africa Rice Production vs Temperature Anomalies 1961 - 2016')


# In[59]:


st.markdown('Rice in South Africa took a spike in production in the early 70s but it didn’t change again until the late 80s when production dropped and continued to gradually ascend throughout the years.')


# In[60]:


df12.reset_index(inplace =True)
df12.head()


# In[61]:


fig = px.line(df12,
        x='Year',
        y=['Mean Temp','Rice - Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 13th

# In[62]:


st.subheader('South Africa Potato Production vs Temperature Anomalies 1961 - 2016')


# In[63]:


st.markdown('The production of potatoes in South Africa gradually rose until about mid to late 90s when it then didn’t increase or decrease for the remainder of the years. ')


# In[64]:


df13.reset_index(inplace =True)
df13.head()


# In[65]:


fig = px.line(df13,
        x='Year',
        y=['Mean Temp','Potatos Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 14th

# In[66]:


st.subheader('Niger Wheat Production vs Temperature Anomalies 1961 - 2016')


# In[67]:


st.markdown('Niger’s temperature behavior is similar to South Africas, where in the first decade it was up and down, then in the late 70s it began to gradually rise throughout the years.  Wheat production started rising, when ultimately reaching its highest point of production in the mid 90s. ')


# In[68]:


df14.reset_index(inplace =True)
df14.head()


# In[69]:


fig = px.line(df14,
        x='Year',
        y=['Mean Temp','Wheat - tonnes per hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 15th

# In[70]:


st.subheader('Niger Rice Production vs Temperature Anomalies 1961 - 2016')


# In[71]:


st.markdown('Rice production in Niger didn’t start gradually rising until around the late 70s, and although it took a hit in the 90s, it has continued to increase its production after. ')


# In[72]:


df15.reset_index(inplace =True)
df15.head()


# In[73]:


fig = px.line(df15,
        x='Year',
        y=['Mean Temp','Rice - Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# # 16th

# In[74]:


st.subheader('Niger Potato Production vs Temperature Anomalies 1977 - 2016')


# In[75]:


st.markdown('Production of potatoes in Niger you can see started in a downhill and stayed still until about the beginning of the 90s where it skyrocketed two and a half times its production.  It began to slowly decrease in production from the early 90s to early 2000’s then it increased gradually after. ')


# In[76]:


df16.reset_index(inplace =True)
df16.head()


# In[77]:


fig = px.line(df16,
        x='Year',
        y=['Mean Temp','Potatos Tonnes per Hectare'])

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(fig)


# In[78]:


st.subheader('Conclusion')


# In[79]:


st.markdown(' climate change will continue to occur throughout years to come.  Human activity will continue to affect climate change daily and cause temperature anomalies yearly.  The good news is that as temperatures rise we can be sure that production of crops will continue to rise gradually.  As seen in the charts above there was mainly always an increase in production even if at times it decreased for a few years.  Although climate change can affect us in many ways like strong heat waves where it can be devastating to work out in the sun, crops are essential to our lives.  As we were able to see the production of crops in Africa rise, I can assume the same for other continents in the world.  Not only rice, wheat and potatoes but other crops as well.  ')


# In[ ]:




