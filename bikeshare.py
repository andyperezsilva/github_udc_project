import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    This function is to ask the user to specify a city, month, and day to analyze, this in a interactive way.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Enter city name from the list: \n1- Chicago\n2- New York City\n3- Washington.\n")
    city = input("City: ").lower()
    
    while city not in {"chicago", "new york city", "washington"}:
        print(city.title() + " is not a city in our list")
        city = input("Enter city: ").lower()
    
    print("How do you want to filter data, by month, day, both or not at all? Type option from the list below: \n1- Month\n2- Day\n3- Both\n4- None (type 'none' to no time filtering)")
    filter_name = input("Filter by: ").title().lower()
    while filter_name not in {"month", "day", "both", "none"}:
        print(filter_name.title() + " is not a filter in our list")
        filter_name = input("Filter by: ").title().lower()
    
    #month and day of week list
    months_list = ["January", "February", "March", "April", "May", "June"]
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if(filter_name == "both"):
        # get user input for month (all, january, february, ... , june)
        print("\nEnter month from the list below.\n")
    
        for index, item in enumerate(months_list, start=1):
            print(index, "- ", item)
        
        month = input("Month: ").title().lower()
    
        while month.title() not in months_list:
            print(month.title() + " is not a month in our list")
            month = input("Month: ").title().lower()
            
        # get user input for day of week (all, monday, tuesday, ... sunday)
        print("\nEnter day of the week from the list below.\n")
    
        for index, item in enumerate(days_list, start=1):
            print(index, "- ", item)
        
        day_of_week = input("Day: ").title().lower()
    
        while day_of_week.title() not in days_list:
            print(day_of_week.title() + " is not a month in our list")
            month = input("Day: ").title().lower()
    elif(filter_name == "month"):
        day_of_week="all"
        # get user input for month (all, january, february, ... , june)
        print("\nEnter month from the list below.\n")
    
        for index, item in enumerate(months_list, start=1):
            print(index, "- ", item)
        
        month = input("Month: ").title().lower()
    
        while month.title() not in months_list:
            print(month.title() + " is not a month in our list")
            month = input("Month: ").title().lower()
    elif(filter_name == "day"):
        month="all"
        # get user input for day of week (all, monday, tuesday, ... sunday)
        print("\nEnter day of the week from the list below.\n")
    
        for index, item in enumerate(days_list, start=1):
            print(index, "- ", item)
        
        day_of_week = input("Day: ").title().lower()
    
        while day_of_week.title() not in days_list:
            print(day_of_week.title() + " is not a month in our list")
            month = input("Day: ").title().lower()
    else:
        month="all"
        day_of_week="all"

    print('-'*40)
    return city, month, day_of_week


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    #Set Start Time to datetime data type
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #Filter results by month
    if month != "all":
        df = df[df['month'] == month.title()]

    #Filter results by day
    if day != "all":
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # display the most common month
    print('The most common month users travel using Bikeshare services is: {}'.format(df['month'].mode()[0]), '\n')
    print('*'*40, '\n')


    # display the most common day of week
    print('The most common day users travel using Bikeshare services is: {}'.format(df['day_of_week'].mode()[0]), '\n')
    print('*'*40, '\n')

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    military_hour = df['Hour'].mode()[0]
    if(military_hour <=11):
        print('The most common starting hour for users to travel using Bikeshare services is: {}'.format(military_hour), '\n')
        print('*'*40, '\n')
    else:
        print('The most common starting hour for users to travel using Bikeshare services is: {}'.format(military_hour%12), '\n')
        print('*'*40, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common station used by Bikeshare users to start traveling is: {}'.format(df['Start Station'].mode()[0]), '\n')

    # display most commonly used end station
    print('The most common end station used by Bikeshare users to deliver bikes is: {}'.format(df['End Station'].mode()[0]), '\n')

   
    #First, create a column for Start and End Station, this column will be called "round_trip"
    df['round_trip'] = "From: " + df['Start Station'] + " To: " + df['End Station']

    #Then display most frequent combination of start station and end station trip from previous created column
    print('The most common combination of Start and End station used by Bikshare users is: {}'.format(df['round_trip'].mode()[0]), '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel duration is: {}'.format(round(df['Trip Duration'].sum(),2)) + " seconds", '\n')

    # display mean travel time
    print('The mean (average) travel duration is: {}'.format(round(df['Trip Duration'].mean(),2))+ " seconds", '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('In the system, there are the following user types: \n')
    print(df['User Type'].value_counts().to_string())

    # Display counts of gender, need to handle exception for Washington, since Washington does not have Gender column
    try:
        print('\nIn the system, there are the following stats for Gender: \n')
        print(df['Gender'].value_counts().to_string())
    except:
        print('Oops, seems like you selected Whasington as a city to display results, and Washington has no gender information\nPlease, select a different city to know about gender\n')


    # Display earliest, most recent, and most common year of birth, need to handle exception for Washington, since Washington does not have Birth Year column
    try:
        print("\nThe data related to year of birth registered in the system is as follows: \n")
        earliest=int(df['Birth Year'].min())
        most_recent=int(df['Birth Year'].max())
        most_common=int(df['Birth Year'].mode())
        print('The earliest year of birth registered in the system is: {}.'.format(earliest), '\n')
        print('The most recent year of birth registered in the system is: {}.'.format(most_recent), '\n')
        print('The most common year of birth registered in the system is: {}.'.format(most_common), '\n')
    except:
        print('Oops, seems like you selected Whasington as a city to display results, and Washington has no year of birth information\nPlease, select a different city to know about year of birth\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_all_city_raw_data(city):
    """Displays five records from the selected city
       and also requests the user to select whether to show raw data or not

    Args:
        (df): Data frame for the selected city
    Returns:
        Nothing
    """
    df = pd.read_csv(CITY_DATA[city])
    user_possible_answers = ['no','yes']
    user_input = ''

    #counter to use for df.head()
    counter = 0

    # Ask the user whether to see more records
    while user_input not in user_possible_answers:
        print("\nDo you want to see raw data records from the city: " + city.title() + "?")
        print("\nPlease, type 'Yes' if you want to see raw data or 'No' if you don't\n")
        user_input = input().lower()

        #If user types 'Yes', display 5 records of raw data
        if user_input == "yes":
            pd.set_option('display.max_columns',200)
            print(df.head())
        elif user_input not in user_possible_answers:
            print("\nSeems like you typed an incorrect answer. Please type again a right answer.Remember to type only 'Yes' or 'No'")

    #Ask the user whether to display more data
    while user_input == 'yes':
        print("\nDo you want to continue to see more raw data records from the city: " + city.title() + "? Type 'Yes' if you want to see raw data or 'No' if you don't\n")
        counter += 5
        user_input = input().lower()
        #If user types 'Yes', display 5 records of raw data, otherwise, break the loop
        if(user_input not in user_possible_answers):
            print("\nSeems like you typed an incorrect answer. Please type again a right answer. Remember to type only 'Yes' or 'No'")
            user_input = "yes"
            continue
        elif(user_input == "yes"):
            pd.set_option('display.max_columns',200)
            print(df[counter:counter+5])
        elif(user_input == "no"):
            break

    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_all_city_raw_data(city)
        
        user_possible_answers = ['no','yes']

        restart = ''
                   
        while restart not in user_possible_answers:
            print("\nSeems like you typed an incorrect answer. Please type again a right answer. Remember to type only 'Yes' or 'No'")
            restart = input('\nWould you like to restart? Please type \'Yes\' or \'No\'.\n')
        
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
    main()