from flask import Flask
app = Flask(__name__)

import os
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import FlaskLogstashFormatter

LOGSTASH_HOST = os.environ.get('LOGSTASH_HOST', None)
LOGSTASH_DB_PATH = os.environ.get('LOGSTASH_DB_PATH', None)
LOGSTASH_TRANSPORT = os.environ.get('LOGSTASH_TRANSPORT', None)
LOGSTASH_PORT = os.environ.get('LOGSTASH_PORT', None)

logstash_handler = AsynchronousLogstashHandler(
    LOGSTASH_HOST,
    LOGSTASH_PORT,
    database_path=LOGSTASH_DB_PATH,
    transport=LOGSTASH_TRANSPORT,
)

logstash_handler.formatter = FlaskLogstashFormatter(metadata={"amit": "flaskapp"})
app.logger.addHandler(logstash_handler)

@app.route('/')
def hello():
    return '<h1>Hello from Flask & Docker</h2>'

print(LOGSTASH_HOST)
print(LOGSTASH_DB_PATH)
print(LOGSTASH_TRANSPORT)
print(LOGSTASH_PORT)


if __name__ == "__main__":
    app.run(debug=True)
