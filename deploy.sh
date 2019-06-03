#!/bin/bash

npm run build
git push heroku master
heroku ps: scale web=1
