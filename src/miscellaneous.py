########################
# -> Imports

#########################
# -> Functions

# -> Functions : Commands { Miscellaneous }

def error(language: str, cmd: str) -> None:
    """
    > It prints an error message if the command is not valid
    
    Args:
      language (str): The language of the error message.
    
    Returns:
      None
    """
    if language == "en":
        print("/!\ Error:", '"' + cmd + '"', "is not a valid command. Please check \"help\".")
    elif language == "fr":
        print("/!\ Erreur:", '"' + cmd + '"', "n'est pas une commande valide. Utilisez \"help\".")
    elif language == "es":
        print("/!\ Error:", '"' + cmd + '"', "no es un comando válido. Por favor, marque \"help\".")
    return

def help(language: str) -> None:
    """
    > `help` takes a string as an argument and prints the help of the language specified in the string
    
    Args:
      language (str): The language of the help message.
    
    Returns:
      None
    """
    # ~> Define Delimiter
    delimiter = " ~ "
    # ~> Print Help of language
    if language == "en":
        help_english(delimiter)
    elif language == "fr":
        help_french(delimiter)
    elif language == "es":
        help_spanish(delimiter)
    return

def help_english(delimiter: str) -> None:
    """
    > It prints a list of commands and their descriptions
    
    Args:
      delimiter (str): str
    
    Returns:
      None
    """
    print("-> Commands:")
    print(delimiter + "quit / exit : Say goodbye and quit")
    print(delimiter + "help        : Display all avaible commands with description")
    print(delimiter + "hello       : Say Hello")
    print(delimiter + "settings    : Allows you to change your settings (name, language and prompt)")
    return

def help_french(delimiter: str) -> None:
    """
    > It prints a list of commands and their descriptions
    
    Args:
      delimiter (str): str
    
    Returns:
      None
    """
    print("-> Commandes:")
    print(delimiter + "quit / exit : Dis au revoir et quitte")
    print(delimiter + "help        : Affiche les commandes disponibles avec une description")
    print(delimiter + "hello       : Dis Bonjour")
    print(delimiter + "settings    : Permet de changer les paramétres (nom, langue et message)")

    return

def help_spanish(delimiter: str) -> None:
    """
    > It prints a list of commands and their descriptions
    
    Args:
      delimiter (str): str
    
    Returns:
      None
    """
    print("-> Comandos:")
    print(delimiter + "quit / exit : Dice hasta luego y dejar")
    print(delimiter + "help        : Mostrar todos los comandos disponibles con descripción")
    print(delimiter + "hello       : Dice Hola")
    print(delimiter + "settings    : Le permite cambiar su configuración (nombre, idioma y mesaje)")
    return