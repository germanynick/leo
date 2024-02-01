# Leo: A Voice Assistant

Leo is a voice assistant that can understand and respond to voice commands. It uses the `speech_recognition` library to convert speech to text and the `pyttsx3` library to convert text to speech.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installing

1. Clone the repository to your local machine:

```sh
git clone https://github.com/germanynick/leo
```

2. Navigate to the project directory:

```sh
cd leo
```

3. Install the required packages:

```sh
pip install --user pipenv
pipenv install
```

## Running the Application

To run the application, execute the [`main.py`](command:_github.copilot.openRelativePath?%5B%22main.py%22%5D "main.py") script:

```sh
python main.py
```

## Project Structure

The project is structured as follows:

- [`main.py`](command:_github.copilot.openRelativePath?%5B%22main.py%22%5D "main.py"): This is the entry point of the application. It calls the [`listen`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22listen%22%5D "main.py") function from the [`sensors`](command:_github.copilot.openRelativePath?%5B%22sensors%22%5D "sensors") module.
- [`sensors/`](command:_github.copilot.openRelativePath?%5B%22sensors%2F%22%5D "sensors/"): This module contains the [`listen`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22listen%22%5D "main.py") function which uses the `speech_recognition` library to convert speech to text.
- [`processors/`](command:_github.copilot.openRelativePath?%5B%22processors%2F%22%5D "processors/"): This module contains the [`process`](command:_github.copilot.openSymbolInFile?%5B%22processors%2F__init__.py%22%2C%22process%22%5D "processors/__init__.py") function which processes the text obtained from the [`listen`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22listen%22%5D "main.py") function.
- [`motors/`](command:_github.copilot.openRelativePath?%5B%22motors%2F%22%5D "motors/"): This module contains the [`speak`](command:_github.copilot.openSymbolInFile?%5B%22motors%2F__init__.py%22%2C%22speak%22%5D "motors/__init__.py") function which uses the [`pyttsx3`](command:_github.copilot.openSymbolInFile?%5B%22motors%2Fspeak.py%22%2C%22pyttsx3%22%5D "motors/speak.py") library to convert text to speech.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [`LICENSE`](command:_github.copilot.openRelativePath?%5B%22LICENSE%22%5D "LICENSE") file for details.

## Acknowledgments

- Python
- pyttsx3
- speech_recognition

## Contact

If you have any questions, feel free to contact us.
