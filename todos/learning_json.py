# Taken from https://realpython.com/python-json/

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Which users have completed the most tasks?

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user
for todo in todos:
    if todo["completed"]:
        try:
            # Incrementing the existing user's count
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen so set their count to 1
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs
max_complete = top_users[0][1]

# Create a list of all users who have completed the maximum
# number of TODOs
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

s = "s" if len(users) > 1 else ""
print(f"User{s} {max_users} completed {max_complete} TODOs")

def keep(todo_item):
    """Filter out completed TODOs of users with max completed TODOs"""
    is_complete = todo_item["completed"]
    has_max_count = str(todo_item["userId"]) in users
    return is_complete and has_max_count

with open("filtered_data.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)
