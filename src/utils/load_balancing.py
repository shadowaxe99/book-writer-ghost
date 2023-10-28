```python
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```
This is a simple load balancing setup using Flask and Werkzeug's ProxyFix. In a production environment, you would typically place this behind a load balancer like Nginx or HAProxy. The load balancer would distribute incoming requests to multiple instances of this application, effectively balancing the load.