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

def test_report():
    URL = 'https://en.wikipedia.org/wiki/Nintendo'
    actual = get_citations_needed_report(URL).split('\n')[0]
    expected = "The organization was reshaped nationwide in the following decades, and those core sales and marketing business functions are now directed by the office in Redwood City, California. The company's distribution centers are Nintendo Atlanta in Atlanta, Georgia, and Nintendo North Bend in North Bend, Washington. As of 2007[update], the 380,000-square-foot (35,000 m2) Nintendo North Bend facility processes more than 20,000 orders a day to Nintendo customers, which include retail stores that sell Nintendo products in addition to consumers who shop Nintendo's website.[226] Nintendo of America operates two retail stores in the United States: Nintendo New York on Rockefeller Plaza in New York City, which is open to the public; and Nintendo Redmond, co-located at NoA headquarters in Redmond, Washington, which is open only to Nintendo employees and invited guests. Nintendo of America's Canadian branch, Nintendo of Canada, is based in Vancouver, British Columbia with a distribution center in Toronto, Ontario.[citation needed] Nintendo Treehouse is NoA's localization team, composed of around 80 staff who are responsible for translating text from Japanese to English, creating videos and marketing plans, and quality assurance.[227]"
    assert actual == expected

def test_report_not_working():
    URL = 'https://en.wikipedia.org/wiki/Nintendo'
    actual = get_citations_needed_report(URL).split('\n')[0]
    expected = "In a related action, Nintendo sent a cease and desist letter to the organizers of the 2020 The Big House Super Smash Bros. tournament that was held entirely online due to the COVID-19 pandemic that year. Nintendo had taken issue with the tournament using emulated versions of Super Smash Bros. Melee which had included a user mod for networked play, as this would have required ripping a copy of Melee to play, an action they cannot condone.[254]"
    assert actual != expected
