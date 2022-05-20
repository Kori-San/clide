#!/bin/python3

# -> Functions

# -> Functions : Settings
def hello_prompt(lang: str) -> str:
    # ~> Define Prompt
    if lang == "en":
        prompt = "Hello, "
    elif lang == "fr":
        prompt = "Bonjour, "
    elif lang == "es":
        prompt = "Hola, "
    return prompt

def init() -> str:
    # ~> Define Supported Langages
    langages = ["en", "fr", "es"]
    lang = ""
    # ~> Langages Check
    while lang not in langages:
        lang = input("EN for English.\nFR pour Français.\nES para Español.\n$ ").lower()
        lang = " ".join(lang.split())
    return lang, hello_prompt(lang), set_name(lang)

# -> Functions : Commands { Miscellaneous }

def error(lang: str) -> None:
    if lang == "en":
        print("/!\ Error:", '"' + cmd + '"', "is not a valid command. Please check \"help\".")
    elif lang == "fr":
        print("/!\ Erreur:", '"' + cmd + '"', "n'est pas une commande valide. Utilisez \"help\".")
    elif lang == "es":
        print("/!\ Error:", '"' + cmd + '"', "no es un comando válido. Por favor, marque \"help\".")

def init_settings(lang: str) -> None:
    # ~> Set Prompt of Langage
    if lang == "en":
        prompt = "-> Enter number:\n 1: Change \"Name\".\n 2: Change \"Langage\"\n 3: Change \"Prompt\"\n"
    elif lang == "fr":
        prompt = "-> Entrer un nombre\n 1: Modifier \"Nom\".\n 2: Modifier \"Language\"\n 3: Modifier \"Message\"\n"
    elif lang == "es":
        prompt = "-> Ingresar número\n 1: Cambiar \"Nombre\".\n 2: Cambiar \"Idioma\"\n 3: Cambiar \"Mesaje\"\n"
    # ~> Define and adjust choice
    choice = 0
    while choice not in [1, 2, 3]:
        # No need to join since int()
        choice = int(input(prompt + "$ "))
    return choice

def set_name(lang: str) -> str:
    # ~> Define Name's specific Prompt
    if lang == "en":
        prompt = "What is your name ?"
    elif lang == "fr":
        prompt = "Quel est votre nom ?"
    elif lang == "es":
        prompt = "¿ Cómo Te Llama ?"
    # ~> Check Name
    name = ""
    while not name:
        name = input(prompt + "\n$ ")
    # ~> Adjust Name
    name = " ".join(name.split())
    return name.capitalize()

def set_lang() -> str:
    # ~> Define Supported Langages
    langages = ["en", "fr", "es"]
    lang = ""
    # ~> Langages Check
    while lang not in langages:
        lang = input("EN for English.\nFR pour Français.\nES para Español.\n$ ").lower()
        lang = " ".join(lang.split())
    return lang

def set_prompt(lang: str) -> str:
    # ~> Define Name's specific Prompt
    if lang == "en":
        prompt = "Enter your custom Prompt ?"
    elif lang == "fr":
        prompt = "Quel est votre Message personalisé ?"
    elif lang == "es":
        prompt = "¿ Ingrese su mensaje personalizado ?"
    # ~> Check Name
    custom_prompt = ""
    while not custom_prompt:
        custom_prompt = input(prompt + "\n$ ")
    # ~> Adjust Name
    custom_prompt = " ".join(custom_prompt.split()) + " "
    return custom_prompt

def help(lang: str) -> None:
    # ~> Define Delimiter
    delim = " ~ "
    # ~> Print Help of Langage
    if lang == "en":
        help_en(delim)
    elif lang == "fr":
        help_fr(delim)
    elif lang == "es":
        help_es(delim)
    return

def help_en(delim: str) -> None:
    print("-> Commands:")
    print(delim + "quit  : Say goodbye and quit")
    print(delim + "help  : Display all avaible commands with description")
    print(delim + "hello : Say Hello")
    return

def help_fr(delim: str) -> None:
    print("-> Commandes:")
    print(delim + "quit  : Dis au revoir et quitte")
    print(delim + "help  : Affiche les commandes disponibles avec une description")
    print(delim + "hello : Dis Bonjour")
    return

def help_es(delim: str) -> None:
    print("-> Comandos:")
    print(delim + "quit  : Dice hasta luego y dejar")
    print(delim + "help  : Mostrar todos los comandos disponibles con descripción")
    print(delim + "hello : Dice Hola")
    return

# -> Functions : Commands { Utilities }

def hello(prompt: str, name: str) -> None:
    # ~> Simple Print
    print(prompt + name + " !")
    return

def bye(lang: str, name: str) -> None:
    # ~> Set Prompt of Langage
    if lang == "en":
        prompt = "See you soon"
    elif lang == "fr":
        prompt = "À plus tard"
    elif lang == "es":
        prompt = "Hasta luego"
    # ~> Simple Print
    print(prompt, name +  " !")
    return

#########################
# -> Main

# -> Main : Settings Vars
lang, prompt, name = init()

# -> Main : Main Loop
while True:
    # ~> Set and adjust current cmd
    cmd = input(prompt + name + ": $ ")
    cmd = " ".join(cmd.split())
    # ~> Check cmd
    if cmd == "quit":
        bye(lang, name)
        break
    elif cmd == "help":
        help(lang)
    elif cmd == "hello":
        hello(prompt, name)
    elif cmd == "settings":
        # ~> Define Choice
        choice = init_settings(lang)
        # ~> Change Parameter of Choice
        if choice == 1:
            name = set_name(lang)
        elif choice == 2:
            lang = set_lang()
        elif choice == 3:
            prompt = set_prompt(lang)          
    else:
        error(lang)
