# Random dog

This project will help you download several photos of random dogs.

You can specify the end point for saving, as well as the required number of pictures.

## Installation
Before installation, make sure you have [Python](https://www.python.org/) 3.x installed

To work with a project, you need to install or clone it.

Use the following command in terminal to clone:

```bash
git clone https://github.com/abfalex/random-dog
```

Next, you need to create a virtual environment for easy use (recommended):

   ```bash
   python -m venv <venv_name>
   ```

After installing the virtual environment, you need to activate it:

  - On Windows:

     ```bash
     <venv_name>\Scripts\activate
     ```

- On macOS and Linux:

     ```bash
     source <venv_name>/bin/activate
     ```

After, you need to install the necessary library. Enter this command into the terminal:

```bash
pip install -r requirements.txt
```

## Launch
To run, you need to enter the following command into the terminal:

```bash
python main.py
```

After this, 50 files will begin downloading to the standard “dogs” folder

To specify your folder and a certain number of photos, you must use arguments.

## Arguments

The arguments are written at the end of the command that starts the download process.

- `--folder` or `-f` specify the folder in which the downloaded pictures will be saved

- `--count` or `-c` specify the number of random dog pictures that will be downloaded

Examples:

With a folder:

```bash
python main.py -f dogs_pictures
```

The final result: a folder "dogs_pictures" with 50 pictures of random dogs

With a count:

```bash
python main.py -c 20
```

The final result: a folder "dogs" with 20 images of random dogs

Arguments can also be grouped:

```bash
python main.py -f dogs_pictures -c 40
```