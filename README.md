# Github Issue Tracker

A basic project based on React and Django stack to track open issues in Github repositories using the Github GraphQL API. The project is hosted at https://vgithub.herokuapp.com/

# Instructions to setup locally

The project uses this token to make queries to Github GrapQL API. Follow the instructions [here](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) to get your Github token. Set environment variable GITHUB_TOKEN as this token.

```sh
$ export GITHUB_TOKEN="YourApiToken"
```

This project is based on React and Django. So make sure you have the necessory tools installed for these frameworks like node, npm, pip3, pipenv, etc. Check out their docs for more info.

Clone this repository and run the following commands:

```sh
$ git clone https://github.com/vibhavsarraf/django-github
$ cd django-github
$ npm install
$ pipenv install
```
After this you need to compile react files using the following command:
```sh
$ npm run dev
```

This command runs in watch mode so it will notice any changes in the react files and recompile. For now you can quit this process once it has compiled the files to main.js.
Next run the django server in the pipenv shell. Make sure you are using python 3.7 version.

```sh
$ pipenv shell
$ cd issues_project
$ python manage.py runserver
```

Go to http://localhost:8000 and you should see your server running.