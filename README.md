# duq_ds3_2024

## Setting up VSCode (Microsoft Visual Studio Code) for your whole computer for the first time

The first rule of VSCode: _only open the folder of the project_, not a folder including multiple projects. You want to open the outermost folder of a single project, which should contain git information for your project (a hidden .git directory).

I organize my directories as follows:

```
programming
└─── duq_ds3_2024
│   │    .gitignore
│   │    README.md
│   └─── .vscode
│       │    launch.json
│       │    settings.json
│
│   └─── duq_ds3_2024
│       │    __init__.py
│       │    some_class.py
│
│   └─── scripts
│       │    some_script.py
│
└─── duq_ds3_2023
│   │    .gitignore
│   │    README.md
```

In VSCode, do NOT open `programming`. Instead, you should have a separate window for `duq_ds3_2024` and any other project, such as `duq_ds3_2023`.

The new hip alternative to `pip` is called `poetry`. I would install it now, using

```
curl -sSL https://install.python-poetry.org | python3 -
```

see https://python-poetry.org/docs/#installing-with-the-official-installer for Windows installation.

## Setting up a git project (once)

The easiest way is to first set up the project in `git` and then clone it to your computer.

1. In github, create a new repository and name it
1. Once, you will have to add your SSH keys
1. Click on the green button called "Code", select "SSH", and copy the resulting code.
1. Clone the repository to your computer. I'm going to navigate to the right place in the terminal first and then clone. This will create a new folder in programming with the name `duq_ds3_2024` in which the project will live.

```
cd /Users/arthur/programming
git clone git@github.com:asugden/duq_ds3_2024.git duq_ds3_2024/
```

5. Now you're ready to open it in vscode.

## Setup VSCode for project (once)

In VSCode, open the directory for ONLY A SINGLE PROJECT. I cannot stress this enough. Anything else will cause problems with git and environments.

1. Create a `.vscode` directory and copy in the `launch.json` and `settings.json` files included here.
1. Copy in the `.gitignore` file to ensure random junk is not uploaded to git.
1. Open the VSCode terminal (you can create a New Terminal in the top menu or just click the circle with an X button at the bottom). Type `poetry init`. This will create a new virtual environment.
1. You can add new packages with `poetry add pandas` for example. And run `poetry install` to make sure everything is up to date.
1. Change the path in `settings.json` to match your computer. You can keep everything from `.venv/bin/activate` but you will have to change the first part of the line to be the location of the directory on your computer.
1. As you go, you can continue to add packages with `poetry add` and `poetry install`.
