import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_article(article_url, headers):
    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Erro ao acessar a página do artigo: {response.status_code}")
            return ""

        article_soup = BeautifulSoup(response.text, 'html.parser')
        # Adapte a linha abaixo para a estrutura específica do site
        article_text = article_soup.get_text()
        return article_text

    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação do artigo: {e}")
        return ""

def scrape_site(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Erro ao acessar a página: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        # Adapte o seletor abaixo para a estrutura específica do site
        links = soup.find_all('a', href=True)

        for link in links:
            article_url = urljoin(url, link['href'])
            article_text = scrape_article(article_url, headers)

            if article_text:
                print(article_text)
                with open('artigos.txt', 'a', encoding='utf-8') as file:
                    file.write(article_text + '\n\n')

    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação da página inicial: {e}")

# URL do site que você deseja raspar
url = 'https://www.example.com'
scrape_site(url)
