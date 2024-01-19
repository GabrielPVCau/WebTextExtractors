import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Erro ao acessar a página: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')

        if not articles:
            print("Nenhum artigo encontrado na página.")
            return

        for article in articles:
            article_text = article.get_text()
            print(article_text)

            with open('artigos.txt', 'a', encoding='utf-8') as file:
                file.write(article_text + '\n\n')

    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")

# URL do site que você deseja raspar
url = 'http://exemplo.com'
scrape_site(url)
