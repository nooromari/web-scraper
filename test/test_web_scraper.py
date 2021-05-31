from web_scraper.web_scraper import *

def test_scraper_count():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(URL)
    expected = 5
    assert actual == expected

def test_scraper_report():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    result = get_citations_needed_report(URL)
    actual = result[0]
    print(actual)
    expected ='The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.\n'
    assert actual == expected