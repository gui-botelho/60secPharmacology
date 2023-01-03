import bs4
import random
import re
import requests
from gtts import gTTS

random_number = random.randint(1, 1000)

link = f'https://go.drugbank.com/drugs/DB00{random_number}'

response = requests.get(link)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

data = soup.find_all('dd')


def clean(information):
    text = str(information)
    clean_text = re.sub('<.*?>[0-9]?[0-9]?', ' ', text)
    cleaner_text = re.sub('\s\(.*?\)', '', clean_text)
    cleanest_text = re.sub('\s+', ' ', cleaner_text)
    return cleanest_text


clean_data = {'summary': clean(data[0]), 'bg': clean(data[4]), 'mechanism': clean(data[16])}

compiled_text = ''

for value in clean_data.values():
    compiled_text += value

'''audio = gTTS(compiled_text, tld='com', lang='en', slow=False, )
audio.save(f'drugDB00{random_number}.mp3')'''

print(compiled_text)