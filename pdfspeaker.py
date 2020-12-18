import pyttsx3
import PyPDF2
book = open('java.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(18 , pages):
    news = pdfReader.getPage(18)
    texts = news.extractText()
    speaker.say(texts)
    speaker.runAndWait()