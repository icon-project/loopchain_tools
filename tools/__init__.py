"""CLI tools for loopchain"""
from typing import Iterable, Union, List


def get_option_from_prompt(options: Iterable, default: Union[str, int] = 1,
                           is_index=True, allow_multiple=False) -> Union[int, List[int], None]:
    """get option from prompt and return choice

    :param options: iterable object of options
    :param default: default choice number (default: 1)
    :param is_index: True if result choice should be based on index number
    :param allow_multiple: True if user input is expected as multiple choices
    :return: choice(int) from user input or None
    """
    options_size = 0
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")
        options_size += 1

    print("\n0. Back")
    while True:
        choice = input(" >>  ") or str(default)

        if choice == '0':
            return None

        if not allow_multiple and not (0 < int(choice) <= options_size):
            print(f"out of range! input valid number.")
        else:
            break

    if allow_multiple:
        choice = [int(num) for num in choice.strip().split(" ")]
    else:
        choice = int(choice)

    if is_index:
        if isinstance(choice, list):
            return [num - 1 for num in choice]
        else:
            return choice - 1
    else:
        return choice
