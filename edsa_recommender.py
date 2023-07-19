# """

#     Streamlit webserver-based Recommender Engine.

#     Author: Explore Data Science Academy.

#     Note:
#     ---------------------------------------------------------------------
#     Please follow the instructions provided within the README.md file
#     located within the root of this repository for guidance on how to use
#     this script correctly.

#     NB: !! Do not remove/modify the code delimited by dashes !!

#     This application is intended to be partly marked in an automated manner.
#     Altering delimited code may result in a mark of 0.
#     ---------------------------------------------------------------------

#     Description: This file is used to launch a minimal streamlit web
# 	application. You are expected to extend certain aspects of this script
#     and its dependencies as part of your predict project.

# 	For further help with the Streamlit framework, see:

# 	https://docs.streamlit.io/en/latest/

# """
# # Streamlit dependencies
# import streamlit as st

# # Data handling dependencies
# import pandas as pd
# import numpy as np

# # Custom Libraries
# from utils.data_loader import load_movie_titles
# from recommenders.collaborative_based import collab_model
# from recommenders.content_based import content_model

# # Data Loading
# title_list = load_movie_titles('resources/data/movies.csv')

# # App declaration
# def main():

#     # DO NOT REMOVE the 'Recommender System' option below, however,
#     # you are welcome to add more options to enrich your app.
#     page_options = ["Recommender System","Solution Overview"]

#     # -------------------------------------------------------------------
#     # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
#     # -------------------------------------------------------------------
#     page_selection = st.sidebar.selectbox("Choose Option", page_options)
#     if page_selection == "Recommender System":
#         # Header contents
#         st.write('# Movie Recommender Engine')
#         st.write('### EXPLORE Data Science Academy Unsupervised Predict')
#         st.image('resources/imgs/Image_header.png',use_column_width=True)
#         # Recommender System algorithm selection
#         sys = st.radio("Select an algorithm",
#                        ('Content Based Filtering',
#                         'Collaborative Based Filtering'))

#         # User-based preferences
#         st.write('### Enter Your Three Favorite Movies')
#         movie_1 = st.selectbox('Fisrt Option',title_list)   # [14930:15200]
#         movie_2 = st.selectbox('Second Option',title_list[1:]) #[25055:25255]
#         movie_3 = st.selectbox('Third Option',title_list[2:]) #[21100:21200]
#         fav_movies = [movie_1,movie_2,movie_3]

#         # Perform top-10 movie recommendation generation
#         if sys == 'Content Based Filtering':
#             if st.button("Recommend"):
#                 try:
#                     with st.spinner('Crunching the numbers...'):
#                         top_recommendations = content_model(movie_list=fav_movies,
#                                                             top_n=10)
#                     st.title("We think you'll like:")
#                     for i,j in enumerate(top_recommendations):
#                         st.subheader(str(i+1)+'. '+j)
#                 except:
#                     st.error("Oops! Looks like this algorithm does't work.\
#                               We'll need to fix it!")


#         if sys == 'Collaborative Based Filtering':
#             if st.button("Recommend"):
#                 try:
#                     with st.spinner('Crunching the numbers...'):
#                         top_recommendations = collab_model(movie_list=fav_movies,
#                                                            top_n=10)
                        
#                     st.title("We think you'll like:")
#                     for i,j in enumerate(top_recommendations):
#                         st.subheader(str(i+1)+'. '+j)
#                 except:
#                     st.error("Oops! Looks like this algorithm does't work.\
#                               We'll need to fix it!")


#     # -------------------------------------------------------------------

#     # ------------- SAFE FOR ALTERING/EXTENSION -------------------
#     if page_selection == "Solution Overview":
#         st.title("Solution Overview")
#         st.write("Describe your winning approach on this page")

#     # You may want to add more sections here for aspects such as an EDA,
#     # or to provide your business pitch.


# if __name__ == '__main__':
#     main()



"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

#Data Visualisation 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from recommenders.content_based import data_preprocessing
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
Ratings= pd.read_csv('resources/data/ratings.csv')
# train= pd.read_csv('resources/data/train.csv')
movies= pd.read_csv('resources/data/movies.csv')
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "Insights", "About us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    
    
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")
        
        
        # User_Id = st.selectbox('User Id',title_list)
        # Movie_Id = st.selectbox('Movie Id',title_list)
        

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.'
    if page_selection == "Insights":
        st.title("Exploratory Data Analysis")
        # st.image("resources\imgs\countplot.png",use_column_width=True)
        st.image("resources\imgs\EDA.jpg",use_column_width=True)
        
        
        mov= st.selectbox('Choose the movie you want to explore',title_list[1:15200])
        
        #Title of the graph
        st.write(f'The distribution of {mov} ratings')
        
        #Combining two dataframes
        Concat_df = pd.merge(movies, Ratings, on='movieId', how='inner')
        
        #Masking the selected movie:
        Concat_df1=Concat_df[Concat_df['title'] == mov]
        
        if mov == "":
            # Calculate the count of each rating
            rating_counts = Ratings['rating'].value_counts().sort_index()
        else:
            rating_counts= Concat_df1['rating'].value_counts().sort_index()

        # Create a bar graph using Plotly
        fig = go.Figure(data=[go.Bar(x=rating_counts.index, y=rating_counts.values)])

        # Customize the layout
        fig.update_layout(
        title="Users Movies Rating",
        xaxis_title="Rating",
        yaxis_title="Count"
        )

        # Render the figure in Streamlit using st.plotly_chart()
        st.plotly_chart(fig)
    
        
        st.header("Genre of the movie")
        
        movies['genres']=movies['genres'].str.replace("|", " ")
        tabl=movies[movies['title']==mov]
        text = ' '.join(tabl['genres'])
        words = text.split()
        for i in words:
            st.write(i)
            
    if page_selection == "About us":
        st.header("About us")
        
        st.title("Our Mission")
        with st.expander('Click here to read more'):
            st.write("Our mission is to harness the power of artificial intelligence to transform data into actionable insights, enabling businesses to make informed decisions and drive meaningful outcomes. We strive to develop cutting-edge predictive models and recommender systems that leverage advanced algorithms and data analytics techniques. By analyzing vast amounts of data, our aim is to empower organizations to unlock hidden patterns, optimize operations, and enhance customer experiences, ultimately driving innovation and growth")
        
        st.title("Our Team")
        
        st.image('resources/imgs/team.jpeg',use_column_width=True)
        
   
        

if __name__ == '__main__':
    main()

