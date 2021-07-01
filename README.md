# test-python-selenium

This program is my first dip into using Selenium for automated testing. My language of choice for this is Python.

## Features

### test.py
In it's current state, test.py will take the urls from the .csv file. For each url, the program will try to load the page. If successful a screenshot will be taken, if not an error message will be printed.

### list-urls.py
Different approach using seleniumbase to tackle the issue of taking screenshots of each page on a website. This programm will list all the urls on a website when run via pytest -s list-urls.py.

### page.py
Following on from the above, page.py will try to visit each of the urls listed above and take a screenshot, displaying errors if there are any. 

## TODO

The above are currently optimised for a specific CSS selector where pages are located by `"li.menu-item a"`. It will need testing to see if it works with just `"li a"` as a selector as not all sites consistently have "menu-item" as a class.

	> This appears to work and has overall better coverage despite bringing in some redundant links (social media, etc). Slightly slower speeds are expected (test data of 8 urls == 4:30 for "li.menu-item a" and 5:45 for "li a"
