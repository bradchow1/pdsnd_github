import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Args:
        None.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # This code is the while loop to handle invalid inputs
    city = ' '

    while city not in CITY_DATA.keys():
        print("\nWelcome to the Bikeshare Data Program! Please choose your city:")
        print("\n1. Chicago  2. New York City  3. Washington")
        city = input("\nAllowable input as follows:\nCity's full name; not case sensitive.\nCity's full name in Title form (Chicago)").lower()

        if city not in CITY_DATA.keys():
            print("\nInput not valid. Please re-enter city name using the allowable formats")
            print("\nReturning for user input...")

    print(f"\nYou have selected {city.title()} as your chosen city!")

    # This code will create the month dictionary including the option for 'all'
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease input the month you want to see, from January to June, for which you're seeking the data:")
        print("\nAllowable input as follows:\nFull month name; not case sensitive.\nMonth's full name in Title form (April).")
        month = input("\nIf you wish to veiw all months, please type 'all' using the above allowable inputs.)").lower()

        if month not in MONTH_DATA.keys():
            print("\nInput not valid. Please re-enter desired monthly data using the allowable formats")
            print("\nReturning for user input...")

    print(f"\nYou have selected {month.title()} as your chosen month!")

    # This code will create the 'days' list to store the selectable days including the option for 'all'
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease input the day of the week for which you want to veiw the data:")
        print("\nAllowable input as follows:\nDay name; not case sensitive.\nName of day in Title form (Monday).")
        print("\n(If you wish to veiw all days, please type 'all' using the above allowable inputs.)")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nInput not valid. Please re-enter desired daily data using the allowable formats")
            print("\nReturning for user input...")

    print(f"\nYou have selected {day.title()} as your chosen day!")
    print(f"\nYou have selected to view the data for the following: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*40)

    # Returns the above selections
    return city, month, day

# This code will create the function to load data from the given .csv files
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str): name of the city to analyze
        (str): name of the month to filter by, or "all" to apply no month filter
        (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # This code loads the selected city data
    print("\nRetreiving requested data...")
    df = pd.read_csv(CITY_DATA[city])

    # This code will change the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # This code will extract the month and day from the 'Start Time' column to create new respective columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # This will filter by month if needed
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # This will filter by month to establish the new dataframe
        df = df[df['month'] == month]

    # This will filter by day if needed
    if day != 'all':
        # This will filter by day to establish the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # This will return the selected file as a (df)
    return df

# This creates the function to calculate the time-based stats for the selected data
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nSearhcing for the most frequent times of travel...\n')
    start_time = time.time()

    # This code uses .mode() to calculate the most popular month
    popular_month = df['month'].mode()[0]

    print(f"The Most Popular Month is (with 1 = January,...,6 = June): {popular_month}")

    # This code uses .mode() to calculate the most popular day
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nThe Most Popular Day is: {popular_day}")

    # This code will extract the hour from the 'Start Time' column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # This code uses .mode() to calculate the most popular hour
    popular_hour = df['hour'].mode()[0]

    print(f"\nThe Most Popular Start Hour is: {popular_hour}")

    # This code will print the time taken to do all the needed calculations
    print(f"\nThis took {(time.time() - start_time)} seconds to complete!")
    print('-'*40)

# This code will create the function to calculate the station related stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nSearching for the most popular stations and trip...\n')
    start_time = time.time()

    # This code uses .mode() to calculate the most common start station
    common_start_station = df['Start Station'].mode()[0]

    print(f"The Most Commonly Used Start Station is: {common_start_station}")

    # This code uses .mode() to calculate the most common end station
    common_end_station = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {common_end_station}")

    # This code uses str.cat method to combine two columns in the df
    # and finds the most common combo if start and end stations
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"\nThe Most Frequent Combination of Trips are from {combo}.")

    print(f"\nThis took {(time.time() - start_time)} seconds to complete!")
    print('-'*40)

# This code will create the function for trip duration related stats
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nSearching for the Trip Duration...\n')
    start_time = time.time()

    # This code uses the sum method to total the trip duration
    total_duration = df['Trip Duration'].sum()
    # This code puts the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    # This code puts the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds!")

    # This code calculates the average trip duration with the mean method
    average_duration = round(df['Trip Duration'].mean())
    # This code puts the average duration in minutes and seconds format
    mins, sec = divmod(average_duration, 60)
    # This code will filter the prints of the time in hours, mins, and sec format if the minutes exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds!")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds!")

    print(f"\nThis took {(time.time() - start_time)} seconds to complete!")
    print('-'*40)

# This code will create the function to calculate user stats
def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nSearching for User Stats...\n')
    start_time = time.time()

    # This code  will count the total users using value_counts
    # and then are printed by the user_type
    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    # This code will use a try clause to display the numebr of users by gender
    # including if there is no gender in the column
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are provided below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # This code will use a try clause to make sure only df containing the 'Birth Year'
    # column is displayed, and displaying earliest, most recent, and most common
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year is: {earliest}\n\nThe most recent birth year is: {recent}\n\nThe most common birth year is: {common_year}")
    except:
        print("There are no found birth years within this file.")

    print(f"\nThis took {(time.time() - start_time)} seconds to complete!")
    print('-'*40)

# This code will create the function to display the data frame itself
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        (df): The data frame you wish to work with.
    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''

    # This code will use a counter variable to ensure only details from a certain point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you want to view the raw data?")
        print("\nAcceptable responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    # This code is an extra while loop to verify if the user wants to keep viewing data
    while rdata == 'yes':
        print("Do you want to view more of the raw data?")
        counter += 5
        rdata = input().lower()
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*40)

# This is the ending function to return all previous functions if user wants to restart
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
