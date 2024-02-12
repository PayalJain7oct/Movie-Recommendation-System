This is a streamlit web application using Jupyter notebook for movie recommendation system. It follows a comprehensive approach to provide personalized suggestions to users.
Streamlit is utilized to create an intuitive web interface, allowing users to effortlessly navigate and interact with the recommendation system. Different steps involved in this are:     
•	Loading the dataset:
This project loads the dataset of the movies and credits into Panda DataFrames.
•	Merging data frames:
The two DataFrames are merged on the 'title' column to combine information about movies.
•	Feature Engineering:
The 'cast' column is manipulated to extract the first three elements, assuming these are the main cast members.
We then collapsed spaces in names ensuring proper formatting so that it gives correct prediction of movie based on our input.
•	Vectorization:
Converted tags into matrix of token counts using CountVectorizer by specifying the maximum number of features to be considered.
•	Similarity calculation:
Calculated cosine similarity between movie vectors, obtaining a similarity matrix.
•	Recommendation function:
It takes a movie title as input and prints the top 5 recommended movies based on similarity.Then the processed data and the similarity matrix is saved to files.
The Streamlit application takes a movie ID as input, calculates recommendations and sends a request to The Movie Database (TMDb) API to get information about the movie,
returning the names and URL for the movie poster. TMDb is a platform for the community which helps users to contribute and edit data related to movies and television content.
It is a whole collection of huge data like details about movie plots, information of cast and crew members, release dates, genres, posters, trailers, and more.
•	Cleaning:
Missing values, duplicate and irrelevant columns are handled efficiently.
•	Feature Selection:
Essential features like genres, keywords, cast, crew are extracted.
•	Text Processing:
Tokenization, stemming and vectorization of textual data collected.
•	Notification Feature for Recent Releases: 
The incorporation of a notification system for new movie releases in the last seven days enhances user engagement and decision-making capability, ensuring that users stay informed about the latest content.
