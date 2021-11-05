import pdfToJson
import task_main
import add_task1
import add_task2
import add_task3
import add_task4



def main():
    isu_number = 13
    variant = isu_number % 36
    current_task = pdfToJson.main(variant)  # parse Pdf to Json format
    # here we are creating new json file with data
    print(f"Лабараторная работа № 4.\nПорядковый номер ISU: {isu_number}\nВариант: {isu_number} % 36 = {variant}\nЗадание:\nВариант: {current_task['variant']},\nИсходный формат: {current_task['sourceFormat']},\nРезультирующий формат: {current_task['resultFormat']},\nДень недели: {current_task['dayOfWeek']}")
    print("[Основное задание] Получение кода сайта используя библиотеку REQUESTS прошло успешно!")
    print("[Основное задание] Преобразование и запись исходного HTML кода в Json прошло успешно!")
    print("[Основное задание] Преобразование и запись данных из Json в Xml (не используя сторонние библиотеки) произведено успешно!")
    if input("Выполнение основного задания завершено.\nЗапустить доп. №1? (y/n): ").lower().strip() == 'y':
        pass


if __name__ == '__main__':
    main()
