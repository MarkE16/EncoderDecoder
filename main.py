import os
from time import sleep
from colorama import init, Fore
import colorama
from pyperclip import copy
# Import the necessary modules from PyQt5 to create a simple window.
# from PyQt5 import QtWidgets, QtCore, QtGui

# class Window(QtWidgets.QWidget):
#   def __init__(self):
#     super().__init__()
#     self.initUI()
#     self.showWindow()

#   def initUI(self):
#     self.setFixedSize(500, 500)
#     self.setWindowTitle('Encoder-Decoder')

#     self.layout = QtWidgets.QGridLayout(self)

#     self.label = QtWidgets.QLabel(self)
#     self.label.setText('Encoder / Decoder')
#     self.label.setAlignment(QtCore.Qt.AlignCenter)
#     self.label.setStyleSheet('font-size: 20px;')

#     self.label2 = QtWidgets.QLabel(self)
#     self.label2.setText('Enter text to encode or decode:')
#     self.label2.setAlignment(QtCore.Qt.AlignCenter)
#     self.label2.setStyleSheet('font-size: 15px;')

#     self.text = QtWidgets.QLineEdit(self)
#     self.text.setAlignment(QtCore.Qt.AlignCenter)
#     self.text.placeholderText = "Your Text"

#     self.button = QtWidgets.QPushButton(self)
#     self.button.setText('Encode / Decode')
#     # self.button.clicked.connect(self.encode)

#     # Radio Buttons
#     self.radio = QtWidgets.QButtonGroup(self)
#     self.radio.setExclusive(True)
#     # self.radio.buttonClicked.connect(self.encode)
#     self.radio.addButton(self.button, 1)
#     self.radio.addButton(self.button, 2)
#     self.radio.addButton(self.button, 3)




#     self.layout.addWidget(self.label, 0, 0, 1, 2)
#     self.layout.addWidget(self.label2, 1, 0, 1, 2)
#     self.layout.addWidget(self.text, 2, 0, 1, 2)
#     self.layout.addWidget(self.button, 2, 0, 2, 2)
#     # self.layout.addWidget(self.radio, 2, 0, 2, 2)
  
#     self.setLayout(self.layout)
#   def showWindow(self):
#     self.show()



clearCMD = lambda: os.system("cls")
colorama.init(autoreset=True)
version = "v1.0.3"

def fetchLatestRelease():
  try:
    import requests
    import json
    response = requests.get("https://api.github.com/repos/MarkE16/EncoderDecoder/releases")
    data = json.loads(response.text)
    return data[0]["tag_name"]
  except Exception as e:
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] An error occurred while fetching the latest release.")
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] Error: {Fore.LIGHTYELLOW_EX}{e}{Fore.RESET}")

def checkUpdates():
  print_header("Checking for updates...")
  sleep(1.5)
  latest = fetchLatestRelease()
  if not isinstance(latest, str):
    input(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] An error occurred while fetching the latest release.")
  if latest != version:
    print(f"[{Fore.LIGHTYELLOW_EX}Update{Fore.RESET}] There is an update available for the Encoder-Decoder project.")
    print(f"[{Fore.LIGHTYELLOW_EX}Update{Fore.RESET}] The latest release is {Fore.LIGHTYELLOW_EX}{latest}{Fore.RESET}.")
    print(f"[{Fore.LIGHTYELLOW_EX}Update{Fore.RESET}] You are currently on {Fore.LIGHTYELLOW_EX}{version}{Fore.RESET}.")
    print(f"[{Fore.LIGHTYELLOW_EX}Update{Fore.RESET}] Get the latest version at {Fore.LIGHTYELLOW_EX}https://www.github.com/MarkE16/EncoderDecoder{Fore.RESET}.")
    input(f"[{Fore.LIGHTYELLOW_EX}Update{Fore.RESET}] Press enter to continue...")
  else:
    print(f"[{Fore.LIGHTGREEN_EX}Update{Fore.RESET}] You are up-to-date.")
    input(f"[{Fore.LIGHTGREEN_EX}Update{Fore.RESET}] Press enter to continue...")

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
      print(f"[{Fore.LIGHTGREEN_EX}Success{Fore.RESET}] Encoded Text: {Fore.LIGHTYELLOW_EX}{encodeString(text)}{Fore.RESET}")
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
      print(f"[{Fore.LIGHTGREEN_EX}Success{Fore.RESET}] Decoded Text: {Fore.LIGHTYELLOW_EX}{decodeString(text)}{Fore.RESET}")
    except UnicodeDecodeError as err:
      print(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] There was a problem decoding your string => {err}.")
    copy_to_board = input("Press ENTER to continue. Input 'C' to copy the result to clipboard. ")
    if copy_to_board.upper() == "C":
      copy(decoded)
      input(f"[{Fore.LIGHTGREEN_EX}COPIED{Fore.RESET}] The result has been copied to your clipboard.")

loading = True

def main():

  # app = QtWidgets.QApplication([])
  # window = Window()
  # window.show()
  # app.exec_()

  # def loadingScreen(func) -> None:
  #   global loading
  #   load = ["|", "/", "-", "\\"]
  #   a = 0
  #   while loading:
  #     for i in load:
  #       print(f"{Fore.LIGHTBLUE_EX}[{i}]{Fore.RESET} Processing...", end="\r")
  #       sleep(0.5)
  #     func()

  # @loadingScreen
  # def some_func():
  #   global loading
  #   print("Hello")
  #   sleep(5)
  #   loading = False
  #   return 1
  while True:
    clearCMD()
    # loadingScreen(loading)
    # some_func()
    print_header("Encoder-Decoder")
    print_description("This is a simple program that allows you to encode text and decode encoded text. Let's get started.")
    print()
    print(
      "[A] OR [1] - Encode text\n"
      "[B] OR [2] - Decode text\n"
      "[C] OR [3] - Check For Updates\n"
      "[X] OR [4] - Exit\n"
    )
    print(f"=> Encoder Decoder | Copyright © 2022 Mark E | {version}")
    choice = input("Enter your choice: ")
    choice = take_input(choice, "int" if choice.isdigit() else "str")
    clearCMD()
    if choice == 1 or choice == "A":
      encodeSection()
      clearCMD()
    elif choice == 2 or choice == "B":
      decodeSection()
      clearCMD()
    elif choice == 3 or choice == "C":
      clearCMD()
      checkUpdates()
    elif choice == 4 or choice == "X":
      break


if __name__ == '__main__':
  main()