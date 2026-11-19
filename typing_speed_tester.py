import time
from io import TextIOWrapper
from pathlib import Path
from typing import Literal

SENTENCE_FILE = Path('sentences.txt')
PREMADE_SENTENCES = [
    'the quick brown fox jumps over the lazy dog',
    'the five boxing wizards jump quickly',
    'sphinx of black quartz judge my vow',
    'pack my box with five dozen liquor jugs',
    'how vexingly quick daft zebras jump',
    'jackdaws love my big sphinx of quartz',
    'a quick movement of the enemy will jeopardize six gunboats',
    'amazingly few discotheques provide jukeboxes',
    'we promptly judged antique ivory buckles for the next prize',
    'my girl wove six dozen plaid jackets before she quit',
]


def ask_question(question: str, confirm: bool) -> str:
    while True:
        answer = input(f'{question}: ').lower().strip()
        if not answer:
            print('Must not be empty')
            continue
        if confirm:
            answer_confirmed = confirm_answer(answer)
            if not answer_confirmed:
                continue
        return answer


def ask_question_with_answers(question: str, answers: list, confirm: bool) -> str:
    while True:
        answer = ask_question(question, confirm)
        if answer not in answers:
            print('Not a valid option')
            continue
        return answer


def confirm_answer(answer: str) -> bool: # pyright: ignore[reportReturnType]
    confirmation = ask_question_with_answers(f'Is {answer} correct?', ['y', 'n'], False)
    match confirmation:
        case 'y':
            return True
        case 'n':
            return False


def open_sentence_file(mode: Literal['r', 'w', 'a']) -> TextIOWrapper:
    return open(SENTENCE_FILE, mode, encoding='utf-8')


def read_sentence_file() -> list:
    with open_sentence_file('r') as f:
            sentences = f.read()
    return sentences.splitlines()


def fill_sentence_file() -> None:
    with open_sentence_file('w') as f:
        for sentence in PREMADE_SENTENCES:
            f.write(f'{sentence}\n')


def load_sentences() -> None:
    try:
        existing_sentences = read_sentence_file()
        print('Using existing sentence file')
        if existing_sentences:
            print('Using existing sentences')
        else:
            print('Filling in premade sentences')
            fill_sentence_file()
    except FileNotFoundError:
        print('Creating sentence file')
        fill_sentence_file()


def list_sentences():
    sentences = read_sentence_file()
    print('\nYour current sentences are:')
    for number, sentence in enumerate(sentences, 1):
        print(f'{number}. {sentence}')
    input('\nPress enter when done: ')


def add_sentence() -> None:
    added_sentence = ask_question('\nWrite the sentence you want to add', True)
    with open_sentence_file('a') as f:
        f.write(f'{added_sentence}\n')
    print(f'Added "{added_sentence}"')


def main():
    load_sentences()
    while True:
        menu_choice = ask_question_with_answers('\n---Typing Speed Tester---\n1. List current sentences\n2. Add a sentence\n3. Begin test\nChoose an option', ['1.', '2.', '3.', '4.', '5.', '6.', '1', '2', '3', '4', '5', '6'], False)
        match menu_choice:
            case '1.' | '1':
                start_test()
            case '2.' | '2':
                list_sentences()
            case '3.' | '3':
                add_sentence()
            case '4.' | '4':
                remove_sentence()
            case '5.' | '5':
                reset_file()
            case '6.' | '6':
                return

if __name__ == '__main__':
    main()
