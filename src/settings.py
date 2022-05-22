########################
# -> Imports

from typing import Tuple

#########################
# -> Functions

# -> Functions : Commands { Settings } 

def launch() -> Tuple[str, str, str]:
    """
    > It asks the user to choose a language, then returns the name of the user, the language chosen and
      the prompt
    
    Returns:
      The name of the user, the language and the prompt.
    """
    # ~> Define Supported languages
    languages = ["en", "fr", "es"]
    language = ""
    # ~> languages Check
    while language not in languages:
        language = input("EN for English.\nFR pour Français.\nES para Español.\n$ ").lower()
        language = " ".join(language.split())
    return set_name(language), language, check_prompt(language)

def settings(name: str, language: str, prompt: str) -> Tuple[str, str, str]:
    """
    > It takes in a name, language, and prompt, and returns a tuple of the name, language, and prompt
    
    Args:
      name (str): The name of the user
      language (str): The language of the program.
      prompt (str): The prompt that the user sees when they are asked to enter a command.
    
    Returns:
      A tuple of the name, language, and prompt.
    """
    # ~> Set Prompt of language
    if language == "en":
        choice_prompt = "-> Enter number:\n 1: Change \"Name\".\n 2: Change \"Language\"\n 3: Change \"Prompt\"\n"
    elif language == "fr":
        choice_prompt = "-> Entrer un nombre\n 1: Modifier \"Nom\".\n 2: Modifier \"Langage\"\n 3: Modifier \"Message\"\n"
    elif language == "es":
        choice_prompt = "-> Ingresar número\n 1: Cambiar \"Nombre\".\n 2: Cambiar \"Idioma\"\n 3: Cambiar \"Mesaje\"\n"
    # ~> Define and adjust choice
    choice = 0
    while choice not in [1, 2, 3]:
        # No need to join since int()
        choice = int(input(choice_prompt + "$ "))
            # ~> Change Parameter of Choice
    if choice == 1:
        name = set_name(language)
    elif choice == 2:
        language = set_language()
    elif choice == 3:
        prompt = set_prompt(language)
    return name, language, check_prompt(language, prompt)

def set_name(language: str) -> str:
    """
    > It asks the user for their name, and returns it
    
    Args:
      language (str): The language of the program.
    
    Returns:
      A string.
    """
    # ~> Define Name's specific Prompt
    if language == "en":
        prompt = "What is your name ?"
    elif language == "fr":
        prompt = "Quel est votre nom ?"
    elif language == "es":
        prompt = "¿ Cómo Te Llama ?"
    # ~> Check Name
    name = ""
    while not name:
        name = input(prompt + "\n$ ")
    # ~> Adjust Name
    name = " ".join(name.split())
    return name.capitalize()

def set_language() -> str:
    """
    > This function asks the user to choose a language from a list of supported languages
    
    Returns:
      The language that the user has chosen.
    """
    # ~> Define Supported languages
    languages = ["en", "fr", "es"]
    language = ""
    # ~> languages Check
    while language not in languages:
        language = input("EN for English.\nFR pour Français.\nES para Español.\n$ ").lower()
        language = " ".join(language.split())
    return language

def set_prompt(language: str) -> str:
    """
    > Define a specific Prompt and returns it
    
    Args:
      language (str): The language of the program.
    
    Returns:
      A string
    """
    # ~> Define Name's specific Prompt
    if language == "en":
        prompt = "Enter your custom Prompt ?"
    elif language == "fr":
        prompt = "Quel est votre Message personalisé ?"
    elif language == "es":
        prompt = "¿ Ingrese su mensaje personalizado ?"
    # ~> Check Name
    custom_prompt = ""
    while not custom_prompt:
        custom_prompt = input(prompt + "\n$ ")
    # ~> Adjust Name
    custom_prompt = " ".join(custom_prompt.split()) + " "
    return custom_prompt

def check_prompt(language: str, prompt: str = None) -> str:
    """
    > The function checks if the prompt is valid, and if not, it returns a default prompt
    
    Args:
      language (str): The language you want to use.
      prompt (str): The prompt to be displayed to the user.
    
    Returns:
      A string.
    """
    if prompt == None:
        # ~> Define Prompt
        if language == "en":
            prompt = "Hello, "
        elif language == "fr":
            prompt = "Bonjour, "
        elif language == "es":
            prompt = "Hola, "
        return prompt
    else:
        # ~> Check Custom Prompt
        if prompt not in ["Hello, ", "Bonjour, ", "Hola, "]:
            return prompt
        else:
            # ~> Return Default Prompt of Language
            return check_prompt(language)