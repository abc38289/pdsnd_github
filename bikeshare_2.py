import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for chicago, new york city, or washington? ').lower()
        if city in CITY_DATA:
            break #Valid input, exit the loop
        else:
            print('Invalid input. Please enter a valid city.')

    # get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Please enter a month (all, january, february, ...,june): ').lower()
        if month in valid_months:
            break #Valid input, exit the loop
        else:
            print('Invalid imput. Please enter a valid month or "all".')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Enter a day of the week (all, monday, tuesday, ... sunday): ').lower()
        if day in valid_days:
            break #Valid input, exit the loop
        else:
            print("Invalid input. Please enter a valid day or 'all'.")


    print('-'*40)
    return city, month, day



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
    df = pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    df['month'] = df['Start Time'].dt.month_name() # or can use dt.month to display the number instead of the name
    popular_month = df['month'].mode()[0] #find the most common month
    print("\nMost common month:", popular_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name() #try change dt.weekday_name to dt.day_anme()
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of the week:", popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    max_start_station = df['Start Station'].value_counts().idxmax()
    max_start_station_count = df['Start Station'].value_counts().max() # find the most commonly used start station
    print("\nMost commonly used start station:", max_start_station)
    print("Count:", max_start_station_count)

    # display most commonly used end station
    max_end_station = df['End Station'].value_counts().idxmax()
    max_end_station_count = df['End Station'].value_counts().max()
    print("\nMost commonly used End station:", max_end_station)
    print("Count:", max_end_station_count)

    # display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combination = df['Start-End Combination'].mode()[0]
    count_popular_combination = df['Start-End Combination'].value_counts().max()
    print("\nMost frequent combination of Start and End Stations:", popular_combination)
    print("Count:", count_popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal travel time:", total_travel_time, "seconds")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nMean travel time: {} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nCounts of User Types:")
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:")
        print(gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("\nYear of Birth Statistics:")
        print("Earliest Birth Year:", int(earliest_birth_year))
        print(f"Most Recent Birth Year:", int(most_recent_birth_year))
        print(f"Most Common Birth Year:", int(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    view_data = input("Do you want to see the raw data? Enter 'yes' or 'no': ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input("Do you want to see the next 5 rows of raw data? Enter 'yes' or 'no': ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print("Selected filters:")
        print("City:", city)
        print("Month:", month)
        print("Day:", day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
