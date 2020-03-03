import pandas as pd
from tqdm import tqdm

import newspaper
from newspaper import Config

config = Config()
config.memoize_articles = False
config.fetch_images = False
config.verbose = True
config.MAX_SUMMARY_SENT = 10
config.language = "vi"

vnexpress = newspaper.build('https://vnexpress.net', config=config)
zingvn = newspaper.build('https://news.zing.vn', config=config)
kenh14 = newspaper.build('https://kenh14.vn/', config=config)
# list_url_slate_paper = []
# for article in slate_paper.articles:
#     list_url_slate_paper.append(article.url)
def extract_data(news, file_name):
    print("crawling: ", file_name)
    data = []
    for article in tqdm(news.articles):
        # count += 1
        # if count > 10:
        #     break
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
    df_frame.to_csv(f"{file_name}.csv")

extract_data(news=vnexpress, file_name="vnexpress_3_3")
extract_data(news=kenh14, file_name="kenh14_3_3")
extract_data(news=zingvn, file_name="zingvn_3_3")