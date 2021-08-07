####Just a scratch file to test out stuff
import nltk
nltk.download('punkt')

from newspaper import Article

url = 'https://www.cnn.com/2021/08/06/politics/doj-clark-trump-election/index.html'
article = Article(url)

article.download()

print(article.html)

article.parse()

print(article.text)

print(article.title)
