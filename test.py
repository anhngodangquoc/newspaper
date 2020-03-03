from newspaper import Article

url = 'https://vnexpress.net/thoi-su/10-guong-mat-tre-viet-nam-tieu-bieu-nam-2019-4063675.html'

article = Article(url=url, language='vi')
article.download()
article.parse()
article.nlp()
# print(article.text)
# print(article.title)
print(article.summary)
print(article.keywords)
