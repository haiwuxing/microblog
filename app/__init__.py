from flask import Flask

app = Flask(__name__)
# tell Flask to read it and use config.
app.config.from_object('config')

# 此句一定要在 app 创建以后调用，因为views.py 中用到了app
from app import views