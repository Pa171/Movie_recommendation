#MOVIE_RECOMMENDATION_PROJECT

import numpy as np    
import pandas as pd 
import warnings     
               
warnings.filterwarnings('ignore')       

df = pd.read_csv('ml-100k/u.data',sep ='\t')
df.columns =['item_id','user_id','rating','timestamp']  
df.shape   

df['user_id'].nunique()                                              
df['item_id'].nunique() 
movie_titles = pd.read_csv('ml-100k/u.item',sep='|\')       
                                                                                       
movie_titles.shape 

movie_titles = movie_titles[[0,1]]           
movie_titles.columns = ['item_id','title']          

movie_titles.head()  
df=pd.merge(df,movie_titles, on='item_id') #merging on the basis of 'item_id'    

#Exploratory data analysis 
import matplotlib.pyplot as plt  
import seaborn as sns          #statiscal_library_of_python
sns.set_style('white')         

df.groupby('title').mean() 
df.groupby('title').mean()['rating'].sort_values(ascending = False) 
df.groupby('title').count()['rating'].sort_values(ascending = False)  

ratings = pd.DataFrame(df.groupby('title').mean()['rating'])  
ratings['number of ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])

ratings.sort_values(by = 'rating',ascending = False)
plt.figure(figsize=(10,6)) 
plt.hist(ratings['number of ratings'],bins=70)  
plt.show()  

plt.figure(figsize=(10,6))              
plt.hist(ratings['rating'],bins=70) 
plt.show()  

sns.jointplot(x='rating',y='number of ratings',data=ratings,alpha=0.5)

#Creating_Movie_Recommendation 
df.head() 
df.pivot_table(index='user_id',columns='title',values='rating') 
ratings.sort_values('number of ratings' , ascending=False) 

starwars_user_ratings = moviemat['star wars(1977)'] 

starwars_user_ratings.head()   

similar_to_star_wars = moviemat.corrwith(starwars_user_ratings) 
pd.DataFrame(similar_to_star_wars , columns=['Correlation'])      
corr_starwars.head()                                          
corr_starwars.dropna(inplace = True)           
corr_starwars.head()                                                              

corr_starwars = corr_starwars.join(ratings['number of rating'])  
corr_starwars[corr_starwars['number of ratings']>100].sort_values('correlation',ascending = False)  

corr_starwars.sort_values('correlation',ascending = False).head(10)  

def predict_movies(movie_name):
    movie_user_ratings = moviemat[movie_name] 
    similar_to_movie=moviemat.corrwith(star_user_ratings) 

    corr_movie = pd.DataFrame(similar_to_movie , columns = ['correleation']) 

    corr_movie.dropna(inplace =True) 
    corr_movie =corr_movie.join(ratings['number of ratings'])
    predictions = corr_movie[corr_movie['number of rating']>100].sort_values('correlation' , ascending = False) 
    return predictions

 x=predict_movies('Titanic 1977')
 print(x.head())                  






