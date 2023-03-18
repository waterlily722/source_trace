import requests

def execute_query(query):
    url = "http://api.github.com/search/code"
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'token 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',
               'Content-Type': 'application/json',
               'Accept': 'application/json'

               }
    response = requests.get(url, headers=headers, params=query)
    results = response.json()
    items = results.get("items", [])

    if response.status_code != 200:
        print('error: fail to request')

    # 提取需要的信息并存储在列表中
    search_results = []
    for item in items:
        repo_name = item["repository"]["full_name"]
        result = {"name": item["name"], "path": item["path"], "repo_name": repo_name}
        search_results.append(result)

    return search_results
