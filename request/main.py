import requests

response = requests.get("https://api.github.com/users/aitvaras66/repos")
# print(response.json()[1])
# print(type(response.text))
my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']}\nProject URL: {project['html_url']}\n")

