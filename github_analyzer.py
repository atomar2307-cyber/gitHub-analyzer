
import requests
username = input("Enter GitHub username: ")

# User data
user = requests.get(f"https://api.github.com/users/{username}").json()

# Followers data
followers = requests.get(user.get("followers_url")).json()

# Repos data
repos = requests.get(user.get("repos_url")).json()

# Output
print("\n--- USER INFO ---")
print("Username:", user.get("login"))
print("Followers:", user.get("followers"))
print("Following:", user.get("following"))
print("Total Repos:", len(repos))

print("\n--- TOP REPOS ---")
for repo in repos[:5]:
    print(repo["name"], "⭐", repo["stargazers_count"])

print("\n--- FOLLOWERS ---")
for f in followers[:5]:
    print(f["login"])
