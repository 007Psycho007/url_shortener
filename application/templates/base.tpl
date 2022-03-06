<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{{ url_for('static', filename='pico.min.css') }}">
    <title>{{ title }}</title>
  </head>
  <body>
    <main class="container">
        {% block content %}
        {% endblock content %}
    </main>
  </body>
</html>