
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import base64


st.title("Webscraping  of Top 100 Adventure Movies in IMDB")
st.image("Downloads\\lord.jpg", use_column_width = True)



# it use to read and upload the file

uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files = True)
for uploaded_file in uploaded_files:
     data = pd.read_csv(uploaded_file)
     st.write("filename:", uploaded_file.name)
     st.write(data)


# def st_display_pdf(pdf_file):
#     with open(pdf_file, "rb") as f:
#         base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
#     pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">' 
#     st.markdown(pdf_display, unsafe_allow_html=True)

# st_display_pdf("Downloads\\Adventure.pdf")


# creating expander

def main():
    menu = ["None", "Link", "Info", "IMDB Video", "Search"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Search':
        st.header("Choose your favourite movies by Year")
        data['release_date'] = pd.to_datetime(data['release_date'])

        with st.expander("Search by Year"):
            movie_year = st.number_input("Year", 1990, 2022)
            df_for_year = data[data['release_date'].dt.year == movie_year]
            st.dataframe(data)

        col1, col2, col3 = st.columns(3)

        with col1:
            with st.expander("Title"):
                for movie in data['movie_name'].tolist():
                    st.success(movie)

        with col2:
            with st.expander("Ratings"):
                for movie1 in data['rating'].tolist():
                    st.write(movie1)

        with col3:
            with st.expander("Genre"):
                for movie2 in data['genre'].tolist():
                    st.write(movie2)

    elif choice == 'Info':
        st.header("The things to webscrape from IMDB are")
        st.markdown("""

                        ###### 1. Movie name\n
                        ###### 2. Description\n
                        ###### 3. Release Date\n
                        ###### 4. Director Name\n
                        ###### 5. Rating\n
                        ###### 6. Duration\n
                        ###### 7. Genre\n
                        ###### 8. Stars (Actors)\n
                        ###### 9. Filming Dates

                        """)
    
    elif choice == 'Link':
        st.title('Top 100 IMBb adventure movies')
        st.markdown('This App shows some visualiztions on the top 100 adventure movies on [IMDb](https://www.imdb.com/).')
        st.image("Downloads\\lord5.jpg", use_column_width = True)
        
    elif choice == 'IMDB Video':
        st.title('Video about IMDB')
        st.markdown("IMDb is the world's most popular and authoritative source for movie, TV and celebrity content. Find ratings and reviews for the newest movie and TV shows.")
        video_file = open('Downloads\\myvideo.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    else:
        print("no")


main()



# it used to make selectbox

data_select = st.sidebar.selectbox("Select your Visualization", ("None", "Movie ratings by year of release", "Movie in top 100 by Actor", "Movie in top 100 by Director"))
k = st.sidebar.selectbox('Minimum number of movies played', [1, 2, 3, 4, 5])
movies = st.sidebar.selectbox('Movies to Recommended', ("None", "Top Actor name", "Top Directo name", "Top Movie name"))



# function

def load_data(data_select):
    if data_select == "Movie ratings by year of release":
        st.title("Visualization of Movie ratings by year of release")
        
        fig = px.scatter(
                   data,  x="release_date", y="rating", color= 'votes', template='seaborn', 
                   title='Movie rating over time', 
                   labels={"release_date": "Year of release",
                                 "rating": "Movie rating"}
                                 )

        st.plotly_chart(fig, use_column_width = True)

    elif data_select == "Movie in top 100 by Actor":
        st.title("Visualization of Movie in top 100 by Actor")
        
        movie_actors_dict = {}
        for movie, actors in zip(data['movie_name'], data['actors']):
            movie_actors_dict[movie] = actors.split(',')
            
        movie_actors = pd.DataFrame(movie_actors_dict).melt(var_name= 'movie', value_name='actors')

        # actors that played at least k number of movies
        nb_movies_per_actor = movie_actors['actors'].value_counts()

        v = nb_movies_per_actor [nb_movies_per_actor >= k]
        actor_movie = pd.DataFrame({'actor': v.index, 'number_movies': v.values})


        fig = px.bar(
                     actor_movie, x = "actor", y = "number_movies",
                            template = 'seaborn',
                            title = f'Actors that played at least {k} movies', 
                            labels = {"actor": "Actor's name",
                                    "number_movies": "Number of movies"}
                                    )

        st.plotly_chart(fig) 
    
    elif data_select == "Movie in top 100 by Director":
        st.title("Visualization of Movie in top 100 by Director")
        nb_movies_per_director = data['director'][data['director'].str.split(',').apply(len) == 1].value_counts()
        v = nb_movies_per_director [nb_movies_per_director >= k]
        director_movie = pd.DataFrame({'director': v.index, 'number_movies': v.values})


        fig = px.bar(
                     director_movie, x = "director", y = "number_movies",
                            template = 'seaborn',
                            title = f'Directors that played at least {k} movies', 
                            labels = {"director": "Director's name",
                                    "number_movies": "Number of movies"}
                                    )

        st.plotly_chart(fig) 
        

    else:
        print("no")

    
load_data(data_select)


# select your box

st.title("Are you waiting for Adventure?")
agree = st.checkbox('Yes')

if agree:
     st.write('**Here comes your favourite adventure**')
     st.write(":smile:"*20)
     st.write('**Go to Movies to Recommended at the sidebar**')
     st.snow()

     
agree1 = st.checkbox('No')

if agree1:
      st.write("**No Adventure**")
      st.write("Come back again")
      st.write(":wave:"*20)


# function

def load(movies):
    if movies == "Top Actor name":
        st.title("Ryan Reynolds")
        st.image("Downloads\\lord2.jpg", use_column_width = True)
        
    elif movies == "Top Directo name":
        st.title("Matthew Vaughn")
        st.image("Downloads\\lord3.jpg", use_column_width = True)
        
    elif movies == "Top Movie name":
        st.title("Avengers: infinity war")
        st.image("Downloads\\lord4.jpg", use_column_width = True)
        
    else:
        print("no")


load(movies)



# rating the work

st.subheader("Give some heart for us")
my_range = range(1, 6)
number = st.select_slider("Choose a number", options = my_range, value = 1)
st.write("You given us %s hearts:" %number, number*":heart:")


if number == 5:
    st.balloons()

