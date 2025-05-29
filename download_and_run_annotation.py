'''
This script downloads a an arxiv PDF from a specified URL
Then it runs the annotation script already done in the annotateai folder to annotate the PDF using the specified Ollama model.

The original PDF is stored in /Users/shreeharshabs/OneDrive - KTH/PDFs_to_read/regular
# and the annotated PDF is stored in the /Users/shreeharshabs/OneDrive - KTH/PDFs_to_read/annotated folder.

'''

import sys
import os
import requests

def download_pdf(url, save_path):
    """
    Downloads a PDF from the given URL and saves it to the specified path.
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded PDF to: {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python download_and_run_annotation.py <arxiv_pdf_url>")
        sys.exit(1)

    pdf_url = sys.argv[1]
    pdf_filename = os.path.basename(pdf_url)
    pdf_path = os.path.join('/Users/shreeharshabs/OneDrive - KTH/PDFs_to_read/regular', pdf_filename)

    # Download the PDF
    download_pdf(pdf_url, pdf_path)

    # Run the annotation script
    os.system(f"python annotateai/run_annotation.py '{pdf_path}'")
    
    os.system(f"mv '{pdf_path[:-4]}-annotated.pdf' '/Users/shreeharshabs/OneDrive - KTH/PDFs_to_read/annotated/{pdf_filename[:-4]}-annotated.pdf'")

if __name__ == "__main__":
    main()
