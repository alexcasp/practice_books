def get_country_city(city, country, population =''):
    if population:
        citycountry = f'{city}, {country}, {population}'
    else:
        citycountry = f'{city}, {country}'    
    return citycountry.title()