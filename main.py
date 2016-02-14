import json
import function

# Get config data
config = open("config.json")
config_data = json.loads(config.read())
config.close()

# Get template


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

for article in config_data["index"]: # print each article
    print("         - %s" %article)

while True:
    print("\n    ACTION - What do you want to do ?\n")
    print("         1- Add article to index")
    print("         2- Delete article to index")
    print("         3- Generate the blog")
    print("         4- Quit\n")

    action = input("    YOU >>> ")

    if action == "1":
        filename = input("  Name of article file : ")
        print(function.add_article(filename))

    elif action == "2":
        filename = input("  Name of article file : ")
        print(function.delete_article(filename))

    elif action == "3":
        print("Generating blog...")
        function.generate_blog()
        print("Blog successfully generated !")

    elif action == "4":
        print("Bye Bye")
        exit()

    else:
        print("Unrecognized command...")

