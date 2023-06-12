from flask import Flask
import os
from datetime import datetime
import boto3

app = Flask(__name__)

log = 'log.txt'
s3 = boto3.client('s3')

@app.route("/")
def hello():
    with open(log, 'a') as logfile:
      sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S')
      logfile.write(sttime + '\n')
    s3.upload_file(log, "sre-tmp-bucket", "pre-stop/log.txt")    
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
