import pandas as pd
from tqdm import tqdm

import newspaper
from newspaper import Config

config = Config()
config.memoize_articles = False
config.fetch_images = False
config.verbose = True
config.language = "vi"

slate_paper = newspaper.build('https://vnexpress.net', config=config)
# list_url_slate_paper = []
# for article in slate_paper.articles:
#     list_url_slate_paper.append(article.url)

data = []
count = 0
for article in tqdm(slate_paper.articles):
    count += 1
    if count > 10:
        break
    if "#box_comment" in article.url:
        continue
    temp = {"link": article.url}
    try:
        article.download()
        article.parse()
        article.nlp()

        temp["keyword"] = ";".join(article.keywords)
        temp["summary"] = article.summary
        temp["text"] = article.text
        temp["title"] = article.title
        temp["publish_date"] = article.publish_date
    except Exception as e:
        print(e)
        pass
    data.append(temp)
# print(data)
df_frame = pd.DataFrame(data)
print(df_frame.head())
print(len(df_frame))
df_frame.to_csv("vnexpress_test.csv")
