import io
import json
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def getLastPage():
    with open('task.pdf', 'rb') as sourceFile:
        for page in PDFPage.get_pages(sourceFile):
            resource_manager, ioString = PDFResourceManager(), io.StringIO()
            converter = TextConverter(resource_manager, ioString)
            PDFPageInterpreter(resource_manager, converter).process_page(page)
            text = ioString.getvalue()
            converter.close()
            ioString.close()
    return text


def parsePage(text):
    result = []
    text = text.split('День недели ')[1].split()
    for i in range(0, len(text), 4):
        result.append({'variant': int(text[i]), 'sourceFormat': text[i + 1], 'resultFormat': text[i + 2],
                       'dayOfWeek': text[i + 3]})
    return result


def writeJson(toWrite):  # if we need .json file
    with open('taskVariant.json', 'w', encoding='UTF-8') as outfile:
        json.dump(toWrite, outfile, ensure_ascii=False)
    outfile.close()
    return toWrite


def main(taskIndex):
    if taskIndex == -1:
        return parsePage(getLastPage())
    return writeJson(parsePage(getLastPage())[taskIndex])
