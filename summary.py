from gensim.summarization.summarizer import summarize
from newspaper import Article


url ='https://n.news.naver.com/article/016/0002101900?ntype=RANKING'
news = Article(url)
news.download()
news.parse()
text = summarize(news.text, ratio=0.4)
print("=====")
print(text)
print("=====")