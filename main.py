import os
from time import sleep
from colorama import init, Fore
import colorama
from pyperclip import copy

clearCMD = lambda: os.system("cls")
colorama.init(autoreset=True)

def print_header(txt: str) -> None:
  print("=" * len(txt))
  print(txt)
  print("=" * len(txt))

def print_description(txt: str) -> None:
  print("| " + txt)

def take_input(input, endResult="str") -> int | str:
  """
  A function that takes input and returns the data type of the input you want.
  Returns 0 if the given input is not a number when attempting to convert it to an integer or invalid endResult was given.
  :param input: The input to take.
  :param endResult: The data type you want the input to be.
  :return: The input as the data type you want.
  """
  if endResult == "int":
    try:
      return int(input)
    except ValueError:
      return 0
  elif endResult == "str":
    return str(input).upper()
  return 0

def encodeString(text: str) -> str:
  """
  A function that encodes a given string.
  :param text: The text to encode.
  :return: The encoded text.
  """
  return text.encode("ascii").hex()

def decodeString(text: str) -> str:
  """
  A function that decodes a given string.
  :param text: The text to decode.
  :return: The decoded text.
  """
  return bytes.fromhex(text).decode('ascii')

def encodeSection():
  print_header("ENCODING")
  print_description("Enter the text you want to encode into ASCII.")
  text = str(input("Text: "))
  confirm = input(f"You're about to encode '{text}'. Continue? [Y/N] ")
  if confirm.upper() == "Y":
    clearCMD()
    print("> GIVEN TEXT: " + text)
    sleep(1.5)
    print("> Encoding...")
    try:
      encoded = encodeString(text)
      print(f"[{Fore.LIGHTGREEN_EX}Sucess{Fore.RESET}] Encoded Text: {Fore.LIGHTYELLOW_EX}{encodeString(text)}{Fore.RESET}")
    except UnicodeEncodeError as err:
      print(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] There was a problem encoding your string => {err}.")
    copy_to_board = input("Press ENTER to continue. Input 'C' to copy the result to clipboard. ")
    if copy_to_board.upper() == "C":
      copy(encoded)
      input(f"[{Fore.LIGHTGREEN_EX}COPIED{Fore.RESET}] The result has been copied to your clipboard.")

def decodeSection():
  print_header("DECODING")
  print_description("Enter the text you want to decode from ASCII.")
  text = str(input("Text: "))
  # Check if the text is not a valid hex string or ASCII.
  if not text.isalnum() or not text.isascii():
    input(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] Invalid text.")
    return
  confirm = input(f"You're about to decode '{text}'. Continue? [Y/N] ")
  if confirm.upper() == "Y":
    clearCMD()
    print("> GIVEN TEXT: " + text)
    sleep(1.5)
    print("> Decoding...")
    try:
      decoded = decodeString(text)
      print(f"[{Fore.LIGHTGREEN_EX}Sucess{Fore.RESET}] Decoded Text: {Fore.LIGHTYELLOW_EX}{decodeString(text)}{Fore.RESET}")
    except UnicodeDecodeError as err:
      print(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] There was a problem decoding your string => {err}.")
    copy_to_board = input("Press ENTER to continue. Input 'C' to copy the result to clipboard. ")
    if copy_to_board.upper() == "C":
      copy(decoded)
      input(f"[{Fore.LIGHTGREEN_EX}COPIED{Fore.RESET}] The result has been copied to your clipboard.")
def main():
  while True:
    print_header("Encoder-Decoder")
    print_description("This is a simple program that allows you to encode text and decode encoded text. Let's get started.")
    print()
    print(
      "[A] OR [1] - Encode text\n"
      "[B] OR [2] - Decode text\n"
      "[X] OR [3] - Exit"
    )
    choice = input("Enter your choice: ")
    choice = take_input(choice, "int" if choice.isdigit() else "str")
    clearCMD()
    if choice == 1 or choice == "A":
      encodeSection()
      clearCMD()
    elif choice == 2 or choice == "B":
      decodeSection()
      clearCMD()
    elif choice == 3 or choice == "X":
      break


if __name__ == '__main__':
  main()