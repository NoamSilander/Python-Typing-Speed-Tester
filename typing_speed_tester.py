import time
from pathlib import Path

SENTENCE_FILE = Path('sentences.txt')

def open_sentence_file(mode: str):
    with open(SENTENCE_FILE, 'mode', encoding='utf-8') as f:
        pass

def file_init():
    try:
        with open(SENTENCE_FILE, encoding='utf-8') as f:
            sentences = f.read()
        print(sentences)
    except FileNotFoundError:
        print('Sentence file ')
        #with open()



def ask_question(question: str) -> str:
    while True:
        answer = input(f'{question}: ').lower().strip()
        if not answer:
            print('Must not be empty')
            continue
        return answer

def ask_question_with_answers(question: str, answers: list) -> str:
    while True:
        answer = ask_question(question)
        if answer not in answers:
            print('Not a valid option')
            continue
        return answer




def sentence_checker():
    sentence = input('What sentence would you like to add to the sentence list?: ').lower().strip().split()
    print(sentence)

def main():
    sentence_list = ['the quick brown fox jumps over the lazy dog', 'the five boxing wizards jump quickly', 'sphinx of black quartz judge my vow']
    menu_choice = ask_question_with_answers('---Typing Speed Tester\nWhat would you like to do?:\n1. List current sentences\n2. Add a sentence\n3. Begin test\nChoose an option', ['1.', '2.', '3.', '1', '2', '3'])
    match menu_choice:
        case '1.' | '1':
            list_sentences()
        case '2.' | '2':
            add_sentence()
        case '3.' | '3':
            test_init()

if __name__ == '__main__':
    main()
