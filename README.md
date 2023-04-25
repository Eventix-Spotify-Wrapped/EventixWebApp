# Eventix Summary Application

## How to setup this project?

Clone this repository locally.
To be able to run the django project you first must install python: https://www.python.org/

Open the project in a code editor and navigate with the terminal to the folder named "EventixPrj"

In this folder we are going to create a virtual environment where we install packages that we need to run the project.
You can create your own envoiremnt using the command:

```
    python3 -m venv env
```

Once you created your own envoirment you need to install all the needed packages in this environment. To do this we will first activate this envoirment. We will do this with the following command:

```
    source /env/bin/activate
```

Now we can install all packages that are needed. You can find the needed packages in the requirements.txt. We just say to the python pipeline to install all the packages in that file.

```
    pip3 install -r requirements.txt
```