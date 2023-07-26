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
import os
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
Ratings= pd.read_csv('resources/data/ratings.csv')
# train= pd.read_csv('resources/data/train.csv')
movies= pd.read_csv('resources/data/movies.csv')
# App declaration
#
def display_team_member(name, description, designation, image_path):
    st.image(image_path, width=200)
    st.markdown(f"<h1 style='font-size:25px'><b>{name}</b></h1>", unsafe_allow_html=True)
    st.write(f"*{designation}*")
    st.write(description)
    st.write("---")

import base64
def add_bg_image(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image('resources/imgs/jj.jpg')

log = "resources/imgs/logo.jpg"


cola, mid, colb = st.columns([25,1,40])
with mid:
        st.image(log, width=150)

def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Approach","Try Something different", "Insights", "About us"]
    with st.sidebar:
        st.image(log, width=250)

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
    
    if page_selection == "Try Something different":
        st.subheader("Feel like watching something different?")
        st.image("resources/imgs/some.jpg",width=750)
        st.markdown("Click on the button below for a random recommendation")
        st.write(" ")

        col1, col2, col3 = st.columns([0.26, 0.3, 0.1])
        with col1:
            pass
        with col2:
            btn = st.button("Click me")
        if btn:
            sample = movies.sample(10)  # movies.sample(5)['title'].iloc[1]
            for i in range(10):
                st.subheader(str(i+1)+'. '+ sample['title'].iloc[i])
        with col3:
            pass


    if page_selection == "Approach":
        st.title("Team Overview")
        st.write("Our cross-functional team consisting of data scientists, machine learning engineers, and DevOps specialists embarked on building an advanced movie recommender system and deploying it on Amazon Web Services (AWS). The primary objective was to create a personalized movie recommendation platform that delivers accurate suggestions to users based on their viewing history and preferences")
        st.write(" ")
        st.title("Data collection")
        st.write("The MovieLens dataset is meticulously maintained by the esteemed GroupLens research group in the Department of Computer Science and Engineering at the University of Minnesota. This group ensures the data's quality and reliability, making it a trusted resource for recommender system research and development.")
        st.write("In addition to the MovieLens data, our team legally acquired and scraped movie content data from IMDB. This allowed us to enrich the dataset with valuable movie information, such as genres, release years, and plot summaries. The inclusion of this supplementary data provided a more comprehensive view of the movies and further enhanced the quality of our recommender system.")
        st.write(" ")
        st.title("Data Preprocessing ")
        st.write("The data was preprocessed to handle missing values, duplicates, and outliers. Text data, such as movie descriptions and user comments, was tokenized, cleaned, and converted into TF-IDF vectors")
        st.write(" ")
        st.title("Model Development")
        st.write("During our movie recommender system development, we explored various models, and Singular Value Decomposition (SVD) stood out as the top performer. SVD's ability to capture latent features and handle sparse data led to accurate and personalized movie recommendations. We fine-tuned the SVD model, achieving excellent results and exceeding performance expectations. Our team remains committed to exploring innovative approaches for delivering the best movie recommendations to our users. ")
        st.write(" ")
        st.title("Model Deployment on AWS")
        st.write("Furthermore, we successfully deployed our SVD-based movie recommender as a Streamlit web application on AWS. This deployment allowed us to provide a user-friendly and interactive platform for our customers to receive personalized movie recommendations. The AWS infrastructure ensures scalability, reliability, and efficient performance, enabling us to deliver a seamless user experience to a wide audience. We are delighted with the outcome and are continuously working to enhance our recommender system to cater to the evolving needs of our users.")


        

    if page_selection == "Insights":
        st.title("Exploratory Data Analysis")
        st.image("resources\imgs\EDA.jpg",use_column_width=True)
        tab1, tab2 = st.tabs(['Movie info', 'Exploratory Data Analysis'])
        with tab1:
            data = data_preprocessing(10)
            data = data.dropna()
            mov = st.selectbox('Choose the movie you want to explore',data["title"])
            
            #Title of the graph
            st.write(f'The distribution of {mov} ratings')
            
            
            #Combining two dataframes
            Concat_df = pd.merge(data, Ratings, on='movieId', how='inner')
            
            #Masking the selected movie:
            Concat_df1 = Concat_df[Concat_df['title'] == mov]
            
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
        
            Movie=data[data['title']==mov]

            st.header("Genre of the movie")
            
            text = Movie['genres'].iloc[0]
            words = text.split()
            for i in words:
                st.write(i)
            
            
            st.header("Director")
            st.write(Movie['director'].iloc[0])

            st.header("Budget")
            
            st.write(str(Movie['budget'].iloc[0]))

            st.header("Run time")
            run = str(round(Movie['runtime'].iloc[0])) + " minutes"
            st.write(run)

            st.header("Cast")
            text = Movie['title_cast'].iloc[0]
            words = text.split(',')
            for i in words:
                st.write(i)
        with tab2:
            st.subheader("Exploratory Data Analysis")
            select = st.selectbox("Insights", ("Users Movies Rating","Top 20 from movies viewed by users","The top ten directors who produced most movies","Distribution of Genres"))

            if select == "Users Movies Rating":
                st.image('resources/imgs/user_movie.png', width = None)
                st.write(" ")
                st.write("The graph above illustrates that the distribution of ratings by users is left-skewed, indicating that the majority of users tend to rate movies positively. The most frequent rating observed in the data is 4.0, which suggests that many users found the movies they viewed enjoyable, entertaining, and of good quality.Additionally, the presence of ratings above 4.0 implies that some users highly praised certain movies. These higher ratings can serve as positive endorsements and may influence other users to consider watching those movies ")

            if select == "Top 20 from movies viewed by users":
                st.image('resources/imgs/top_20.png', use_column_width=True)
                st.write(" ")
                st.write("The most viewed movies by users is shawshank Redemption which was produced in 1994, this movie tells a powerful and emotionally captivating story that explores themes of hope, friendship, redemption, and the resilience of the human spirit.This movie may still resonate with with audiences of different generations, thus a continous increase of viewers over time. The second and third most viewed movies were also produced in 1994. In 1994, there was a noticeable shift in the movie industry, as some new faces were able to bring in fresh films that had people buzzing in a hurry. Thus, 1994 is regarded as the best movie year of all time and this may have accounted to three most viewed movies to be those produced in 1994.")

            if select == "The top ten directors who produced most movies":
                st.image('resources/imgs/top_ten_direc.png', width = None)
                st.write(" ")
                st.write("The treemap above shows the top ten directors who directed most movies on the give data. Both Woody Allen and Luc Besson directed most movies. Woody Allen is a well-known American filmmaker, writer, and actor. He has had a prolific career spanning several decades and has made significant contributions to the world of cinema. Luc Besson is a French filmmaker, writer, and producer known for his distinct visual style and his contributions to the action and science fiction genres.")

            if select == "Distribution of Genres":
                st.image('resources/imgs/genres.png', width = None)
                st.write(" ")
                st.write("The first most common genre is drama. The high frequency of this genre may be accounted to the fact that most directors always want to connect with the viewer’s feelings, thus producing drama genre that are usually very emotional. It is important to note that these movies that have a drama genre can still span through other genres because directors often want to create unique storytelling experiences and cater to a broader audience. The second most common genre is comedy. With Comedy, the directors aim to provide a source of joy and amusement, offering a break from daily routines and stresses. ")
            


    


            
    if page_selection == "About us":
       
        
        st.title("About Us")
        
        st.write("Welcome to Kinnetic.inc! We are a leading data-driven solutions provider, "
                "empowering businesses across various industries with actionable insights and innovative "
                "data-driven strategies. Our team of highly skilled data scientists, analysts, and machine "
                "learning experts is dedicated to unlocking the true potential of data and transforming it "
                "into tangible business value.")
        
        st.subheader("Our Vision:")
        st.write("At Kinnetic.inc, our vision is to revolutionize how businesses harness the power of "
                "data to make informed decisions, optimize processes, and drive growth. We believe that "
                "data is the cornerstone of success in today's fast-paced and competitive world, and we are "
                "committed to being at the forefront of the data science revolution.")
        
        st.subheader("Our Mission:")

        st.write("Our mission is to harness the power of artificial intelligence to transform data into actionable"
                 " insights, enabling businesses to make informed decisions and drive meaningful outcomes."
                 " We strive to develop cutting-edge predictive models and recommender systems that leverage advanced"
                 " algorithms and data analytics techniques. By analyzing vast amounts of data, our aim is to empower "
                 "organizations to unlock hidden patterns, optimize operations, and enhance customer experiences, ultimately driving innovation and growth")
        
        st.subheader("What Sets Us Apart:")
        st.write("- Expertise: Our team comprises seasoned data scientists and domain experts who possess a "
                "deep understanding of various industries. We bring a wealth of experience to every project "
                "we undertake, ensuring top-notch solutions tailored to your specific needs.")
        st.write("- Innovation: Embracing innovation is in our DNA. We continuously explore the latest "
                "advancements in data science, artificial intelligence, and machine learning to deliver "
                "creative and game-changing solutions that stay ahead of the curve.")
        st.write("- Client-Centric Approach: Your success is our success. We pride ourselves on building "
                "strong, long-lasting partnerships with our clients. Our client-centric approach focuses on "
                "understanding your unique challenges and delivering solutions that directly address your "
                "business goals.")
        st.write("- Data Privacy and Security: Trust is fundamental to our relationships. We adhere to the "
                "highest standards of data privacy and security to protect your sensitive information and "
                "maintain the utmost confidentiality.")
        
        st.subheader("Our Services:")
        st.write("- Data Analytics and Visualization: Uncover hidden insights within your data and transform "
                "them into compelling visualizations that facilitate informed decision-making.")
        st.write("- Machine Learning Solutions: Leverage the power of machine learning algorithms to predict "
                "outcomes, automate processes, and gain a competitive edge.")
        st.write("- Predictive Analytics: Anticipate future trends and behavior patterns to make proactive "
                "decisions and stay ahead of the competition.")
        st.write("- Data Engineering: Ensure the integrity and efficiency of your data pipelines, from data "
                "collection to storage and processing.")
        
        st.subheader("Why Choose Kinnetic.inc:")
        st.write("When you partner with Kinnetic.inc, you gain a trusted ally in your journey towards "
                "data-driven success. We combine technical expertise with a deep understanding of your "
                "business to deliver tailor-made solutions that fuel your growth and maximize your ROI.")
        
        
        ####
        st.title("Our Team")

        team_members = [
        {"name": "Tshifhumulo Mapasa", "description": "Tshifhumulo Mapasa is the CEO of our data science company. With a Ph.D. in Machine Learning and a profound passion for extracting valuable insights from complex datasets, Tshifhumulo brings a wealth of experience to the leadership role. With over a decade of industry experience, she has successfully led numerous data science projects across diverse domains.", "designation": "Chief Executive Officer"},
        {"name": "Akule Cekwana", "description": "Akule Cekwana is a seasoned data scientist with a strong background in predictive analytics and data mining. With a master's degree in Data Science, she brings expertise in developing scalable and efficient machine learning models. Akule Cekwana excels in feature engineering, algorithm selection, and model validation, ensuring the team delivers accurate and actionable insights to drive informed decision-making.", "designation": "Senior Data Scientist"},
        {"name": "Busisiwe Socatsha", "description": "Busisiwe Socatsha is a dynamic and innovative Data Engineer, leveraging his expertise to architect and build robust data pipelines and scalable infrastructure. With a deep understanding of big data technologies and distributed systems, he excels at optimizing data workflows to ensure efficient data processing and storage.", "designation": "Data Engineer"},
        {"name": "Tshegofatso Seabi", "description": "Tshegofatso Seab a Ph.D. in Computer Science, specializing in Natural Language Processing and Text Mining. He is an expert in extracting information from unstructured textual data and developing cutting-edge language models. Tshegofatso Seab's research background and expertise in deep learning techniques enable him to build robust solutions for text analysis, sentiment analysis, and document classification.", "designation": "Mananger"},
        {"name": "Mpho Manthada", "description": "Mpho Manthada is a highly skilled and results-driven Data Engineer with a passion for designing and implementing cutting-edge data solutions. With a solid foundation in computer science and data management, Alexandra excels in building efficient data pipelines and data warehouses to support complex analytics and business intelligence initiatives..", "designation": "Data Engineer"},
        {"name": "Mojalefa Motloung", "description": "Mojalefa Motloung is a highly skilled and motivated Machine Learning Engineer, bringing his expertise to the forefront of developing intelligent and innovative machine learning solutions. With a strong background in computer science, mathematics, and statistical modeling, Mojalefa is adept at designing and implementing algorithms that drive predictive analytics and data-driven decision-making.", "designation": "Machine Learning Engineer"},]
        
        num_members = len(team_members)
        rows = num_members // 3 + (num_members % 3 > 0)

        for i in range(rows):
            cols = st.columns(3)
            for j in range(3):
                index = i * 3 + j
                if index < num_members:
                    with cols[j]:
                        # image_filename = team_members[index]['name'].replace(' ', '_').lower() + ".jpeg"
                        # image_path = os.path.join("team_images", image_filename)
                        # permissions = 0o644  # Example: read and write for the owner, read for others
                        # os.chmod(image_path, permissions)  # Change file permissions
                        if team_members[index]["name"] == "Mojalefa Motloung":
                            imag = "resources/imgs/lefas.jpg"
                        elif team_members[index]["name"] == "Tshifhumulo Mapasa":
                            imag = "resources/imgs/T.jpg"
                        elif team_members[index]["name"] == "Akule Cekwana":
                            imag = "resources/imgs/ak.jpg"
                        elif team_members[index]["name"] == "Busisiwe Socatsha":
                            imag = "resources/imgs/Busi.jpg"
                        elif team_members[index]["name"] == "Tshegofatso Seabi":
                            imag = "resources/imgs/jo.jpg"
                        elif team_members[index]["name"] == "Mpho Manthada":
                            imag = "resources/imgs/mp.jpg"
                        display_team_member(
                            team_members[index]["name"],
                            team_members[index]["description"],
                            team_members[index]["designation"],
                             imag#"resources/imgs/b.png" #image_path
                        )
        
        

        st.title("Contact Us")
    
        st.write("For any inquiries or questions, please feel free to reach out to us:")
        
        st.subheader("Email:")
        st.write("contact@Kinnetic.inc.com")
        
        st.subheader("Phone:")
        st.write("+27 (123) 456-7890")
        
        st.subheader("Address:")
        st.write(" Kinnetic.inc")
        st.write("123 Main Street")
        st.write("City, State, Zip Code")
        
        st.subheader("Social Media:")
        st.write("Twitter: @Kinnetic.inc")
        st.write("LinkedIn: linkedin.com/company/Kinnetic.inc")
        st.write("Facebook: facebook.com/Kinnetic.inc")
        
   
        

if __name__ == '__main__':
    main()

