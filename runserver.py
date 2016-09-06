import os
from app import app

#Run on C9
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
app.run(host=host,port=port)