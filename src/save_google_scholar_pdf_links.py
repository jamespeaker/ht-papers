import requests
from bs4 import BeautifulSoup

from utils import ensure_dir_exists

def html_to_text(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract and return the text
    return soup.get_text()


def extract_links(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <a> tags and extract href attributes
    links = []
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    
    return links



def main():
    pdf_links = []

    for i in range(10,110,10):
        print(i)
        url = f"https://scholar.google.com/scholar?start={i}&q=human+trafficking&hl=en&as_sdt=0,5"
        r = requests.get(url)
        print(r)
        html = r.text
        links = extract_links(html)

        for link in links:
            if link.endswith(".pdf"):
                # print(link)
                pdf_links.append(link)

        print(i, r, len(pdf_links))

    save_pth = "src/data/pdfs.txt"
    ensure_dir_exists(save_pth)
    with open(save_pth,"w") as f_out:
        for pdf_link in pdf_links:
            f_out.write(pdf_link+"\n")
        

if __name__=="__main__":
    main()