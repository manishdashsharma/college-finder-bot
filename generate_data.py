import pandas as pd
import random
from faker import Faker

fake = Faker()

# List of well-known Indian colleges and universities
indian_colleges = [
    "Indian Institute of Technology Bombay",
    "Indian Institute of Technology Delhi",
    "All India Institute of Medical Sciences Delhi",
    "Jawaharlal Nehru University",
    "Anna University",
    "University of Mumbai",
    "University of Calcutta",
    "Christ University",
    "Manipal University",
    "SRM Institute of Science and Technology",
    "Birla Institute of Technology and Science, Pilani",
    "Indian Institute of Science",
    "Indian Institute of Technology Kharagpur",
    "Indian Institute of Technology Kanpur",
    "Indian Institute of Technology Madras",
    "Banaras Hindu University",
    "National Institute of Technology, Trichy",
    "Vellore Institute of Technology",
    "Jadavpur University",
    "Aligarh Muslim University",
    "Jamia Millia Islamia",
    "Amity University",
    "Symbiosis International University",
    "Indian School of Business",
    "Xavier School of Management (XLRI)",
    "Tata Institute of Social Sciences",
    "IIM Ahmedabad",
    "IIM Bangalore",
    "IIM Calcutta",
    "Delhi University",
]

# Generate synthetic data
data = []
courses = ["B.Tech", "M.Tech", "MBBS", "BBA", "MBA", "B.Sc", "M.Sc", "Ph.D", "BCA", "MCA"]
facilities = ["Library", "Labs", "Hostels", "Sports Complex", "Cafeteria", "Gym", "Research Centers"]

for i in range(1000):
    college_name = random.choice(indian_colleges) if i < len(indian_colleges) else f"{fake.company()} College"
    fees = random.randint(20000, 300000)
    established_on = random.randint(1950, 2020)
    offered_courses = ", ".join(random.sample(courses, random.randint(1, 3)))
    class_timings = f"{random.randint(8, 10)} AM - {random.randint(3, 6)} PM"
    cutoff_marks = random.randint(60, 100)
    offered_facilities = ", ".join(random.sample(facilities, random.randint(2, 5)))
    location_lat = random.uniform(8.0, 37.0)
    location_lon = random.uniform(68.0, 97.0)

    data.append([
        college_name,
        fees,
        established_on,
        offered_courses,
        class_timings,
        cutoff_marks,
        offered_facilities,
        location_lat,
        location_lon
    ])

# Create a DataFrame
columns = [
    "college_name",
    "fees",
    "established_on",
    "courses_offered",
    "class_timings",
    "cutoff_marks",
    "facilities",
    "location_lat",
    "location_lon"
]
college_data = pd.DataFrame(data, columns=columns)

# Save to CSV
college_data.to_csv('data.csv', index=False)
print("Indian college data generated and saved to 'data.csv'.")
