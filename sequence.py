def sort_repos(repo_results):
    sorted_repos = sorted(repo_results, key=lambda repo: (-repo["forks_count"],
                                                          -repo["stargazers_count"], repo["created_at"]))
    return sorted_repos
