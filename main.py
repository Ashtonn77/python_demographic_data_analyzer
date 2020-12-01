import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    total_ppl = df.shape[0]
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df['race']
    race_map = {}
    for i in race:
        race_map[i] = race_map.get(i, 0) + 1

    race_count = pd.Series(race_map)

    # What is the average age of men?
    age = df[['sex', 'age']]
    age = age.loc[age['sex'] == 'Male']
    age_total = age['age'].sum()
    age_avg = age_total / age.shape[0]

    average_age_men = round(age_avg, 1)

    # What is the percentage of people who have a Bachelor's degree?
    edu = df.loc[df['education'] == 'Bachelors']
    percentage_bachelors = edu.shape[0] / total_ppl
    percentage_bachelors = round(percentage_bachelors * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    hi_ed_num = higher_education.shape[0]
    lo_ed_num = lower_education.shape[0]

    higher_education = higher_education.loc[higher_education['salary'] == '>50K']
    lower_education = lower_education.loc[lower_education['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = higher_education.shape[0] / hi_ed_num
    higher_education_rich = round(higher_education_rich * 100, 1)
    higher_education = higher_education.shape[0]

    lower_education_rich = lower_education.shape[0] / lo_ed_num
    lower_education_rich = round(lower_education_rich * 100, 1)
    lower_education = lower_education.shape[0]

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min(axis=0)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df['hours-per-week'].min(axis=0)

    num_min_workers = (df.loc[df['hours-per-week'] == min_work_hours]).shape[0]
    nm_wrk = (df.loc[df['hours-per-week'] == min_work_hours])

    rich_num = (nm_wrk.loc[nm_wrk['salary'] == '>50K'])
    rich_percentage = rich_num.shape[0] / num_min_workers
    rich_percentage = round(rich_percentage * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_country = df['native-country']

    pop = dict(rich_country.value_counts())

    rich_country = rich_country.loc[df['salary'] == '>50K']

    rich_map = {}
    for i in rich_country:
        rich_map[i] = rich_map.get(i, 0) + 1

    for i, k in pop.items():
        if i in rich_map:
            rich_map[i] = round(((rich_map[i] / k) * 100), 1)


    mx_v = list(rich_map.values())
    mx_k = list(rich_map.keys())

    highest_earning_country = mx_k[mx_v.index(max(mx_v))]
    highest_earning_country_percentage = rich_map[highest_earning_country]

    # Identify the most popular occupation for those who earn >50K in India.
    india = df.loc[df['native-country'] == 'India']
    india = india.loc[india['salary'] == '>50K']

    c = india['occupation'].value_counts()
    c = c.nlargest(1)
    top_IN_occupation = list(dict(c).keys())[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
