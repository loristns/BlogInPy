import json
import engine
import sys


def run_ui():

    # Get config data
    config = open("config.json")
    config_data = json.loads(config.read())
    config.close()

    print("""
          ____  _             _____       _____
         |  _ \| |           |_   _|     |  __ |
         | |_) | | ___   __ _  | |  _ __ | |__) |   _
         |  _ <| |/ _ \ / _` | | | | '_ \|  ___| | | |
         | |_) | | (_) | (_| |_| |_| | | | |   | |_| |
         |____/|_|\___/ \__, |_____|_| |_|_|    \__, |
                         __/ |                   __/ |
                        |___/                   |___/

        -- Welcome to the smallest blog generator ever --

        INFO - Article list :
        """)

    for article in config_data["index"]:  # Print each article in index
        print("         - %s" % article)

    while True:  # Print the menu
        print("\n    ACTION - What do you want to do ?\n")
        print("         1- Add article to index")
        print("         2- Delete article to index")
        print("         3- Generate the blog")
        print("         4- Quit\n")

        action = input("    YOU >>> ")

        if action == "1":  # Add article
            filename = input("  Name of article file : ")
            print(engine.add_article(filename))

        elif action == "2":  # Delete article
            filename = input("  Name of article file : ")
            print(engine.delete_article(filename))

        elif action == "3":  # Generate blog
            print("Generating blog...")
            engine.generate_blog()
            print("Blog successfully generated !")

        elif action == "4":  # Exit
            print("Bye Bye")
            exit()

        else:
            print("Unrecognized command...")

if __name__ == '__main__':

    try:

        if sys.argv[-2] == "-index+":  # Add a command for adding file to index
            print(engine.add_article(sys.argv[-1]))

        elif sys.argv[-2] == "-index-":
            print(engine.delete_article(sys.argv[-1]))

        elif sys.argv[-1] == "-gen":
            print("Generating blog...")
            engine.generate_blog()
            print("Blog successfully generated !")

        elif sys.argv[-1] == "-ui":
            run_ui()

        else:
            print("Unrecognized command...")

    except IndexError:
        run_ui()
