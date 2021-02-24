# WebScraping

Scraping data from upwork rss feed and creating a dataset from it using Feedparser and BeautifulSoup.

The csv is appended with new data after every 800 seconds.

# Code

```python
#Add your rss feed link to the feedparser
RSSFeed = feedparser.parse(
                "https://www.upwork.com/ab/feed/jobs/rss?replace_with_your_rss_feed_link")
                

if __name__ == '__main__':
        while True:
                parser = read_data()
                print(read_data())
                print(edit_data())
                #timer for 800 seconds
                time.sleep(800)
```
