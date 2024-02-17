def get_details(restuarant_list):
    result = []
    
    for entry in restuarant_list:
        restaurant = entry.get('restaurant', {})
        # Get the restaurant id
        restaurant_id = restaurant.get('R', {}).get('res_id', "NA")
        # Get the restaurant name
        restaurant_name = restaurant.get('name', "NA")
        # Get the country_id
        country_id = restaurant.get('location', {}).get('country_id', "NA")
        # Get the city name
        city = restaurant.get('location', {}).get('city', "NA")
        # Get the User Rating Votes
        votes = restaurant.get('user_rating', {}).get('votes', "NA")
        # Get the User Aggregate Rating
        aggregate_rating = restaurant.get('user_rating', {}).get('aggregate_rating', "NA")
        # Get the Cuisines
        cuisines = restaurant.get('cuisines', "NA")
        
        result.append([restaurant_id, restaurant_name, country_id, city, votes, aggregate_rating, cuisines])
        
    return result

columns = ['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines']

def map_replace(df, column, mapping):
    df[column] = df[column].map(mapping.set_index('Country Code')[column])
    return df