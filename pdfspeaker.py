# Write a program to convert pdf file into mp3
# By @NewBeginner2701

import pyttsx3  # You have to import the pyttsx3 from terminal using pip install pyttsx3
import PyPDF2   # You have to import the PyPDF2 from terminal using pip install PyPDF2
book = open('java.pdf', 'rb') # You have to mention the name of the PDF file in "  "
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages) # This will print the number of your mention pdf file
speaker = pyttsx3.init() 
for num in range(18 , pages): # In this you can set the range of the pages from ___ page to ____ page
    news = pdfReader.getPage(18) 
    texts = news.extractText()
    speaker.say(texts)
    speaker.runAndWait()
