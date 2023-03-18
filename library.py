import json
import requests


def get_repo_properties(repo_name):
    url = f"http://api.github.com/repos/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_data = json.loads(response.text)
        return {"created_at": repo_data["created_at"], "forks_count": repo_data["forks_count"],
                "stargazers_count": repo_data["stargazers_count"]}
    else:
        raise ValueError(f"Failed to retrieve properties for repo {repo_name}.")
