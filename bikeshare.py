""" Explore US Bikeshare Data In Python

In this project, I used Python to explore data related to  bike share systems for three major cities in the United States:
Chicago, New York City, and Washington. I wrote a code to import the  data and answer interesting questions about it by computing descriptive
statistics. The script takes in raw input from the user; to create an interactive experience in the terminal to present these statistics.
"""

__author__ = "Mohamed Abdel-Gawad Ibrahim"
__contact__ = "muhammadabdelgawwad@gmail.com"
__phone__ =  "+201069052620"
__phone__ =  "+201147821232"
__date__ = "25th April, 2021"

import time # Time module to convert timestamp column from string to python time object
from datetime import datetime # To get the current date and time, and assign them to the created folder name, where we will save the graphs of the statistics
import pandas as pd # open source data analysis and manipulation tool
import numpy as np # used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices
import matplotlib.pyplot as plt # matplotlib.pyplot is a module in Matplotlib, and it is a collection of functions that make matplotlib work like MATLAB
import os # provides functions for interacting with the operating system. we will use it to create a directory to save the plot figures inside it

#pd.set_option('display.max_columns', None) # Specify maximum columns width of pandas dataframe when we print them in the terminal window.

# A global dictionary where we set a string - the city name - as the key, and the corresponding raw data file as the value.
CITY_DATA = { 'chicago': 'chicago.csv', # A quick note: .csv stands for Comma Seperated Values
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_user_resp(q_string):

    while True: # Foolproof loop to capture if the user want to print general information about the dataframe
        print('-'*80)
        user_input = input( "\n" + q_string + " Type 'Yes' or 'No': ").lower()
        if user_input in ['yes', 'no']: # Check if we captured a correct answer
            break
        else:
            print('Sorry, wrong answer..')

    return user_input


def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!') # print a welcome message

    # First Filter: City

    while True: # Foolproof Loop to capture a correct city name from the user. it breaks when the user enters a city that exists in the keys of CITY_DATA dictionary
        # A user may enter different formats of the city names, so I used .lower() to convert user's input to lowercase, similar to the keys in CITY_DATA dictionary
        city = input('Please enter a city name from (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA.keys(): # check if we captured correct city name from the user to exit the Foolproof loop
            break
        else: # Display a message to the user when they enter a wrong city name, before looping to capture their input again
            print('Sorry, wrong answer..')

    # Second Filter: month

    # A list variable includes all available months in the raw data. 'all' value specify that the user doesn't want to filter on a specific month.
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True: # Foolproof Loop to capture a correct month name from the user. it breaks when the user enters a month that exists in the months variable.
        # Capture month name from the user, and convert it to lowercase, similar to the names in the months variable.
        month = input('Please enter a month you want to investigate in, from January to June, or all (All, January, February, ... , June): ').lower()
        if month in months: # check if we captured correct month name from the user to exit the Foolproof loop.
            break
        else: # Display a message to the user when they enter a wrong month name, before looping to capture their input again.
            print('Sorry, wrong answer..')

    # Third Filter: Day

    # A list variable includes all available days in the week. 'all' value specify that the user doesn't want to filter on a specific day.
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True: # Foolproof Loop to capture a correct day name from the user. it breaks when the user enters a day that exists in the days variable.
        # Capture a day name from the user, and convert it to lowercase, similar to the items in days variable.
        day = input('Please enter a day you want to investigate in (All, Monday, Tuesday, ... Sunday): ').lower()
        if day in days: # check if we captured correct day name from the user to exit the Foolproof loop.
            break
        else: # Display a message to the user when they enter a wrong day name, before looping to capture their input again.
            print('Sorry, wrong answer..')

    print('-'*40) # Display dashes separator indicating we finished taking the inputs we need.
    return city, month, day # Return the inputs we captured from the user



def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) # dataFrame variable to store the raw data based on the city that the user has chosen.

    df.rename(columns = {'Unnamed: 0' : 'User ID'}, inplace = True) # Rename The First Column As It has no name in the original dataframe

    print('\nThe first 5 columns in the raw data are:')
    print(df.head()) # Print The first 5 Rows of the raw data

    df['Start Time'] = pd.to_datetime(df['Start Time']) # Convert the 'Start Time' column which is a string, to a Python Date time object.

    df['month'] = df['Start Time'].dt.month # create a new column 'month' from 'Start Time' column (stored as integers from 1 to 12)

    df['day_of_week'] = df['Start Time'].dt.day_name() # create a new column 'day_of_week' from 'Start Time' column (stored as strings e.g. sunday)

    # filter by month if applicable:

    if month != 'all': # check if the user chose to filter on a specific month (any value except 'all')
        # List of all available months where their indexes reflect the number of the month (february --> index = 2). We will use this list
        # to convert the month that the user has chosen, to its corresponding number; to match the month format in the 'month' column.
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) # Convert the month that the user has chosen, to its corresponding number, and store it back again in the month variable.
        df = df[df['month'] == month] # Filter the dataFrame, from the 'month' column, on the month that the user has chosen.

    # filter by day of week if applicable:

    if day != 'all': # check if the user chose to filter on a specific day (any day value except 'all')
        df = df[df['day_of_week'] == day.title()]  # Filter the DataFrame, from the 'day_of_week' column, on the day of week that the user has chosen.

    return df # Return the DataFrame after filtering on City, Month, and Day of Week



