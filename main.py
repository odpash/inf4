import additional_one
import pdfToJson
import task_main
import time
import additional_two
import additional_four

def main():
    isu_number = 13
    variant = isu_number % 36
    current_task = pdfToJson.main(variant)
    print(
        f"Лабараторная работа № 4.\nПорядковый номер ISU: {isu_number}\nВариант: {isu_number} % 36 = {variant}\nЗадание:\nВариант: {current_task['variant']},\nИсходный формат: {current_task['sourceFormat']},\nРезультирующий формат: {current_task['resultFormat']},\nДень недели: {current_task['dayOfWeek']}\n\n")
    js = task_main.read_json()
    task_main.main(js)  # main target
    additional_one.main(js)  # first add
    additional_two.main()
    #### task 3 ####
    main_task_time = time.time()
    for _ in range(10):
        task_main.main(js)
    main_task_time = time.time() - main_task_time
    additional_one_time = time.time()
    for _ in range(10):
        additional_one.main(js)
    additional_one_time = time.time() - additional_one_time

    additional_two_time = time.time()
    for _ in range(10):
        additional_two.main()
    additional_two_time = time.time() - additional_two_time

    print(f"Дополнительное задание №3:\nВремя выполнения главного скрипта: {main_task_time},\nВремя выполнения дополнительного задания №1: {additional_one_time},\nВремя выполнения дополнительного задания №2: {additional_two_time}")

    additional_four.main(js)


if __name__ == '__main__':
    main()
