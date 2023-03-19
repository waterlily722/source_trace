from typing import List
from library import get_repo_properties


def sort_repositories(repositories: List[str]) -> List[str]:
    properties = []
    for repo in repositories:
        repository_property = get_repo_properties(repo)
        properties.append((repo, repository_property))

    # 排序
    sorted_repositories = sorted(
        properties,
        key=lambda x: (-x[1]['forks_count'], -x[1]['stargazers_count'], x[1]['created_at'])
    )

    return [repo[0] for repo in sorted_repositories]
