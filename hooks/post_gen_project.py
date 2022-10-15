from curses import ERR
import os

project_slug = "{{ cookiecutter.project_name }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{ERROR_COLOR}Let's do it! You are going to create something awesome!")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")
