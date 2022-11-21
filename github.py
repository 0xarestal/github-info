import requests,sys
import json
import time
from colorama import Fore,init
init(convert=True)

print('''
   ____ ___ _____ _   _ _   _ ____    ___ _   _ _____ ___  
  / ___|_ _|_   _| | | | | | | __ )  |_ _| \ | |  ___/ _ \ 
 | |  _ | |  | | | |_| | | | |  _ \   | ||  \| | |_ | | | |
 | |_| || |  | | |  _  | |_| | |_) |  | || |\  |  _|| |_| |
  \____|___| |_| |_| |_|\___/|____/  |___|_| \_|_|   \___/ 
                                                             ''')
username = input("Enter the username: ")
url = "https://api.github.com/users/" + username
response = requests.get(url)

data = response.json()

# if the user isn't on github or wrong username 
if response.status_code == 404:
    print("The User Wasn't Found on Github")
    time.sleep(2)
    sys.exit()

print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Name: {Fore.RESET}{Fore.MAGENTA}" + data["name"]+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Bio: {Fore.RESET}{Fore.MAGENTA}" + data["bio"]+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Public Repos: {Fore.RESET}{Fore.MAGENTA}" + str(data["public_repos"])+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Public Gists: {Fore.RESET}{Fore.MAGENTA}" + str(data["public_gists"])+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Followers: {Fore.RESET}{Fore.MAGENTA}" + str(data["followers"])+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Following: {Fore.RESET}{Fore.MAGENTA}" + str(data["following"])+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Created At: {Fore.RESET}{Fore.MAGENTA}" + data["created_at"]+Fore.RESET)
print(f"{Fore.RED} INFO : {Fore.RESET}{Fore.CYAN}Updated At: {Fore.RESET}{Fore.MAGENTA}" + data["updated_at"]+Fore.RESET)


repos_data = requests.get(data["repos_url"]).json()

output = {}
output["Name"] = data["name"] ; output["Bio"] = data["bio"] ; output["Public Repos"] = data['public_repos'] ; output['Public Gists'] = data['public_gists']
output["Followers"] = data['followers'] ; output['Following'] = data['following'] ; output["Created At"] = data["created_at"] ; output['Updated At'] = data['updated_at']
d = []
for i in repos_data:
    d.append(i['name'])
output['repos'] = d
with open('output.json','a') as f:
    d = str(open('output.json').read().splitlines())
    if username in d:
        print(f"{Fore.RED} INFO : {Fore.LIGHTMAGENTA_EX} Username Already In File {Fore.RESET}")
        sys.exit(0)
        
    v = {} ; v[username] = output
    json.dump(v,f) ; f.close()

time.sleep(2)
print(f"{Fore.RED} INFO : {Fore.GREEN}Saved the data in a file{Fore.RESET}")
time.sleep(3)
