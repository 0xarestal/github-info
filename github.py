import requests
import json
import time


print('''
   ____ ___ _____ _   _ _   _ ____    ___ _   _ _____ ___  
  / ___|_ _|_   _| | | | | | | __ )  |_ _| \ | |  ___/ _ \ 
 | |  _ | |  | | | |_| | | | |  _ \   | ||  \| | |_ | | | |
 | |_| || |  | | |  _  | |_| | |_) |  | || |\  |  _|| |_| |
  \____|___| |_| |_| |_|\___/|____/  |___|_| \_|_|   \___/ 
                                                           - termed#7613
                                                             ''')
username = input("Enter the username: ")
url = "https://api.github.com/users/" + username
response = requests.get(url)

data = json.loads(response.text)

print("Name: " + data["name"])
print("Bio: " + data["bio"])
print("Public Repos: " + str(data["public_repos"]))
print("Public Gists: " + str(data["public_gists"]))
print("Followers: " + str(data["followers"]))
print("Following: " + str(data["following"]))
print("Created At: " + data["created_at"])
print("Updated At: " + data["updated_at"])

repos = data["repos_url"]
repos_response = requests.get(repos)
repos_data = json.loads(repos_response.text)

print("Repos: ")
for repo in repos_data:
    print(repo["name"])

with open("github.txt", "w") as file:
    file.write("Name: " + data["name"] )
    file.write("Bio: " + data["bio"] )
    file.write("Public Repos: " + str(data["public_repos"]) )
    file.write("Public Gists: " + str(data["public_gists"]) )
    file.write("Followers: " + str(data["followers"]) )
    file.write("Following: " + str(data["following"]) )
    file.write("Created At: " + data["created_at"] )
    file.write("Updated At: " + data["updated_at"] )
    file.write("Repos: " )
    for repo in repos_data:
        file.write(repo["name"])

with open("repos.txt", "w") as file:
    for repo in repos_data:
        file.write(repo["name"])
        
time.sleep(2)
print("Saved the data in a file")
time.sleep(3)
