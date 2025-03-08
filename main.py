import requests, random

users = []
wpm = 195

# User creation

for i in range(10):
    name = f"tcswc_russiahacker{random.random()}"
    body = {
        "username":name,
        "password":"Hello@world1!",
        "full_name":"Russia Hacker",
        "tests": [
            {
                "wpm":0,
                "accuracy":0
            }
        ]
    }
    request = requests.post('https://tcs-typer.netlify.app/api/register', json=body)

    if request.status_code != 200:
        print(f"User creation request {i} of 10 failed with status code {request.status_code}!")
    else:
        print(f"User creation request {i} of 10 succeded with status code {request.status_code}!")
        users.append(name)
    
for user in users:
    for i in range(25):
        body = {
            "username":user,
            "wpm":wpm,
            "accuracy":100
        }
        request = requests.post('https://tcs-typer.netlify.app/api/test', json=body)

        if request.status_code != 200:
            print(f"Test creation request {i} of 25 for user {user} failed with status code {request.status_code}!")
        else:
            print(f"Test creation request {i} of 25 for user {user} succeded with status code {request.status_code} and wpm {wpm}!")
    wpm = wpm - 1

print("Leaderboard spam completed!")