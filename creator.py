import os
from textwrap import dedent
from time import sleep

from scaffold import Scaffold

if __name__ == "__main__":
    name = input("Source name: ")
    lang = input("Source language: ")
    baseUrl = input("Base URL: ")
    is_parsed = None

    while is_parsed is None:
        response = input(
            dedent(
                """
        Choose the source type:
            1. AnimeHttpSource / API/JSON oriented
            2. ParsedAnimeHttpSource / JSoup/CSS oriented

        Enter your choice: """
            )
        )
        print()

        if not response.isnumeric():
            print("Invalid choice: Enter numbers only!")
        else:
            choice = int(response)
            if choice in (1, 2):
                is_parsed = choice == 2
                break
            else:
                print("Invalid choice! Please select 1 or 2.")

        sleep(1)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    scaffold = Scaffold(is_parsed, name, lang, baseUrl)
    scaffold.create_dirs()
    scaffold.create_files()
