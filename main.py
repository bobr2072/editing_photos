import sys
import os

from photo_editing import photo_edit


relative_path = os.path.basename(__file__)


def help():

    print('\n\n======= List of available functions: =======\n\n')

    for func in functions:
        print(f'{func} ---> python {relative_path} {func}\n')


if __name__ == "__main__":

    functions = {
        'help': help,
        'apply_film_effect': photo_edit.apply_film_effect,
        'black_and_white': photo_edit.black_and_white,
    }

    if len(sys.argv) < 2:
        print('\n!!!!!! Incorrect call !!!!!!')
        help()
    else:
        function_name = sys.argv[1]
        selected_function = functions.get(function_name)
        if selected_function:
            selected_function()
        else:
            print('\n!!!!!! Unknown function !!!!!!\n')
