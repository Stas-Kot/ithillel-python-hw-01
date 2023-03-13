# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print('We are ready to help you anytime!')

try:
    print('Welcome to quadratic equation calculator!')
    print('This online calculator is a quadratic equation solver that will solve '
          'a second-order polynomial equation such as ax2 + bx + c = 0 for x, ')
    print('where a ≠ 0, using the quadratic formula.')
    a = int(input('Insert integer number a: '))
    b = int(input('Insert integer number b: '))
    c = int(input('Insert integer number c: '))

    d = b * b - 4 * a * c
    print(d)
    print(d ** (0.5))

    if d == 0:
        x = -1 * b / (2 * a)
        result = 'x = ' + str(x)

    elif d > 0:
        x1 = (-1 * b + d ** (0.5)) / (2 * a)
        x2 = (-1 * b - d ** (0.5)) / (2 * a)
        result = 'x1 = ' + str(x1) + ' and ' + 'x2 = ' + str(x2)

    print(result)


except ValueError:
    print('You didn`t insert an integer number! Calculator closed!')

if __name__ == '__main__':
   main()

