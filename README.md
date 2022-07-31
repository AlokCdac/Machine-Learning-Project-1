# Machine-Learning-Project-1
This is my Machine learning Project 

creating conda environment 
'''
conda create -p venv python==3.7 -y
''''

Activating conda environment 
'''
conda activate venv/
'''

Installing requirements 

'''
pip install -r requirements.txt
'''

To add file in git
'''
git add .
or 
git add filename
'''

To create version/commit

'''
git commit -m "message"
'''

To push data in git

'''
git push origin main
'''

To established CI/CD pipeline

'''

HEROKU_EMAIL=<Your heroku Email id >

HEROKU_API_KEY=<API_KEY>

HEROKU_APP_NAME=<Your Heroku App Name >


build docker image
'''

docker build -t<imagename>:<tagname>

'''
Note :- imagename must be in lowercase 


To list Docker images
'''
docker images 
'''

Run docker images 

''''
docker run -p 5000:5000 -e PORT:5000  <imageid>

""""

