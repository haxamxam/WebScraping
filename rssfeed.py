import feedparser
import pandas as pd
import time
import csv
from bs4 import BeautifulSoup


def read_data():
        RSSFeed = feedparser.parse(
                "https://www.upwork.com/ab/feed/jobs/rss?replace_with_your_rss_feed_link")
        df = pd.DataFrame()

        df['Date'] = [post.published for post in RSSFeed.entries]
        df['Title'] = [post.title for post in RSSFeed.entries]
        df['Summary'] = [post.summary for post in RSSFeed.entries]
        df['Link'] = [post.link for post in RSSFeed.entries]
        df['Description'] = [post.description for post in RSSFeed.entries]
        return df

def edit_data():
        df = read_data()
        full_df = df['Description']

        t = []
        e = []
        o = []
        p = []
        for i in full_df:
                soup = BeautifulSoup(i, "html.parser")
                b = soup.find_all("b")
                t.append(["".join(t.next_sibling.string.split()[1:]) for t in b][0])
                e.append(["".join(t.next_sibling.string.split()[1:]) for t in b][-1])
                o.append(["".join(t.next_sibling.string.split()[1:]) for t in b][2])
                p.append(["".join(t.next_sibling.string.split()[1:]) for t in b][-2])

        df['Price'] = t
        df['Country'] = e
        df['Category'] = o
        df['Skills'] = p
        df.to_csv('upwork.csv', mode='a', header=False, index=False)
        return df


if __name__ == '__main__':
        while True:
                parser = read_data()
                print(read_data())
                print(edit_data())
                time.sleep(800)