def time_stats(df):

    """
    Displays statistics on the most frequent times of travel

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time() # saves current time; to calculate the execution time of this function.

    popular_month = df['month'].mode()[0] # Find the most common month (from January to June)
    print('\n Most Frequent Start Month: ', popular_month)

    popular_day = df['day_of_week'].mode()[0] # find the most common day of week.
    print('\n Most Frequent Start Day of Week: ', popular_day)


    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour # First create 'hour' column from 'Start TIme' column using time module
    popular_hour = df['hour'].mode()[0] # find the most common hour (from 0 to 23)
    print('\n Most Frequent Start Hour: ', popular_hour)
    df.drop('hour', inplace = True, axis = 1)

    print("\nThis took %s seconds." % (time.time() - start_time)) # Print total execution time of this function
    print('-'*40)  # Display dashes separator indicating we finished displaying statistics on the most frequent times of travel



def station_stats(df):

    """
    Displays statistics on the most popular stations and trip

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time() # save current time; to calculate the execution time of this function.

    popular_start_station = df['Start Station'].mode()[0] # calculate most commonly start station
    print('\n Most Commonly Used Start Station: ', popular_start_station)

    popular_end_station = df['End Station'].mode()[0] # calculate most commonly end station
    print('\n Most Commonly Used End Station: ', popular_end_station)

    # calculate most frequent combination of start station and end station trip
    # Create a new column with concatenating both start station column and end station column
    df['Complete Trip'] = "Start Station: " + df['Start Station'] + ", End Station: " + df['End Station']
    frequent_trip = df['Complete Trip'].mode()[0] # find the most common trip
    print('\n Most Frequent Trip --> ', frequent_trip)
    df.drop('Complete Trip', inplace = True, axis = 1) # delete 'Complete Trip' column from our DataFrame, since we don't need it anymore

    print("\nThis took %s seconds." % (time.time() - start_time)) # Print total execution time of this function
    print('-'*40)  # Display dashes separator indicating we finished displaying statistics on the most popular stations and trip



