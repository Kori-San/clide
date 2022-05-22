#!/bin/python3

########################
# -> Imports

import src.settings as settings
import src.miscellaneous as misc
import src.utils as utils

#########################
# -> Main

# -> Main : Settings Vars
# ~> Unpacking the tuple returned by the function `launch()` into three variables: `name`,
#    `language`, and `prompt`.
name, language, prompt = settings.launch()

# -> Main : Main Loop
# ~> The main loop of the program. It asks the user for a command, and then executes the
#    command.
while True:
    # ~> Set and adjust current cmd
    cmd = input(prompt + name + ": $ ")
    cmd = " ".join(cmd.split())
    # ~> Check cmd
    if cmd in ["quit", "exit"]:
        utils.bye(language, name)
        break
    elif cmd == "help":
        misc.help(language)
    elif cmd == "hello":
        utils.hello(prompt, name)
    elif cmd == "settings":
        name, language, prompt = settings.settings(name, language, prompt)
    elif cmd == "info":
        utils.info(name, language, prompt)
    else:
        misc.error(language, cmd)