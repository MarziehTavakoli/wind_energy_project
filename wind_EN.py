import streamlit as st
from PIL import Image
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly
import plotly.express as px


st.set_page_config(page_title='Energy Analyse',page_icon='Ripg',layout='wide')
st.title("Wind_Energy")
imag1=Image.open('OIP.jpg')
st.image(imag1)
st.subheader('Wind energy is currently the biggest climate-friendly energy source.In order to produce enough CO2-free electricity for Germany, wind energy capacity must be increased by at least 9 gigawatts per year by 2030.To achieve these targets, increasing the size and capacity of  wind energy plants will be vital.')
st.write('--------------------------------------------------------------------')

col1,col2=st.columns([1,2])
col1.subheader('The aim of this project is to use the analysis of wind meteorological data to show which regions and cities in Germany have more potential for wind energy production.')

col2.image('https://th.bing.com/th/id/R.6fd37b272e1285d908a423644ee059d0?rik=Qc6Xl1IHEceTCQ&riu=http%3a%2f%2fwonderfulengineering.com%2fwp-content%2fuploads%2f2014%2f09%2fwind-turbine-8.jpg&ehk=FL0MjVUXNlIVJ1w7Hag1vhO1XeAENKUeonkAkRW1bBM%3d&risl=&pid=ImgRaw&r=0')

st.write('--------------------------------------------------------------------')
col1,col2=st.columns([1,1])
col1. write('Data source for the project')
col1.write('www.visualcrossing.com')
col2.write('The original data from website  include all elements of weather. but my focus in this project is on wind elements.Threr are separate data frame for each capital city in Germany.')

st.markdown('-------------------------------------------------------------------------')
#Hamburg-------------------------
def main():
    st.subheader('Here you can see the various influencing factors that were measured in the city of Hamburg last year:')
    df =pd.read_csv('Hamburg.csv')
    d1=df.head(10)
    st.table(d1)
    st.subheader('Plotting with Hamburg data')
   
    fig1= px.bar(df,x='dates' , y = 'wind_speed', width=1000, height=400)   
    st.plotly_chart(fig1) 

if __name__ == '__main__': 
    main()
st.write('---------------------------------------------')      
def main():      
    st.subheader('The three measured of wind factors for each capital cities are:')
    
    bnt1=st.button('wind Direction')
    if bnt1:
       st.write('The wind direction indicates the direction from where the wind is blowing from. The units of the wind direction is degrees from north. The value ranges from 0 degrees (from the North), to 90 degrees (from the east), 180 degrees (from the south), 270 (from the west) back to 360 degrees.The direction of the wind is taken into account during the installation of the turbine, so it is not analyzed in this project')
       st.write('Today, new wind turbines are not fixed and adjust according to the wind direction.')
       from windrose import WindroseAxes
       from matplotlib import cm

       direction = [350.4, 39.2, 272.2, 301.1, 290.1, 235.4, 255, 198.2, 95.9,
                     48.2, 281.5, 185.2, 221.1, 262.7, 264.2, 150.7, 54.9, 209.8,
                     256.7, 255, 202.6, 213.3, 215.9, 224.1, 232.4, 297.2, 299.3, 266.9, 195, 219, 195.4]
       speed = [16.8, 11.3, 26.6, 32.2, 31.6, 19.1, 38.4, 14.1, 14.1, 21.9, 28.8,
                   25.2, 38, 39.7, 29.8, 37.3, 23.7, 20, 17, 18.9, 19.5, 32.7, 30.3,
                    33.7, 31.7, 24.2, 34.6, 16.6, 27, 27.4, 18.2]
       fig, ax = plt.subplots(figsize=(8,6))
       ax = WindroseAxes.from_ax(fig=fig)
       ax.bar(direction, speed, normed=True, opening=0.8, edgecolor='w', bins=10, cmap=cm.plasma_r)
       st.pyplot(fig)
     
           
    bnt2=st.button('wind Gust')
    if bnt2:
        
       st.write('Wind gust is the maximum wind speed measures over a short amount of time (typically less than 20 seconds).We need stability in the wind! ')
       st.write('The amount of wind gust has a high variance. We cannot count on it')
       df= pd.read_csv('combind.csv')
       st.dataframe(df.describe())
       
    bnt3=st.button('wind_speed')
    if bnt3:
       st.latex('\Huge\color{blue} Power  of  wind(W)  =  1/2  ρ  A  V^3 ')
       
       st.markdown('wind physics Basic Facts :')
       st.markdown('* **ρ :** It is almost equal to one. so it doesnt matter much. ')
       st.markdown('* **A :** area and Bigger turbin more power! ')
       st.markdown('* **V :** Faser wind lots more power! ') 
       
if __name__ == '__main__': 
    main()
st.write('---------------------------------------------')
st.header('The Analysis for all German capital cities in charts:')
#max---------------
def main():
    st.subheader('Maximum Wind speed for each  city in last  year')
    df2=pd.read_csv('max_table.csv')
    
    fig2= px.bar(df2,x='city_name' , y = 'maximum speed',color='city_name',
                 width=800, height=400)
       
    st.plotly_chart(fig2) 
if __name__ == '__main__':
  main()
#max_ranking------------     
st.subheader('Ranking')
df3=pd.read_csv('total_max.csv')
fig3=px.bar(df3,x='max(wind_speed)', y= 'city_name') 
st.plotly_chart(fig3)

#sum--------------
st.write('plotting the sum of speed in a year')
df4=pd.read_csv('result_table.csv')
fig4=px.scatter(df4,  x='city_name', y='Sum of speeds in a year', color='city_name')
st.plotly_chart(fig4)

#sum_ranking-------------------
st.write('Rnking')
df5=pd.read_csv('sorted_result_table.csv')
fig5=px.bar(df5,x='Sum of speeds in a year', y='city_name')
st.plotly_chart(fig5)
#conclusion--------------
st.write('conclusion')
col1,col2=st.columns([1,1])
col1.write('The highest wind speed:')

col1.markdown('* **1** _Erfurt' )
col1.markdown('* **2** _Keil' )
col1.markdown('* **3** _Breman' )
col1.markdown('* **4** _Saarbrücken' )
col1.markdown('* **5** _Hamburg' )

col2.write('The maximum amount of wind:')

col2.markdown('* **1** _Erfurt')
col2.markdown('* **2** _Bremen')
col2.markdown('* **3** _Düsseldorf')
col2.markdown('* **4** _Keil')
col2.markdown('* **5** _Hamburg')

#line_chart---------------------
df=pd.read_csv('combind.csv')
fig=px.line(df, x='dates', y='wind_speed',color='city_name',
           height=600, width=1100)
st.write(fig)


#animated_1------------------
st.write('Wind speed over time_1')
df= pd.read_csv('combind.csv')
fig = px.scatter(df , x ='city_id' ,size ='wind_speed',  color ='city_name',
                  hover_name='city_name' , log_x=True , size_max=50 ,
                  animation_frame= 'dates' , animation_group='city_name')

fig.update_layout(width=800)
st.write(fig)

