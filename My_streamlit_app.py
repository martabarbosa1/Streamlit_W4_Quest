import pandas as pd
import streamlit as st
import seaborn as sns

st.title("W4_Quest_Streamlit")

page_names=['US', 'Europe', 'Japan']
page=st.radio('Please choose the region:', page_names)

link="https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars=pd.read_csv(link)
df_cars


if page == 'US':
    
    st.subheader('You selected US')
    cond_US=df_cars[df_cars['continent']==' US.']
    
    st.subheader('1) Distribution analysis')
    st.write('We analysed the distribution of each variable given.')
    
    fig, axes = plt.subplots(2, 4, figsize=(18, 10))

    ax=sns.histplot(data=cond_US, x='mpg', ax=axes[0,0])
    ax.set_xlabel("mpg")
    ax.set_ylabel("count")
    ax.set_title("mpg")

    ax=sns.histplot(data=cond_US, x='cylinders', ax=axes[0,1])
    ax.set_xlabel("cylinders")
    ax.set_ylabel("count")
    ax.set_title("cylinders")
    
    ax=sns.histplot(data=cond_US, x='cubicinches', ax=axes[0,2])
    ax.set_xlabel("cubicinches")
    ax.set_ylabel("count")
    ax.set_title("cubicinches")
    
    ax=sns.histplot(data=cond_US, x='hp', ax=axes[0,3])
    ax.set_xlabel("hp")
    ax.set_ylabel("count")
    ax.set_title("hp")
    
    ax=sns.histplot(data=cond_US, x='weightlbs', ax=axes[1,0])
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("count")
    ax.set_title("weightlbs")
    
    ax=sns.histplot(data=cond_US, x='time-to-60', ax=axes[1,1])
    ax.set_xlabel("time-to-60")
    ax.set_ylabel("count")
    ax.set_title("time-to-60")
    
    ax=sns.histplot(data=cond_US, x='year', ax=axes[1,2])
    ax.set_xlabel("year")
    ax.set_ylabel("count")
    ax.set_title("year")
    
    st.pyplot(fig)
    
    st.subheader('2) Correlation analysis')
    st.write('We only analysed the correlation of the variables that showed some degree of correlation')
    st.write('As you can see these variables show a trend between each other.')
        
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="mpg", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("mpg")
    ax.set_title("mpg x weightlbs")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="cubicinches", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("cubicinches")
    ax.set_title("weightlbs x cubicinches")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="hp", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("hp")
    ax.set_title("weightlbs x hp")
    st.pyplot(fig)
    
    
elif  page == 'Europe':
    st.subheader('You selected Europe')
    cond_Europe=df_cars[df_cars['continent']==' Europe.']
    
    st.subheader('1) Distribution analysis')
    st.write('We analysed the distribution of each variable given.')
    
    fig, axes = plt.subplots(2, 4, figsize=(18, 10))
    
    ax=sns.histplot(data=cond_Europe, x='mpg', ax=axes[0,0])
    ax.set_xlabel("mpg")
    ax.set_ylabel("count")
    ax.set_title("mpg")

    ax=sns.histplot(data=cond_Europe, x='cylinders', ax=axes[0,1])
    ax.set_xlabel("cylinders")
    ax.set_ylabel("count")
    ax.set_title("cylinders")
    
    ax=sns.histplot(data=cond_Europe, x='cubicinches', ax=axes[0,2])
    ax.set_xlabel("cubicinches")
    ax.set_ylabel("count")
    ax.set_title("cubicinches")
    
    ax=sns.histplot(data=cond_Europe, x='hp', ax=axes[0,3])
    ax.set_xlabel("hp")
    ax.set_ylabel("count")
    ax.set_title("hp")
    
    ax=sns.histplot(data=cond_Europe, x='weightlbs', ax=axes[1,0])
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("count")
    ax.set_title("weightlbs")
    
    ax=sns.histplot(data=cond_Europe, x='time-to-60', ax=axes[1,1])
    ax.set_xlabel("time-to-60")
    ax.set_ylabel("count")
    ax.set_title("time-to-60")
    
    ax=sns.histplot(data=cond_Europe, x='year', ax=axes[1,2])
    ax.set_xlabel("year")
    ax.set_ylabel("count")
    ax.set_title("year")
    
    st.pyplot(fig)
    
    st.subheader('2) Correlation analysis')
    st.write('We analysed the same correlation of variables as in the US.')
    st.write('As you can see the variables do not show such an evident trend as in the US, with more dispersion of the values.')
 
 
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="mpg", data=cond_Europe)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("mpg")
    ax.set_title("mpg x weightlbs")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="cubicinches", data=cond_Europe)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("cubicinches")
    ax.set_title("weightlbs x cubicinches")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="hp", data=cond_Europe)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("hp")
    ax.set_title("weightlbs x hp")
    st.pyplot(fig)  
    
else:
    st.subheader('You selected Japan')
    cond_Japan=df_cars[df_cars['continent']==' Japan.']
    
    st.subheader('1) Distribution analysis')
    st.write('We analysed the distribution of each variable given.')
    
    fig, axes = plt.subplots(2, 4, figsize=(18, 10))
    
    ax=sns.histplot(data=cond_Japan, x='mpg', ax=axes[0,0])
    ax.set_xlabel("mpg")
    ax.set_ylabel("count")
    ax.set_title("mpg")

    ax=sns.histplot(data=cond_Japan, x='cylinders', ax=axes[0,1])
    ax.set_xlabel("cylinders")
    ax.set_ylabel("count")
    ax.set_title("cylinders")
    
    ax=sns.histplot(data=cond_Japan, x='cubicinches', ax=axes[0,2])
    ax.set_xlabel("cubicinches")
    ax.set_ylabel("count")
    ax.set_title("cubicinches")
    
    ax=sns.histplot(data=cond_Japan, x='hp', ax=axes[0,3])
    ax.set_xlabel("hp")
    ax.set_ylabel("count")
    ax.set_title("hp")
    
    ax=sns.histplot(data=cond_Japan, x='weightlbs', ax=axes[1,0])
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("count")
    ax.set_title("weightlbs")
    
    ax=sns.histplot(data=cond_Japan, x='time-to-60', ax=axes[1,1])
    ax.set_xlabel("time-to-60")
    ax.set_ylabel("count")
    ax.set_title("time-to-60")
    
    ax=sns.histplot(data=cond_Japan, x='year', ax=axes[1,2])
    ax.set_xlabel("year")
    ax.set_ylabel("count")
    ax.set_title("year")
    
    st.pyplot(fig)
    
    st.subheader('2) Correlation analysis')
    st.write('We analysed the same correlation of variables as in the US.')
    st.write('As you can see the variables show the same trend in Japan.')
 
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="mpg", data=cond_Japan)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("mpg")
    ax.set_title("mpg x weightlbs")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="cubicinches", data=cond_Japan)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("cubicinches")
    ax.set_title("weightlbs x cubicinches")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="hp", data=cond_Japan)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("hp")
    ax.set_title("weightlbs x hp")
    st.pyplot(fig)  




#fig, ax = plt.subplots(figsize=(10, 4))
#ax = sns.regplot(x="weightlbs", y="mpg", data=df_cars)
#ax.set_xlabel("weightlbs")
#ax.set_ylabel("mpg")
#ax.set_title("mpgxweightlbs")
#st.pyplot(fig)
             





