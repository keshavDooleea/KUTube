# KUTube

Download videos from a YoTube playlist on your device as mp3 files.

## Local Dev Setup

#### Setup Virtual Env

python -m venv venv  
pip install -r requirements.txt  
. venv/Scripts/activate

#### Run Flask locally

flask --app src/app.py run

#### Run new deployment

git push heroku
