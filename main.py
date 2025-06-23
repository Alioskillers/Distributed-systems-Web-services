import threading
import random
from collections import defaultdict

# Binary lock for thread-safe dataset access
lock = threading.Lock()
dataset = []

# Constants
course_names = ["Machine Learning", "Cyber Security", "Data Science", "AI Ethics"]
universities = ["Stanford University", "MIT", "Harvard", "UC Berkeley"]

# Function to generate one random entry
def generate_entry():
    return {
        "Year": random.randint(2022, 2024),
        "Course Name": random.choice(course_names),
        "Grade": random.randint(60, 100),
        "University": random.choice(universities)
    }

# Thread-safe function to add entries
def add_entries(thread_id, num_entries):
    for _ in range(num_entries):
        entry = generate_entry()
        #to test without lock replace with lock by return
        with lock:
            dataset.append(entry)

# Simulate multiple threads adding data
def add(num_threads=10, entries_per_thread=5):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=add_entries, args=(i, entries_per_thread))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Verify and write the results to a file
def verify(filename="output.txt"):
    total_entries = len(dataset)
    course_distribution = defaultdict(int)

    for entry in dataset:
        course_distribution[entry["Course Name"]] += 1

    with open(filename, "w") as f:

        for course, count in course_distribution.items():
            f.write(f" - {course}: {count} entries\n")

        f.write("\nGenerated Entries:\n")
        for i, entry in enumerate(dataset):
            f.write(f"{i+1}. {entry}\n")

# Main execution
if __name__ == "__main__":
    add()
    verify()