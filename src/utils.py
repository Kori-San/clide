########################
# -> Imports

#########################
# -> Functions

# -> Functions : Commands { Utilities }

def hello(prompt: str, name: str) -> None:
    """
    > `hello` is a function that takes in a string and a name, and prints out a greeting
    
    Args:
      prompt (str): str
      name (str): str
    
    Returns:
      None
    """
    # ~> Simple Print
    print(prompt + name + " !")
    return

def bye(language: str, name: str) -> None:
    """
    > This function takes a language and a name as input and prints a goodbye message in the given
      language
    
    Args:
      language (str): str
      name (str): str
    
    Returns:
      None
    """
    # ~> Set Prompt of language
    if language == "en":
        prompt = "See you soon"
    elif language == "fr":
        prompt = "À plus tard"
    elif language == "es":
        prompt = "Hasta luego"
    # ~> Simple Print
    print(prompt, name +  " !")
    return

def info(name: str, language: str, prompt: str) -> None:
    """
    > It prints out the name, language, and prompt of the user
    
    Args:
      name (str): str
      language (str): The language of the prompt.
      prompt (str): The prompt that the user will see.
    
    Returns:
      None
    """
    delimiter = " ~> "
    if language == "en":
        info_name = "Name :"
        info_language = "Language :"
        info_prompt = "Prompt :"
    elif language == "fr":
        info_name = "Nom :"
        info_language = "Langue :"
        info_prompt = "Message :"
    elif language == "es":
        info_name = "Nombre :"
        info_language = "Idioma :"
        info_prompt = "Mesaje :"
    print(delimiter + info_name,'\"' + name + '\"')
    print(delimiter + info_language, '\"' + language.upper() + '\"')
    print(delimiter + info_prompt, '\"' + prompt + '\"')
    return