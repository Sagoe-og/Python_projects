"""Another code block has been addeed which enables the user to input a country of interest and get the average, min, and max life expectancy for that country."""



min_expectancy = 100  # initializing the value of the min_expectancy to 100
max_expectancy = 0    # initializing the value of the max_expectancy to 0
max_year = None
max_country = None
small_year = None
small_country = None

with open("life-expectancy.csv") as list:
    next(list)

    for line in list:
        new_list = line.strip()
        breakdown = new_list.split(",")

        entity = breakdown[0]
        code = breakdown[1]
        years = breakdown[2]
        life_expectancy = (breakdown[3])


        life_expectancy = float(breakdown[3])
        country = entity
        low_year = years


        # Update min and max expectancy values
        if life_expectancy >= max_expectancy:
            max_expectancy = life_expectancy
            max_year = years
            max_country = entity

        if life_expectancy < min_expectancy:
            min_expectancy = life_expectancy
            small_year = years
            small_country = entity

        # Prompt for year of interest only once, outside the loop
        # So this is moved outside the file reading loop

        # Collect data for year of interest
        if 'total' not in locals():
            total = 0
            no_of_times = 0
            new_low = 100
            new_high = 0
            min_life_country = ""
            max_life_country = ""

        # We'll prompt for interest year after reading the file

        # Store data for each line for later use
        if 'data_by_year' not in locals():
            data_by_year = []
        data_by_year.append({
            'year': int(years),
            'country': entity,
            'life_expectancy': life_expectancy
        })

# Print overall statistics before asking for user input
print(f"The overall max life expectancy is: {max_expectancy:.2f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_expectancy:.2f} from {small_country} in {small_year}")

print()


# After reading the file and collecting data_by_year
while True:
    year_of_interest = int(input("Enter the year of interest: "))
    total = 0
    no_of_times = 0

    # Initialize min and max for the year of interest
    min_life = float('inf')
    max_life = float('-inf')
    min_life_country = ""
    max_life_country = ""

    for entry in data_by_year:
        if entry['year'] == year_of_interest:
            total += entry['life_expectancy']
            no_of_times += 1
            # Check for min
            if entry['life_expectancy'] < min_life:
                min_life = entry['life_expectancy']
                min_life_country = entry['country']
            # Check for max
            if entry['life_expectancy'] > max_life:
                max_life = entry['life_expectancy']
                max_life_country = entry['country']

    if no_of_times > 0:
        average = total / no_of_times
        print(f"For the year {year_of_interest} : ")
        print(f"The average life expectancy accross all countries was {average:.2f}")
        print(f"The min life expectancy was in {min_life_country} with {min_life:.2f} ")
        print(f"The max life expectancy was in {max_life_country} with {max_life:.2f}")
    else:
        print("No data for that year.")
        continue
    break  # Exit the loop after processing the year of interest

print()

# Get a set of all country names in the data for quick lookup
all_countries = set(entry['country'].lower() for entry in data_by_year)

while True:
    country_of_interest = input("Enter the country of interest: ").strip().lower()
    if country_of_interest in all_countries:
        # Calculate stats for the valid country
        country_total = 0
        country_count = 0
        country_min = float('inf')
        country_max = float('-inf')
        country_min_year = ""
        country_max_year = ""

        for entry in data_by_year:
            if entry['country'].lower() == country_of_interest:
                country_total += entry['life_expectancy']
                country_count += 1
                if entry['life_expectancy'] < country_min:
                    country_min = entry['life_expectancy']
                    country_min_year = entry['year']
                if entry['life_expectancy'] > country_max:
                    country_max = entry['life_expectancy']
                    country_max_year = entry['year']

        country_avg = country_total / country_count
        print(f"\nFor {country_of_interest.title()}:")
        print(f"Average life expectancy: {country_avg:.2f}")
        print(f"Minimum life expectancy: {country_min:.2f} (Year: {country_min_year})")
        print(f"Maximum life expectancy: {country_max:.2f} (Year: {country_max_year})")
        break
    else:
        print("Country not found. Please enter a valid country name.")



