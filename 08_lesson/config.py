class Config:
    BASE_URL = "https://ru.yougile.com"
    API_URL = f"{BASE_URL}/api-v2"
    
    # вставить Токен
    API_TOKEN = "fQkavIAxDgVBf4FVaPgwMsEzf-Ef3nb19szRascvWJjv2XHH75111NOUSw06ZLE6"

    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }