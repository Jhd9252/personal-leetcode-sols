
!sudo curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
!sudo echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
!sudo apt update
!sudo apt install -y mongodb-org

# start the service
!sudo service mongod start
!pip install pymongo

# import and start pymongo
from pymongo import MongoClient

client = MongoClient()

client.list_database_names() # ['admin', 'local']