import PyPDF2
import openpyxl
#otwiera plik do zapisania
file=open(r"C:\Users\310295192\Desktop\inv.pdf",'rb')
#otwiera pdf
pdfreader = PyPDF2.PdfFileReader(file)
#dostaje sie do stron
print(pdfreader.getNumPages())
#otwiera pierwszą stronę
paging =pdfreader.getPage(0)
#wyciąga dane z pierwszej strony
strona = paging.extractText()
#zamienia kropki na przecinki
nowastrona=strona
print(nowastrona)
#znajduje początek listy
start_pack=nowastrona.find(')1')
#znalazlo na 83
#znajduje koniec listy
end_pack = nowastrona.find("TOTAL")
#tworzy zmienna tylko z danymi odnosnie paczek
products =nowastrona[start_pack+1:end_pack]
print(start_pack)
print(end_pack)
print(products)