def trip_duration_stats(df):

    """
    Displays statistics on the total and average trip duration

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time() # save current time; to calculate the execution time of this function.

    total_travel_time = df['Trip Duration'].sum() # calculate total trips duration in seconds
    print('\nTotal Trips Duration = {:,} hours'.format( int(total_travel_time / 3600))) # Display total trip duration in hours with commas as thousands separator

    mean_travel_time = df['Trip Duration'].mean() # calculate the mean of trips duration in seconds
    print('\nMean Trips Duration = {} mintues'.format( int(mean_travel_time / 60) )) # Print mean travel time in minutes

    print("\nThis took %s seconds." % (time.time() - start_time)) # Print total execution time of this function
    print('-'*40)  # Display dashes separator indicating we finished displaying statistics on the total and average trip duration



def user_stats(df):

    """
    Displays statistics on bikeshare users

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time() # save current time; to calculate the execution time of this function.

    user_types = df['User Type'].value_counts() # calculate counts of user types
    print('\nUser Type Counts:\n', user_types)

    # Since 'Gender' & 'Birth Year' columns doesn't exist in washington file, we need to check if it exists in our dataframe,
    # before Calculating the count of genders; to avoid getting an error.
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts() # calculates the counts of genders.
        print('\nGenders Counts:\n', genders)

    if 'Birth Year' in df.columns: # Check if we have 'Birth Year' column in our dataframe
        earliest_year_of_birth = df['Birth Year'].min() # calculates oldest user's year of birth
        print('\nEarliest Year of Birth: ', int(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max() # calculates youngest user's year of birth
        print('\nMost Recent Year of Birth: ', int(most_recent_year_of_birth))

        common_year_of_birth = df['Birth Year'].mode()[0] # calculates most common year of birth
        print('\nMost Common Year of Birth: ', int(common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time)) # Print total execution time of this function
    print('-'*40) # Display dashes separator indicating we finished displaying statistics on the total and average trip duration



def display_raw_date(df):

    """
    Displays The Raw Data, 5 rows in each print.

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    start_row = 0 # row start position
    end_row = 5 # row end positions

    while True: # A loop to display 5 rows of the raw data in each time. it breaks when the user doesn't want to see any more raw data
        if start_row == 0: # check if this is the first time to ask the user, to ask him if want to see the first 5 rows of the raw data
            while True: # Foolproof loop to capture if the user want to see the raw data
                view_data = input("\nWould you like to see the first 5 rows of the raw data? Type 'Yes' or 'No': ").lower()
                if view_data in ['yes', 'no']: # Check if we captured a correct answer
                    break
                else:
                    print('Sorry, wrong answer..')
        else: # check if this is not the first time to ask the user if they want to see the raw data, display a message if they want to see 5 more rows.
            while True: # Foolproof loop to capture if the user want to see the raw data
                view_data = input("\nWould you like to see 5 more rows of the raw data? Type 'Yes' or 'No': ").lower()
                if view_data in ['yes', 'no']: # Check if we captured a correct answer
                    break
                else:
                    print('Sorry, wrong answer..')

        if view_data == 'yes': # Check if the user chose to display the raw data
            # We can select data using loc and iloc, which you can read more about here. loc uses labels of rows or columns to select data,
            df_rows = df.iloc[start_row : end_row] #  while iloc uses the index numbers
            print(df_rows) # print 5 rows of the raw data
            start_row = end_row # change start_row to point to the first of the next 5 rows to be displayed
            end_row += 5 # change end_row to point to the end of the next 5 rows to be displayed
        else: # if the user doesn't want to see the raw data, break out of the loop and end this function
            break



def save_raw_data(df):

    """
    saves the dataframe into .csv file in the same directory of this script

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    while True: # Foolproof loop to capture if the user want to save the raw data into a csv file
        save_data = input("\nWould you like to save the raw data into a .csv file? Type 'Yes' or 'No': ").lower()
        if save_data in ['yes', 'no']: # Check if we captured a correct answer from the user
            break
        else:
            print('Sorry, wrong answer..')

    if save_data == 'yes': # check if the user want to save the raw data
        file_name = input('\nplease enter a name to save the data with: ') # Ask the user for the name of the file
        df.to_csv('{}.csv'.format(file_name), index = False) # save the file in the same directory of this script, and disable the index column that pandas creates
        print("\nDone! You will find a file named '{}.csv' in the same directory of this script\n".format(file_name))



def general_info(df):

    """
    Print general information and statistics about the dataframe

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    want_info = get_user_resp("Would you like to print general_info")

    if want_info == 'yes': # check if the user want to print general info about the dataframe
        print('\nGeneral Information About The Selected dataframe: \n')
        print('Number of Rows = ',df.shape[0], '\n') # number of rows
        print('Number of Columns = ',df.shape[1], '\n') # number of columns
        print('Columns of The dataframe: ') # Columns of The dataframe and their indexes
        for index, column in enumerate(df.columns):
            print(index, column)
        print('\nNumber of Unique Start Statinos: ', df['Start Station'].nunique(), '\n') # Count of Unique Distinct Values in 'Start Station' Column
        print('Data Types of The DataFrame Columns: \n', df.dtypes, '\n') # Data Types of The DataFrame Columns

        # The describe() function provides good summary statistics about the dataframe
        print('\nSummary Statistics: \n')
        print(df.describe())

        print('\n\n Dataframe info: \n')
        df.info() # Print General Information About The DataFrame



def clean_data(df):

    """
    Clean the raw data from 3 common issues:
        1. NAN Values
        2. Duplicated Rows
        3. Incorrect Data types

    Args:
        (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    while True: # Foolproof loop to capture if the user want to clean the dataframe
        want_clean = input("\n\nWould you like to clean the dataframe? Type 'Yes' or 'No': ").lower()
        if want_clean in ['yes', 'no']: # Check if we captured a correct answer
            break
        else:
            print('Sorry, wrong answer..')

    if want_clean == 'yes': # check if the user want to print general info about the dataframe
        print('\nInfo before The Cleaning:\n')
        df.info() # Print General Information About The DataFrame

        # 1. First issue: NAN values

        # 1. a. Birth Year Column: Fill NAN with mean
        if 'Birth Year' in df.columns: # check if this column exists in the dataframe first
            birth_year_mean = int(df['Birth Year'].mean())
            df['Birth Year'].fillna(birth_year_mean, inplace = True)

        #1. b. Gender Column (String): Fill NAN with mode
        if 'Gender' in df.columns: # check if this column exists in the dataframe first
            gender_mode = df['Gender'].mode()[0]
            df['Gender'].fillna(gender_mode, inplace = True)

        #1. c. User Type Column (String): Fill NAN with mode
        user_type_mode = df['User Type'].mode()[0]
        df['User Type'].fillna(user_type_mode, inplace = True)

        # 2. Second issue: Duplicated Rows

        duplicated_rows_count = sum(df.duplicated())
        print('\nNumber of Duplicated Rows = {}\n'.format(duplicated_rows_count))
        df.drop_duplicates(inplace = True) # remove the duplicates Rows

        # 3. Third issue: Incorrect Data types
        # in this issue, we usually have timestamp column represented as string; instead of datetimes

        # Currently we have 'End Time' column as string. We didn't convert it to datetimes till now as we didn't need it so far
        df['End Time'] = pd.to_datetime(df['End Time'])

        print('\nInfo After The Cleaning:\n')
        df.info() # Print General Information About The DataFrame



def plot(df):

    """
        Generate different kinds of graphs of the raw data to visualize it and visualize the relationships between its variables

        Args:
            (Pandas Dataframe) df - the dataFrame that the user has specified
    """

    while True: # Foolproof loop to capture if the user want to plot the dataframe
        want_plot = input("\n\nWould you like to plot the dataframe? Type 'Yes' or 'No': ").lower()
        if want_plot in ['yes', 'no']: # Check if we captured a correct answer
            break
        else: # Display a message to the user when they enter a wrong city name, before looping to capture their input again
            print('Sorry, wrong answer..')

    if want_plot == 'yes': # check if the user want to plot the dataframe

        # Print a message to alret the user that it will take some time to plot and save the graphs
        print('\n\nPlease wait while we prepare and plot the graphs..')

        # First Let's create a directory to save the figures inside it.
        # Get the current directory of the script and concatenate the new folder we want to create
        now = datetime.now() # datetime object containing current date and time
        path = os.getcwd() + '\graphs-' + now.strftime("%d-%b-%Y-%H-%M-%S") # Create folder with current timestamp
        # Why do I create the folder with the timestamp of seconds?
        # To avoid over-write on existing graphs if I used the same folder over and over again
        # os.mkdir() method results in an error when it try to create a directory that's already exists!
        # So, we need to handle that error:
        try:
            os.mkdir(path)
        except OSError:
            pass # do nothing and continue

        if 'Birth Year' in df.columns: # check first if Birth Year column exists inside the selected dataframe
            # Quick way to view histograms for all numberical columns in a DataFrame is hist function
            # which we can call directly on the pandas dataframe
            df.hist('Birth Year', figsize = (8, 8), range=[1930, 2005], facecolor='gray', align='mid'); # we created plot of 'Birth Year' column
            #and specified its size # we used a semi colon to suppress unwanted output by the function
            #plt.show() # and with this line, we display the plot but the program stops until you close the plot window, then continues after that
            plt.savefig(path + '/Birth_Year_Histogram.png') # Save the plot into a file in the same directory
            plt.clf() # clear the figure; to start a new one

            df['Birth Year'].plot(kind = 'hist'); # Plot a histogram of 'Trip Duration' column
            plt.xlim(1930, 2005) # Set X Axis Range
            plt.savefig(path +  '/Birth_Year_Histogram_2.png') # Save The Histogram of the 'Trip Duration' column
            plt.clf() # clear the figure; to start a new one

            # Draw a box plot using the plot function of any variable
            df['Birth Year'].plot(kind = 'box')
            plt.savefig(path + '/Birth_Year_Box.png')
            plt.clf() # clear the figure; to start a new one

            # we can also do scatter plots using plot function, and remember the scatter plot is between two variables, so we'll specify 2 variables to plot.
            # let's draw the relationship between the month and Birth Year columns
            df.plot(x = 'month', y = 'Birth Year', kind = 'scatter');
            plt.savefig(path + '/Gender_and_Birth_Year_Scatter.png')
            plt.clf() # clear the figure; to start a new one

        if 'Gender' in df.columns: # check first if Gender column exists inside the selected dataframe
            # Create pie chart of Gender column
            df['Gender'].value_counts().plot(kind = 'pie', figsize = (8,8))
            plt.savefig(path + '/Gender_Pie.png')
            plt.clf() # clear the figure; to start a new one

        # To create a Bar Chart, we need to count for each distinct value in the column
        # This value_counts function aggregates counts for each unique value in a column
        df['User Type'].value_counts().plot(kind = 'bar')
        plt.savefig(path + '/User_Type_Bar.png')
        plt.clf() # clear the figure; to start a new one

        # The next function is very useful for getting quick insight into the relationships among numerical variables with scatter plots
        # It also plot the histogram for each variable
        # Remember that scatter is a relationship between two variables? in the output graph you get, you have 4 variables, where every 4 variables
        # exists on the x axis and on the Y axis. Each variable has 3 scatter plots, each one is between itself and another variable.
        # The fourth plot that is between itself and itself, is actually a histogram plot of the variable! how cool is this!
        pd.plotting.scatter_matrix(df, figsize = (15,15)) # plot all columns in one figure of scatter plot
        plt.savefig(path + '/All_columns_Scatter.png')
        plt.clf() # clear the figure; to start a new one

        print("\nDone! Graphs have been created and saved inside a directory named 'output_graphs' in the same directory of this script.")



def main():

    """main function"""

    while True: # A Loop to reload the script if the user like to restart
        city, month, day = get_filters() # Get city, month, and day from the user through get_filters() function
        df = load_data(city, month, day) # Get the DataFrame based on the user inputs, through load_data() function
        clean_data(df) # clean the dataframe
        time_stats(df) # Displays statistics on the most frequent times of travel
        station_stats(df) # Displays statistics on the most popular stations and trip
        trip_duration_stats(df) # Displays statistics on the total and average trip duration
        user_stats(df) # Displays statistics on bikeshare users
        display_raw_date(df) # Displays The Raw Data If The User Wants
        save_raw_data(df) # save the raw data into an .csv file
        general_info(df) # print general information about the dataframe
        plot(df) # Plotting the data
        # Check if the user want to restart and enter different inputs
        while True: # Foolproof loop to capture a correct answer from the user
            restart = input("\nWould you like to restart the script? Type 'Yes' or 'No': ")
            if restart in ['yes', 'no']:
                break
            else:
                print('Sorry, wrong answer..')

        if restart.lower() == 'no': # If the answer is no, break out of the loop. Otherwise, it will loop again and restart the main function.
            break



# The following if statement is the first line that will be executed in this program
if __name__ == "__main__": # execute this line if and only if you run this file, which will run the next line main() and start executing the program
# however, if we import this file into another program, to use some functions from it, this condition will be false, and the main() won't be called.
	main()
