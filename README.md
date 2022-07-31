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
HEROKU_EMAIL=alokdwivedifgiet@gmail.com
HEROKU_API_KEY=66cd5971-e19e-4c6f-aab7-9da02f650f72
hEROKU_APPLICATION_NAME=my-app-project1



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
docker run -p 5000:5000 -e PORT:5000  85a3c8443fd3

""""

