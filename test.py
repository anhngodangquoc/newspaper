from newspaper import Article
import pandas as pd


df = pd.read_csv("vnexpress_3_3.csv")
df.drop(columns=["text"], inplace=True)

df.to_excel("vnexpress.xlsx")