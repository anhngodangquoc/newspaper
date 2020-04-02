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
Xuân Nghị được biết đến là một chàng diễn viên trẻ sở hữu nét hài duyên dáng và lối diễn khá tự nhiên, thu hút. Sau những thành công từ vai diễn Mr. Cần Trô, Xuân Nghị bắt đầu có những bước tiến vượt bậc trong sự nghiệp. Mới đây, anh đảm nhận vai nam chính trong một bộ phim truyền hình chiếu trên VTV3.

Vốn luôn xuất hiện với hình ảnh hài hước, lạc quan nhưng Xuân Nghị cho biết anh gặp phải không ít áp lực khi đảm nhận vai chính phim truyền hình đầu tay. “Lúc trước mình đã tạo được dấu ấn với vai Mr Cần Trô, do đó, thách thức của Nghị là phải làm sao cho vai Mr Xà Bông (Bách) phải xuất sắc hơn những gì mà mình từng làm được. Vượt qua chính mình là áp lực lớn nhất của Nghị”. 
Đặt mục tiêu vượt qua “cái bóng” của Mr Cần Trô, chỉ sau 3 tập phát sóng, vai Bách của Xuân Nghị trong bộ phim Nhà Trọ Balanha đã để lại được những dấu ấn đáng kể trong lòng khán giả.

Lần đầu, người hâm mộ được chứng kiến một Xuân Nghị vô cùng ấm áp, tâm lý. Nam diễn viên cho biết, vai Bách có nhiều nét tương đồng về tính cách với anh ngoài đời, nhất là sự hài hước, tuy nhiên, bản thân lại không “mê gái” như Bách. “Bách trong phim mê gái lắm, còn Nghị thì không đâu” (cười).

"""
article.title="Diễn viên Xuân Nghị: 'Áp lực lớn nhất của tôi là vượt qua 'cái bóng' của Mr Cần Trô'"

article.nlp()
print(article.keywords)
print(article.summary)

