import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website you want to scrape
url = 'https://www.scrapethissite.com/pages/simple/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Create lists to hold the data
    countries = []
    capitals = []
    populations = []
    areas = []

    # Find all country divs
    for country_div in soup.find_all('div', class_='country'):
        # Extract country name
        country_name = country_div.find('h3', class_='country-name').get_text(strip=True)
        
        # Extract capital
        capital = country_div.find('span', class_='country-capital').get_text(strip=True)
        
        # Extract population
        population = country_div.find('span', class_='country-population').get_text(strip=True)
        
        # Extract area
        area = country_div.find('span', class_='country-area').get_text(strip=True)

        # Append the extracted data to the lists
        countries.append(country_name)
        capitals.append(capital)
        populations.append(population)
        areas.append(area)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame({
        'Country': countries,
        'Capital': capitals,
        'Population': populations,
        'Area (km²)': areas
    })

    # Print the DataFrame
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv('country_data.csv', index=False)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
