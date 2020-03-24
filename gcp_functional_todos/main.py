"""docs"""
from flask import Flask, render_template_string

APP = Flask(__name__)
APP.debug = True

INDEX_TEMPLATE = """
<!DOCTYPE html>
<head>
  <title>Saying Hello</title>
</head>
<body>
  {% for place in places %}
  Hello, <b>{{ place }}!</b><br>
  {% endfor %}
  Hello, finally without GUI but with local testing, good job, {{ name }}!!! :)
</body>
"""


@APP.route("/", defaults={"path": ""})
@APP.route("/<path:path>")
def hello(request=None, path=None):
    """docs"""
    name = request.path[1:] if request else path
    print(request)
    return render_template_string(
        INDEX_TEMPLATE, places=["World", "dev.to"], name=name
    )


if __name__ == "__main__":
    APP.run()
