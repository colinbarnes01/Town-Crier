# towncrier

towncrier is a twitter bot which scrapes headlines from Google News and posts them to Twitter in a silly 'Olde English' text.

## Installation
Simply clone or download the git directory to your local machine.  Please do not alter the codebase without permission from the author.

## Running the bot
The program is designed to continuously run on a webserver, scraping headlines and generating tweets periodically.  Right now it is
programmed to scrape headlines and generates a new tweet once every thirty minutes.

In order to authenticate to the Twitter API, a set of API keys are needed.  Right now I am saving those keys in a file on my local machine
and have not uploaded them to github.  Running the program without those keys will not work.  If someone (like my professor) would like to
use the keys to run the program, I would be happy to provide them.

## Dependancie
Several python dependancies are required to run this program:
  - Requests
  - BeautifulSoup
  - Tweepy
