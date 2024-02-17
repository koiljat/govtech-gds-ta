import pandas as pd

events_columns = ['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 'Event Title', 'Event Start Date', 'Event End Date']

def get_events(restuarant_list):
    '''Get the events from the given list of restaurants.'''
    result = []
    
    for entry in restuarant_list:
        restaurant = entry.get('restaurant', {})
        restaurant_id = restaurant.get('R', {}).get('res_id', "NA")
        restaurant_name = restaurant.get('name', "NA")
        zomato_events = restaurant.get('zomato_events', [])
        
        for item in zomato_events:
            event = item.get('event', {})
            event_id = event.get('event_id', "NA")
            photos = event.get('photos', [])
            
            ## Set default as NA
            photo_URL = "NA"
            
            if photos:
                photo = photos[0]
                photo_URL = photo.get('photo', {}).get('URL', "NA")
            
            event_title = event.get('title', "NA").strip()
            event_start_date = event.get('start_date', "NA")
            event_end_date = event.get('end_date', "NA")
            
            result.append([event_id, restaurant_id, restaurant_name, photo_URL, event_title, event_start_date, event_end_date])
    
    return result

def filter_april(df):
    '''Filter the events that are in April 2019.'''
    df['Event Start Date'] = pd.to_datetime(df['Event Start Date'])
    filtered_event_df = df[(df['Event Start Date'] >= '2019-04-01') & (df['Event Start Date'] <= '2019-04-30')]
    
    return filtered_event_df
    