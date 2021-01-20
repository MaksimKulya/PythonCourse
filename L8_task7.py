# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел.
#
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(f'Sum of two complex numbers:')
        return f'z = ({self.x + other.x}) + i({self.y + other.y})'

    def __mul__(self, other):
        print(f'Product of two complex numbers:')
        return f'z = ({self.x * other.x - (self.y * other.y)}) + i({self.x * other.y  + other.x * self.y})'

    def __str__(self):
        return f'z = ({self.x}) + i({self.y})'


z1 = ComplexNumber(1, -2)
print(z1)
z2 = ComplexNumber(3, 4)
print(z2)

print(z1 + z2)
print(z1 * z2)
