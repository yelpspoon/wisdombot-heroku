# wisdombot-heroku
Running JayBo's Wisdom Bot on Heroku


## To get the new files and layout
 - git clone https://github.com/yelpspoon/wisdombot-heroku.git

## Steps
 - brew install heroku/brew/heroku
 - heroku apps:create wisdombot-app
 - heroku buildpacks:set heroku/python
 - heroku stack:set heroku-18
 - git add .
 - git commit -m "Maybe Profile is needed?"
 - git push heroku master
 - heroku logs --tail
 - heroku open

## Notes
 - Procfile is a Heroku manadate
 - run.app() is a Flask convention not used in Heroku
   - gunicorn is used (in requirements)
