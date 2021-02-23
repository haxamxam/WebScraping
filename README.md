# WebScraping

Scraping data from upwork rss feed and creating a dataset from it using Feedparser and BeautifulSoup.

The csv is appended with new data after every 800 seconds.

# Timer Example

```python

if __name__ == '__main__':
        while True:
                parser = read_data()
                print(read_data())
                print(edit_data())
                time.sleep(800)
```
