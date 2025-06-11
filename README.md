# HOW TO RUN

1. make sure you have all the files "combined.csv", "data_cleaning.py", "exceptions.py", "file_handling.py", "movie-back.png", "plotting.py", "sample.py", "summarize.py".
2. paste all the files in the same directory.
3. pip install pandas streamlit matplotlib
4. run "data_cleaning.py".
5. open directory in cmd prompt and type "streamlit run sample.py".
6. for the summary txt file, run "summarize.py".

# PopViz

This is an Exploratory Data Analysis (EDA) of a movies dataset picked up from Kaggle. The original data that we downloaded were in separate files categorized by genres (the "dataset" file). combine.py is a simple script written to combine all those csv files into one (combined.csv). Hereafter, the combined.csv file is used as the main data source file. 

Data cleaning is performed on the dataset using Pandas library. We dropped any fishy rows with null values, and unnecessary columns. The format of the release date column was changed from inconvenient American format to the pleasant and understandable non-American one, and to datetime datatype. That part was tricky. This file uses the modules we created for Exception Handling and File Handling.

The exceptions.py file contains all the user defined [by yours truly(plural)] exceptions that may occur during file handling, data cleaning, plotting, etc. We also created a user defined exception extending another user defined exception which was unexpectedly possible. wow programming! 

Module file_handling.py as the name suggests, for loading and saving data during cleaning. User defined exceptions called.

The marvellous plotting.py contains the Matplotlib code functions for several graphs. We created some normal graphs you'd expect to see in a generic movies dataset visualization like for ratings by genre, ratings histogram, runtime over years, runtime histogram, etc. Now the annoying part is over.

Coming to the central file that joins everything together, the interface, sample.py (yes we left it at just the sample stage). Introduces, shows plots bla bla, but the interesting part here was the filter searching implemented (thanks krishita!), meaning we could basically filter data by categories like genre and release year.

As a footnote, summarize.py is an unnecessary file that generates a "movie_summary.txt" file that highlights key data details like total number of movies present in the dataset, the timespan covered, etc and insights like most common genre, movie with the longest/shortest runtime, highest/lowest rated movie of all time and all that sort of information. This file does not contribute to sample.py.

Note that all of the information given is only limited to the dataset we downloaded and we do not claim to show data including all of the movies that were ever released, thank you.