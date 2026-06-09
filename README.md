# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Character Frequency Counter

This is a small Python program that reads a text file and counts how often each valid character appears.

The program ignores characters such as spaces and special characters. It only counts the characters that are allowed by the script.

## Requirements

You need to have Python 3 installed on your computer.

## Setup

After downloading the project files, create a folder in the same directory as `main.py`.

You can name the folder anything you want, but it is recommended to name it:

```bash
books
```

Place your book or text file inside that folder.

The file must be a `.txt` file. This program does not support PDF files yet.

## How to Run

Run the program from the terminal like this:

```bash
python3 main.py path/to/your/book.txt
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

The program will read the text file and show the frequency of each valid character.
