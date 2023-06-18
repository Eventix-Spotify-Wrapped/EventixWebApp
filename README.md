# Eventix Summary Application

## How to setup this project?

Clone this repository locally.
To be able to run the django project you first must install python: https://www.python.org/

And after that you need to make sure you have the Node Package Manager installed: https://www.npmjs.com/

Open the project in a code editor and navigate with the terminal to the folder named "EventixPrj"

In this folder we are going to create a virtual environment where we install packages that we need to run the project.
You can create your own envoiremnt using the command:

```
    python3 -m venv env
```

Once you created your own envoirment you need to install all the needed packages in this environment. To do this we will first activate this envoirment. We will do this with the following command:

```
    source env/bin/activate
```

Now we can install all packages that are needed. You can find the needed packages in the requirements.txt. We just say to the python pipeline to install all the packages in that file.

```
    pip3 install -r requirements.txt
```
After all the requirements are installed we just need to run the server that starts the application. We can do this by entering the following in the terminal:

```
    python3 manage.py runserver
```

Now you will see the startup screen of django in your webbrowser. Instead of this page navigate to the event summary (or dashboard) by adding one of those lines to the url:

* /panel
* /sprint2demo

Now that django is installed we also need to install node.js because we use a package named "Laravel-Mix" which compiles all sass and javascript files to minified versions that can be read by internet browsers. Note that you need to be at the root of the directory with the terminal again.

```
    npm install
```

After that you need to run the comment below to start watching all files and start compiling them when changes are applied. You need to run this comment every time you want to change the css and/or js-files in the repository.

```
    npx mix watch
```

Instead of using both the commands: ```npx mix watch``` & ```python3 manage.py runserver``` you can also run the command:

```
    npm run dev
```

This will execute both the commands in one terminal window. Do this each time you want to run the server/adjust the resource files.