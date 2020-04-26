import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
        'august', 'september', 'october', 'november', 'december']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    time.sleep(.5)
    while True:
        city = input('What CITY do you want to explore?\n').lower()
        if city in CITY_DATA:
            break
        else:
            print('Sorry that is not a valid CITY. Please choose among the ' +
            'following:')
            for x in CITY_DATA.keys():
                time.sleep(.2)
                print('- ' + x.title())


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        time.sleep(.5)
        month = input('What MONTH do you want to explore?\n').lower()
        if month in months:
            break
        else:
            print('Sorry that is not a valid MONTH. Please choose among the ' +
            'following:')
            for x in months:
                time.sleep(.2)
                print('- ' + x.title())


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time.sleep(.5)
        day = input('What DAY do you want to explore?\n').lower()
        if day in days:
            break
        else:
            print('Sorry that is not a valid DAY. Please choose among the ' +
            'following:')
            for x in days:
                time.sleep(.2)
                print('- ' + x.title())

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

    # load dataframe with chosen city data
    data = pd.read_csv(city.replace(' ', '_') + '.csv')
    df = pd.DataFrame(data)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # add columns for month/weekday/hour
    df['month'] = df['Start Time'].dt.month_name()
    df['weekday'] = df['Start Time'].dt.day_name()
    df['start hour'] = df['Start Time'].dt.hour

    # filter df based on chosen month/weekday
    df = df[df['month'] == month.title()]
    df = df[df['weekday'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nMost common MONTH: ' + df['month'].mode()
    .to_string(index=False).strip())

    # TO DO: display the most common day of week
    print('\nMost common DAY OF THE WEEK: ' + df['weekday'].mode()
    .to_string(index=False).strip())

    # TO DO: display the most common start hour
    print('\nMost common START HOUR: ' + df['start hour'].mode()
    .to_string(index=False).strip())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used START STATION: ' + df['Start Station'].mode()
    .to_string(index=False).strip())

    # TO DO: display most commonly used end station
    print('\nMost commonly used END STATION: ' + df['End Station'].mode()
    .to_string(index=False).strip())

    # TO DO: display most frequent combination of start station and end station trip
    print((df['Start Station'] + ', ' + df['End Station']).mode()
    .to_string(index=False).strip())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # # TO DO: display total travel time
    print('\nTOTAL travel time: ' + str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\nMEAN travel time [grr, so mean!]: ' +
    str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCount of USER TYPES: ' + df['User Type'].groupby(df['User Type'])
    .count().to_string())

    # TO DO: Display counts of gender
    try:
        print('\nCount of GENDER: ' + df['Gender'].groupby(df['Gender'])
        .count().to_string())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEARLIEST birth year: ' + str(df['Birth Year'].min()))
        print('\nMOST RECENT birth year: ' + str(df['Birth Year'].max()))
        print('\nMOST COMMON birth year: ' + str(df['Birth Year'].mode()
        .to_string(index=False).strip()))

    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    s_index = 0
    while True:
        time.sleep(.5)
        prompt = input('Do you want to see raw data? Enter yes or no.\n')
        if prompt.lower() == 'yes':
            print(df.iloc[s_index:s_index+5])
            while True:
                time.sleep(.5)
                re_prompt = input('Do you want to see more raw data? '
                + 'Enter yes or no.\n')
                if re_prompt.lower() == 'yes':
                    s_index += 5
                    print(df.iloc[s_index:s_index+5])
                elif re_prompt.lower() not in ['yes', 'no']:
                    print('Sorry that is an invalid answer. Please enter ' +
                    'yes or no.\n')
                else:
                    break
            break
        elif prompt.lower() not in ['yes', 'no']:
            print('Sorry that is an invalid answer. Please enter yes or no.\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
