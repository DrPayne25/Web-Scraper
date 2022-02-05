from web_scraper.scraper import get_citations_needed_report, get_citations_needed_count

import pytest

def test_count():
    URL = 'https://en.wikipedia.org/wiki/Nintendo'
    actual = get_citations_needed_count(URL)
    expected = 4
    assert actual == expected

def test_count_not_working():
    URL = 'https://en.wikipedia.org/wiki/Sony'
    actual = get_citations_needed_count(URL)
    expected = 4
    assert actual != expected
