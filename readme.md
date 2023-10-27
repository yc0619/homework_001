# homework

this project aims to inference client credit card's type by analysing user data by application.

## installation

if you want to run the script on windows. suppose you has just bought this pc for 2 sec. and on your windows there is no python.

### first of the first step: install python & create venv

the tutorial are for poor sad windows beginners.

1. **download python for vscodecheck** `https://www.python.org/downloads/windows/` the url and download the newest python
2. ****open your vs-code `ctrl + shift + x` goto extension in vs-code. search for `python` and install it.
3. let's create venv! (since others may recommand `miniconda` but i think they are the same `venv` seems to be more popular in the production for me)
    - without terminal `ctrl + shift + p` and in the search bar input `python` and choose `python: create environment` then click `Venv` then click create!
    - with terminal: it will be cooler. go to menu -> new terminal open the terminal in vs code.
        - **install python in microsoft scrore**: input `python` run with `enter` (you will go to microsoft store i have restart the vs code
        - input `python` you will then go to terminal version python. don't panic just input `exit()`
        - then you're back. run `python -m venv .venv`. actually you can run `python -m venv .your_customized_venv_name` the `.` means your **v**(-irtual)**env**(-ironment) the `.` point before your customized name means: it is and should be hidden folder. but any other customized fancy name is not very recommanded. but still, you can taste the pain by yourself later when you has more projects. **just name it `.venv`**
4. if you succeeded you will find `.venv` folder under your project folder. (in vs-code don't open the file, open the folder instead)
5. THE MOST IMPORTANT: DON'T FORGET OPEN WINDOWS SEARCH POWERSHELL RUN AS ADMINISTATOR `Set-ExecutionPolicy RemoteSigned` AND INPUT `A`
6. in terminal `.venv\Scripts\activate`
