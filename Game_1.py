#   Определяем начальные значения переменных
min_max = [0, 1000]
vvod = (min_max[0] + min_max[1]) / 2
v_text = {1:'нижний предел', 2:'верхний предел', 3:'отгадываемое число'}

#   Создаем функцию проверки ввода
def prov_vvoda(vd_text):
    global vvod
    while True:
        sp = input('Введите ' + v_text[vd_text] + ' (от ' + str(min_max[0]) + ', до ' + str(min_max[1]) + ')\nили нажмите "Enter" для выхода:')
        if sp == '':
            raise SystemExit(1)
        elif not sp.isdigit():
            print('Ну это же не положительное число!')
        else:
            vvod = int(sp)
            if min_max[0] <= vvod <= min_max[1]:
                break
            else:
                print('Число не соответствует условию (от ', min_max[0], ', до ', min_max[1], ')', sep = '')

#   Вводим пределы min_max, проверяем ввод
prov_vvoda(1)
min_max[0] = vvod
prov_vvoda(2)
min_max[1] = vvod

#   Генерируем случайное число в диапазоне min_max
import random
r_vopros = random.randint(min_max[0], min_max[1])

#   Предлагаем отгадать, проверяем ввод
print('Компьютером загадано число. Попробуйте отгадать!')
i_step = 1
while True:
    print('Попытка №', i_step, sep='')
    prov_vvoda(3)
    if r_vopros == vvod:
        print('Отлично! Загаданное число "', vvod, '" Вы угадали с ', i_step, '-й попытки!', sep = '')
        input('Нажмите "Enter" для выхода.')    
        raise SystemExit(1)
    elif r_vopros > vvod:
        if vvod > min_max[0]: min_max[0] = vvod
    else:
        if vvod < min_max[1]: min_max[1] = vvod
    i_step += 1
input('Нажмите "Enter" для выхода.')
