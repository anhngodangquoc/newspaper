from newspaper import Article
from newspaper.article import ArticleDownloadState
from newspaper import Config
MAX_SUMMARY_SENT=10
config = Config()
config.memoize_articles = False
config.fetch_images = False
config.verbose = True
config.MAX_SUMMARY_SENT = MAX_SUMMARY_SENT
config.language = "vi"

# article = Article("https://vnexpress.net/the-gioi/so-nguoi-chet-o-italy-vi-ncov-gan-bang-trung-quoc-4071469.html", config=config)
# article.download()
# article.parse()

article = Article("temp", config=config)
article.download_state = ArticleDownloadState.SUCCESS
article.is_parsed = True
article.text = """
Italy ghi nhận 2.987 người chết vì nCoV sau khi tăng 475 ca trong một ngày, gần bằng số ca tử vong ở Trung Quốc là 3.237. Cơ quan Bảo vệ Dân sự Italy cho biết nước này ghi nhận thêm 475 người chết vì nCoV, mức tăng trong ngày cao nhất thế giới và cao nhất từ khi nước này công bố số liệu. Trong số 475 ca, riêng vùng Lombardy ghi nhận 319 trường hợp. Tổng cộng 35.713 người nhiễm nCoV
"""
# article.title="Covid-19: Gần 500 người chết vì Covid-19 ở Italy trong một ngày"

article.nlp()
print(article.keywords)
print(article.summary)

