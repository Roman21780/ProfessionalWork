from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ChromeOptions

# Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL страницы со статьями
URL = 'https://habr.com/ru/articles/'

# Функция для ожидания элемента
def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None

# Функция для получения полного текста статьи
def get_full_article_text(browser, article_url):
    try:
        # Переходим на страницу статьи
        browser.get(article_url)
        article_body = wait_element(browser, delay=10, by=By.CLASS_NAME, value="article-formatted-body")
        if not article_body:
            return ""
        return article_body.text.strip()

        # Получаем HTML-код страницы статьи
        # article_html = browser.page_source
        # article_soup = BeautifulSoup(article_html, 'lxml')
        # Извлекаем весь текст статьи
        # full_text = ' '.join(p.text.strip() for p in article_soup.find_all('p'))
        # return full_text
    except Exception as e:
        print(f"Ошибка при получении текста статьи: {e}")
        return ""

# Настройка Selenium с автоматической загрузкой ChromeDriver
options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Загружаем страницу
    browser.get(URL)
    # time.sleep(5)  # Ждем, пока JavaScript загрузит контент

    # Ждем появления статей на странице
    articles_container = wait_element(browser, delay=10, by=By.TAG_NAME, value="article")
    if not articles_container:
        print("Статьи не найдены на странице.")
        exit()

    # Получаем HTML-код страницы после полной загрузки
    html = browser.page_source

    # Парсим HTML-код
    soup = BeautifulSoup(html, 'lxml')

    # Находим все статьи на странице
    articles = soup.find_all('article')
    print(f"Найдено статей: {len(articles)}")

    # Проходим по каждой статье и проверяем наличие ключевых слов
    for article in articles:
        try:
            # Получаем заголовок статьи
            title_tag = article.find('h2', class_='tm-title')
            if not title_tag:
                continue
            title = title_tag.text.strip()

            # Получаем ссылку на статью
            if title_tag and title_tag.find('a'):
                link = title_tag.find('a')['href']
                full_url = f"https://habr.com{link}"
            else:
                continue

            # Получаем дату публикации
            date_tag = article.find('time')
            if not date_tag:
                continue
            date = date_tag['datetime']

            # Получаем preview-информацию (текст статьи)
            preview_div = article.find('div', class_=lambda x: x and 'article-formatted-body' in x)
            preview_text = ""
            if preview_div:
                # Собираем весь текст из тегов <p> внутри preview
                preview_text = ' '.join(p.text.strip() for p in preview_div.find_all('p'))

            # Получаем полный текст статьи
            full_text = get_full_article_text(browser, full_url)

            # Объединяем preview и полный текст
            combined_text = f"{preview_text} {full_text}"

            # Проверяем, есть ли в тексте хотя бы одно ключевое слово
            if any(keyword.lower() in combined_text.lower() for keyword in KEYWORDS):
                # Выводим информацию о статье
                print(f'{date} - {title} - {full_url}')
        except Exception as e:
            print(f"Ошибка при обработке статьи: {e}")

finally:
    # Закрываем браузер
    browser.quit()