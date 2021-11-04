import pdfToJson


def main():
    isuNumber = 335097
    variant = isuNumber % 36
    currentTask = pdfToJson.main(variant)  # parse Pdf to Json format
    print(f"Лабараторная работа № 4.\nНомер ISU: {isuNumber}\nВариант: {isuNumber} % 36 = {variant}\nЗадание:\nВариант: {currentTask['variant']},\nИсходный формат: {currentTask['sourceFormat']},\nРезультирующий формат: {currentTask['resultFormat']},\nДень недели: {currentTask['dayOfWeek']}")


if __name__ == '__main__':
    main()
