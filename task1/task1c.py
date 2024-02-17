import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def get_ratings(restuarant_list):
    '''Get the ratings from the given list of restaurants.'''
    
    results = []
    
    for entry in restuarant_list:
        try:
            restaurant = entry.get('restaurant', {})
            
            user_rating = restaurant.get('user_rating', {})
            
            rating_text = user_rating.get('rating_text', "NA")
            aggregate_rating = user_rating.get('aggregate_rating', "NA")
            
            results.append([rating_text, aggregate_rating])
        except Exception as e:
            logging.error("An error occurred while getting ratings")
            raise
        
    return results


def filter_and_group_ratings(ratings_df):
    '''Filter the ratings and group them by rating_text.'''
    try:
        target_ratings = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor']
        filtered_ratings = ratings_df[ratings_df['rating_text'].isin(target_ratings)]
        
        filtered_ratings.loc[:, 'aggregate_rating'] = pd.to_numeric(filtered_ratings['aggregate_rating'], errors='coerce')
        
        grouped_ratings = filtered_ratings.groupby('rating_text').agg({'aggregate_rating': ['min', 'max']})
        grouped_ratings = grouped_ratings.reset_index()
        grouped_ratings['rating_text'] = pd.Categorical(grouped_ratings['rating_text'], categories=target_ratings, ordered=True)
        
        return grouped_ratings
    except Exception as e:
        logging.error("An error occurred while filtering and grouping ratings")
        raise