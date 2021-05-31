import requests
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    result_list = list(result)
    length=len(result_list)
    return length



def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report_result = [a.parent.text for a in result]
    # uniqe_res = set(report_result)
    # list_res = list(uniqe_res)
    return report_result


if __name__ == '__main__':
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))