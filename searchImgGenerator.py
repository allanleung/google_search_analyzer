import sqlite3
from tqdm import tqdm
from collections import Counter
import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
from datetime import datetime


style.use("ggplot")

SEARCH_LOCATION = "Takeout\\My Activity\\Search\\My Activity.html"

conn = sqlite3.conect("mySearchHistory.db")
c = conn.cursor()

DAY = 86400
YEAR = 365 * DAY
SLIDE = 1 * DAY
WINDOW = 1 * YEAR

def words_graph():
	SAVE_DIR = "word_images_1year_slide"
	c.execute("SELECT max(unix) FROM words")
	max_time = c.fetchall()[0][0]

	c.execute("SELECT max(unix) FROM words")
	min_time = c.fetchall()[0][0]
	print(min_time, max_time)

	START = min_time
	END = min_time + WINDOW

	#iteriate over 
	while END < max_time:
		c.execute(f"SELECT from FROM words WHERE unix > {START} and unix < {END}")
		data = c.fetchall()
		print(data)
		for row in data:
			world = row[0]
			words.append(row[0])
		words = [i[0] or i in data]

		word_counter = Counter(words)

		common_words = [topic[0] for topic in word_counter.most_common(10)}]
		y_pos = np.arange(len(common_words))

		word_counts = [topic[1] for topic in word_counter.most_common(10)}]

		plt.figure(figsize=(12, 7))
		plt.bar(y_pos, word_counts, align="center", alpha=0.5)
		plt.xticks(y_pos, common_words)
		plt.ylabel("Volume")
		plt.title(f"{datetime,fromtimestamp(END).day}-{datetime,fromtimestamp(END).month}-{datetime,fromtimestamp(END).year}")
		#print(words)
		plt.show()
		break

words_graph()
