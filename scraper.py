import requests
from bs4 import BeautifulSoup
url= "https://en.wikipedia.org/wiki/History_of_Mexico"
def  get_citations_needed_count(url):
    """
    this function countes the p that need citation
    and return the number of p
    """
    page= requests.get(url)
    soup= BeautifulSoup(page.content,"html.parser")
    all=soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    arr=[]
    for i in all:
        citation=i.find("span")
        arr.append(citation)
    return len(arr)

def get_citations_needed_report(url):
    """
    this function find the p that need citation
    and return all of them in array
    """
    page= requests.get(url)
    soup= BeautifulSoup(page.content,"html.parser")
    all=soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    arr=[]
    for i in all:
        citation=i.find("span").parent.parent.parent.parent.text
        arr.append(citation)
    return arr

print(get_citations_needed_count(url))
def print_all_p_that_citations_needed():
    """
    this function for printingn all p
    """
    all_p=get_citations_needed_report(url)
    for i in all_p:
        print(i)
        print("\n")
        
print_all_p_that_citations_needed()




