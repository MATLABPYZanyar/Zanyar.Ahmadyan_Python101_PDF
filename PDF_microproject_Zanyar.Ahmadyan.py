import pdfplumber

pdf = pdfplumber.open('Zanyar.pdf')
page = pdf.pages[0]
text = page.extract_text()
text.split('\n')
line = text.split('\n')[10]
print(line)