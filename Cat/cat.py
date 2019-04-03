from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
text = open(path.join(d, 'cat.txt')).read()
cat_pic = np.array(Image.open(path.join(d, "cat.jpeg")))
stopwords = set(STOPWORDS)
stopwords.add("stop")
cat_wc = WordCloud(background_color="black", max_words=150, mask=cat_pic,
               stopwords=stopwords, max_font_size = 65, scale=4, min_font_size = 6)
cat_wc.generate(text)
plt.figure("CAT")
plt.imshow(cat_wc)
plt.axis("off")
plt.show()
