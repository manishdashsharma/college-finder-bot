
# College Finder Bot

College Finder Bot is a Python script that helps users find nearby colleges based on their location and course interests. It uses natural language processing (NLP) to understand user queries and geospatial calculations to determine proximity to colleges.

## Features

- **User Interaction**: Engage in a conversation with the bot to provide your name, location, and course of interest.
- **Location-Based Search**: Utilizes geospatial calculations to find colleges within a specified radius from the user's location.
- **Course Filtering**: Filters colleges based on the course specified by the user.
- **Logging**: Logs user interactions, queries, and bot responses to `interaction_logs.json`.

## Requirements

- Python 3.x
- pandas
- geopy
- transformers

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/manishdashsharma/college-finder-bot.git
   cd college-finder-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

## Usage

1. Run the script and follow the prompts to interact with the bot.
2. Enter your name, current location, and the course you are interested in.
3. The bot will display colleges near your location that offer the specified course.

## Example

```bash
Bot: Hello! What's your name?
You: John
Bot: Nice to meet you, John!
Bot: Where are you currently located, John?
You: New Delhi
Bot: What course are you interested in?
You: B.Tech
Bot: Let me find some colleges near New Delhi that offer B.Tech.
Bot: Here are some colleges near New Delhi offering B.Tech:
- College Name: ABC College
  Fees: 50000
  Established On: 1995
  Courses Offered: B.Tech, M.Tech
  Class Timings: 9 AM - 5 PM
  Cutoff Marks: 85
  Facilities: Library, Sports Complex, Hostels
  Distance: 5.00 km

Bot: Is there anything else I can help you with?
You: no
Bot: Goodbye, John! Have a great day!
```

