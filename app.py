from flask import Flask
import logging
import sys
import os
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import FlaskLogstashFormatter

app = Flask(__name__)

LOGSTASH_HOST = os.environ.get('LOGSTASH_HOST', None)
LOGSTASH_DB_PATH = os.environ.get('LOGSTASH_DB_PATH', None)
LOGSTASH_TRANSPORT = os.environ.get('LOGSTASH_TRANSPORT', None)
LOGSTASH_PORT = os.environ.get('LOGSTASH_PORT', None)

logger = logging.getLogger("Flask & Docker & Logstah ( Fuck that shit)")
logger.setLevel(logging.INFO)
logger.formatter = FlaskLogstashFormatter(metadata={"amit": "flask-app"})
logger.addHandler(AsynchronousLogstashHandler(LOGSTASH_HOST, LOGSTASH_PORT, LOGSTASH_DB_PATH, LOGSTASH_TRANSPORT))


@app.route('/')
def home():
    logger.info("Hello from Flask & Docker & Logstah")
    return '<h1>Hello from Flask & Docker & Logstah</h1>'

# if __name__ == "__main__":
#     app.run(debug=True)
