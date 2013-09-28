from grab import Grab
from djangodash2013.settings import DEBUG_DIR

def get_months():
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august",
              9: "september", 10: "october", 11: "november", 12: "december"}

    return months

def parse_famous(year, month, day):
    '''
    parse famous from famousbirthdays.com
    by month day
    year is ignore now
    '''
    months = get_months()
    url = 'http://www.famousbirthdays.com/%s%d.html' % (months[month], day)

    g = Grab()
    g.setup()
    g.go(url)

    elements = g.doc.select('//ul[@class="top-celebrity-col4 col1"]/li')
    list = []

    for element in elements:
        src = element.node.getchildren()[1].getchildren()[0].getchildren()[0].get('src')
        age = element.node.getchildren()[2].getchildren()[0].text_content().split(' ')[-1]
        name = element.node.getchildren()[2].getchildren()[0].getchildren()[0].text_content()
        description = element.node.getchildren()[2].getchildren()[1].text_content()

        list.append({'src': src, 'name': name, 'age': age, 'description': description})

    return list

def parse_events_by_date(year, month, day):
    '''
    parse events from historyorb.com
    by year month day
    '''
    months = get_months()
    url = 'http://www.historyorb.com/events/date/%d/%s/%d' % (year, months[month], day)

    g = Grab()
    g.go(url)

    events = g.doc.select('//div[@id="main_text"]')[0].node.getchildren()[3].text_content().split("\n")

    return events
