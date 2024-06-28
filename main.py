import pandas as pd
from geopy.distance import geodesic
from transformers import pipeline
import json


college_data = pd.read_csv('data.csv')

qa_pipeline = pipeline("question-answering")

def extract_information(user_query, context):
    qa_input = {
        'question': user_query,
        'context': context
    }
    result = qa_pipeline(qa_input)
    return result['answer']

def get_nearby_colleges(user_location, max_distance_km=50):
    def get_distance(college_location, user_location):
        return geodesic(college_location, user_location).km

    user_lat_lon = (user_location['lat'], user_location['lon'])
    college_data['distance'] = college_data.apply(lambda row: get_distance((row['location_lat'], row['location_lon']), user_lat_lon), axis=1)
    nearby_colleges = college_data[college_data['distance'] <= max_distance_km]
    return nearby_colleges.to_dict(orient='records')

def main():
    print("Welcome to the College Finder Bot!")
    
    user_name = input("Bot: Hello! What's your name?\nYou: ")
    print(f"Bot: Nice to meet you, {user_name}!")

    interaction_logs = []
    
    while True:
        
        user_location_query = input(f"Bot: Where are you currently located, {user_name}?\nYou: ")
       
        context = f"My name is {user_name}. I am located at 28.6139, 77.2090. I am looking for colleges nearby offering B.Tech courses."
        user_location_str = extract_information(user_location_query, context)
        
        user_location = {'lat': 28.6139, 'lon': 77.2090}
        
        course_query = input("Bot: What course are you interested in?\nYou: ")
        print(f"Bot: Let me find some colleges near {user_location_str} that offer {course_query}.")
        
        nearby_colleges = get_nearby_colleges(user_location)
        
        filtered_colleges = [college for college in nearby_colleges if course_query.lower() in college['courses_offered'].lower()]
        
        if not filtered_colleges:
            bot_response = f"Sorry, {user_name}, I couldn't find any colleges near {user_location_str} offering {course_query}."
            print(f"Bot: {bot_response}")
        else:
            bot_response = f"Here are some colleges near {user_location_str} offering {course_query}:"
            print(f"Bot: {bot_response}")
            for college in filtered_colleges:
                college_info = (
                    f"\nCollege Name: {college['college_name']}\n"
                    f"Fees: {college['fees']}\n"
                    f"Established On: {college['established_on']}\n"
                    f"Courses Offered: {college['courses_offered']}\n"
                    f"Class Timings: {college['class_timings']}\n"
                    f"Cutoff Marks: {college['cutoff_marks']}\n"
                    f"Facilities: {college['facilities']}\n"
                    f"Distance: {college['distance']:.2f} km"
                )
                print(college_info)
                bot_response += college_info
            print("\n")

        
        interaction_logs.append({
            'user_name': user_name,
            'user_location_query': user_location_query,
            'course_query': course_query,
            'bot_response': bot_response
        })

        user_query = input("Bot: Is there anything else I can help you with?\nYou: ")
        if user_query.lower() in ['no', 'nothing', 'exit', 'bye']:
            print(f"Bot: Goodbye, {user_name}! Have a great day!")
            break

    with open('interaction_logs.json', 'w') as f:
        json.dump(interaction_logs, f, indent=4)

if __name__ == '__main__':
    main()
