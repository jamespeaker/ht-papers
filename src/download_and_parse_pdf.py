import PyPDF2
import requests

from utils import ensure_dir_exists

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def download_pdf(url, file_name):
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return False
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"PDF downloaded successfully as {file_name}")
    return True


def main():
    c=0
    with open("src/data/pdfs.txt") as f_in:
        for pdf_link in f_in:
            pdf_link = pdf_link.replace("\n","")
            print()
            print("#"*100)
            print(c)
            print(pdf_link)

            pdf_name = pdf_link.split("/")[-1]

            pdf_path = f"src/data/pdfs/{pdf_name}"
            ensure_dir_exists(pdf_path)
            success = download_pdf(pdf_link,pdf_path)

            if not success:
                continue

            try:
                pdf_text = extract_text_from_pdf(pdf_path=pdf_path)
                text_path = pdf_path.replace(".pdf",".txt").replace("/pdfs/","/corpora/")
                ensure_dir_exists(text_path)
                with open(text_path,"w") as f_out:
                    f_out.write(pdf_text)
            except Exception as e:
                print(e)
            c+=1


if __name__=="__main__":
    main()