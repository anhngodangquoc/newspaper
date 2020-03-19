from newspaper import Article
from newspaper.article import ArticleDownloadState
from newspaper import Config
import pandas as pd
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
Italy ghi nhận 2.987 người chết vì nCoV sau khi tăng 475 ca trong một ngày, gần bằng số ca tử vong ở Trung Quốc là 3.237.

Cơ quan Bảo vệ Dân sự Italy cho biết nước này ghi nhận thêm 475 người chết vì nCoV, mức tăng trong ngày cao nhất thế giới và cao nhất từ khi nước này công bố số liệu. Trong số 475 ca, riêng vùng Lombardy ghi nhận 319 trường hợp.

Tổng cộng 35.713 người nhiễm nCoV, 2.978 người chết, 4.025 người bình phục ở Italy tính đến 19/3. Số người chết vì nCoV ở Italy chiếm hơn 1/3 số ca tử vong toàn cầu, trong bối cảnh nước này đã đóng cửa tất cả các doanh nghiệp, cấm các cuộc tụ họp công cộng.

Tỷ lệ tử vong ở Italy là 8,3%, cao gấp đôi tỷ lệ trung bình toàn cầu 4,1%. Dân số già và bệnh viện quá tải là hai trong số các nguyên nhân khiến tỷ lệ tử vong ở nước này đặc biệt cao.

Nhân viên nhà tang lễ đưa thi thể người chết vì nCoV đến nghĩa trang Bergamo, Italy hôm 16/3. Ảnh: Reuters.

"Biện pháp chính hiện nay là đừng từ bỏ", Giám đốc Viện Y tế Quốc gia Italy Silvio Brusaferro nói tại Rome ngày 18/3. "Sẽ mất vài ngày trước khi chúng ta thấy được lợi ích của các biện pháp ngăn chặn. Chúng tôi phải tiếp tục duy trì để thấy tác dụng của chúng và
trên hết là bảo vệ những người dễ bị tổn thương nhất", Brusaferro nói.

Dịch đang lây lan mạnh ở châu Âu. Ngoài Italy, Tây Ban Nha ghi nhận hơn 14.700 nhiễm, 638 ca tử vong, Đức hơn 12.300 ca nhiễm, 28 người chết, Pháp hơn 9.100 người nhiễm, 264 ca tử vong, Anh hơn 2.600 ca nhiễm, 104 người tử vong.

Covid-19 xuất hiện ở 173 quốc gia và vùng lãnh thổ kể từ khi dịch khởi phát ở Vũ Hán, Trung Quốc tháng 12/2019, khiến hơn 218.000 nhiễm, gần 9.000 người chết, hơn 84.000 người hồi phục. Tổ chức Y tế Thế giới (WHO) đã tuyên bố đây là đại dịch và kêu gọi các quốc g
ia tăng cường các biện pháp ứng phó.

"""
article.title="Covid-19: Gần 500 người chết vì Covid-19 ở Italy trong một ngày"

article.nlp()
print(article.keywords)
print(article.summary)

