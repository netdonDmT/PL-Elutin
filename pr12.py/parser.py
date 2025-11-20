import requests
import json

def get_repo_data(repo_name):
    repo_url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(repo_url)
    
    if response.status_code != 200:
        raise Exception(f"Ошибка: {response.status_code} - {response.text}")
    
    repo_info = response.json()
    
    owner_url = repo_info['owner']['url']
    owner_response = requests.get(owner_url)
    
    if owner_response.status_code != 200:
        raise Exception(f"Ошибка при получении данных владельца: {owner_response.status_code}")
    
    owner_info = owner_response.json()
    
    result = {
        'company': owner_info.get('company'),
        'created_at': repo_info.get('created_at'),
        'email': owner_info.get('email'),
        'id': repo_info.get('id'),
        'name': owner_info.get('login'),
        'url': owner_info.get('url')
    }
    
    with open('github_repo_data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    return json.dumps(result, indent=2, ensure_ascii=False)