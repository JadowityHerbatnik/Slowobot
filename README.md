# Slowobot

A simple [słowotok](https://www.slowotok.pl) ~~bot~~ assistant

![screen](/img/screenshot.png)


## Dependencies:

* [Selenium WebDriver](https://pypi.org/project/selenium/) (`pip install selenium`)
* [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)(for Chrome/Chromium support)
* or [geckodriver](https://github.com/mozilla/geckodriver/releases)(for Firefox support)

Put the driver somewhere in your PATH and you're good to go

###Usage

```
optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  Quiet mode. No words are going to be selected on the grid, but the dictionary is still going to be updated
  -l, --login  Use custom login credentials
  --firefox    Use Firefox (Chrome/Chromium is the default browser)
```
