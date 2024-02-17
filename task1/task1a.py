import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

columns = ['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines']

def get_details(restuarant_list):
    '''Get the details from the given list of restaurants.'''
    result = []
    
    for entry in restuarant_list:
        try:
            restaurant = entry.get('restaurant', {})
            restaurant_id = restaurant.get('R', {}).get('res_id', "NA")
            restaurant_name = restaurant.get('name', "NA")
            country_id = restaurant.get('location', {}).get('country_id', "NA")
            city = restaurant.get('location', {}).get('city', "NA")
            votes = restaurant.get('user_rating', {}).get('votes', "NA")
            aggregate_rating = restaurant.get('user_rating', {}).get('aggregate_rating', "NA")
            cuisines = restaurant.get('cuisines', "NA")
            
            result.append([restaurant_id, restaurant_name, country_id, city, votes, aggregate_rating, cuisines])
    
        except Exception as e:
            logging.error("An error occurred while processing restaurant")
    
    return result

def map_replace(df, column, mapping):
    '''Replace the values in the given column with the values from the mapping dataframe.'''
    try:    
        df[column] = df[column].map(mapping.set_index('Country Code')[column])
        return df
    except Exception as e:
        logging.error("An error occurred while mapping and replacing values")
        raise