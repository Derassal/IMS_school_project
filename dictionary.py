import requests
import urllib
from bs4 import BeautifulSoup
import warnings
from bs4 import MarkupResemblesLocatorWarning
import urllib.parse
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def get_definition(word):
  url = f"https://sinonim.org/t/{urllib.parse.quote_plus(word)}"
  payload = {}
  headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'usedSug=1; num_hits=8; num_hits=9',
    'priority': 'u=0, i',
    'referer': 'https://sinonim.org/t/book',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
  }

  html = requests.request("GET", url, headers=headers, data=payload).text
  soup = BeautifulSoup(html, "html.parser")
  definition = '\n'.join([el.get_text() for el in soup.find_all("ol")])
  if not definition:
    definition = '\n'.join([el.get_text() for el in soup.find_all("p")])
  return definition.split(' ◆')[0] + '.'


