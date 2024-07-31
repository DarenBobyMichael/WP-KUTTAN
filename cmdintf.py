from dotenv import load_dotenv
load_dotenv()

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter

from prompt_smart_menu import PromptSmartMenu
from prompt_smart_menu.helpers import InvalidArgError
from wpservice import retrieve
import os



def help():
    print("Use tab completion to input your command.")

menu_config = [
    {
        'command': 'retrieve',
        'function': retrieve,
    },
    {
        'command': 'help',
        'function': help,
    },
    {
        'command': 'exit',
        'function': exit,
    }
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    psm = PromptSmartMenu(menu_config, validate_args=True)
    completer_dict = psm.nested_completer_dict()

    completer = NestedCompleter.from_nested_dict(completer_dict)

    session = PromptSession(completer=completer)
    while True:
        try:
            command = session.prompt('\n\nWP BOT\n=======\n*Type help for commands info*\n\nEnter cmd: ')
            try:
                psm.run(command)
            except InvalidArgError as err:
                print(f'Bad input: {err}')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

if __name__ == '__main__':
    main()