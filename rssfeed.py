import feedparser
import pandas as pd
import time
import csv
from bs4 import BeautifulSoup


def read_data():
        RSSFeed = feedparser.parse(
                "https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=1337378355181158401&amp;paging=0%3B10&amp;q=&amp;securityToken=b3ca045a00546b0827978b274aeb245a10809a97d1f8f145bc8761c9dfdb648ed92df76358492c1aa57baa9e388323d3584f68ce096828d61273a659c9d765c7&amp;sort=recency&amp;userUid=1337378355172769792")
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


