from pi_task.area_func import *

r = int(input('Введите радиус круга:\n'))

a = int(input('Введите длину прямоугольника:\n'))
b = int(input('Введите ширину прямоугольника:\n'))

if area_circle(r) > area_rect(a, b):
    print('Площадь круга больше')
else:
    print('Площадь прямоугольника больше')

if __name__ == 'main':
    main()
