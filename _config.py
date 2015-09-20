import os
base_dir = os.path.abspath(os.path.dirname(__file__))
DATABASE='flasktaskr.db'
USERNAME='lukasz'
PASSWORD='x'
SECRET_KEY='difficult_key'
WTF_CSRF_EMABLED= True
DATABASE_PATH=os.path.join(base_dir,DATABASE)