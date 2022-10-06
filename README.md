# ml-project
This is machine learning project.

### Software and account requirement 

Requirement.

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda enviroment
'''
conda create -p <enviroment_name> python==3.7 -y
-p 
'''
conda activate venv/
'''
conda activate venv
'''
installing requirement
'''

pip install -r rpip install -r requirements.txt
'''
To add files to git 
'''

git add <file_name>
'''
Note: To ignore file or folder in git then we can write the name of file/folder name in git 
'''

To check git status
'''
git status 
'''

To check diferent version of file 
'''
git log 
'''

To create version/commit all change to git 
'''

git commit -m "message"
'''

To send version changes to github
'''

git push origin main 
'''
To check remote url 
'''

git remote -v
'''

To setup CI/CD pipeline we need two information: 

1. HEROKU_EMAIL= pranavmore2568@gmail.com
2. HEROKU_API_KEY= 
3. HEROKU_APP_NAME= ml2569



Built docker image
'''

docker build -t <image_name>:<tag_name> .
'''

To list down docker image
'''

docker image
'''

Run docker image
'''

docker run -p 5000:5000 -e PORT=5000 image_name
'''

To check running containers in docker 
'''

docker container 
'''

To stop docker image
'''

docker stop <container_id>
'''

python setup.py install'''

