{% extends 'base.tpl' %}

{% block content %}
<form method="post">
  <label for="url">Enter URL</label>
  <input type="url" id="url" name="url">
  <div class="grid">
    <div><button type="submit">Shorten URL</button></div>
    <div><a href="/all_urls" role="button">Show all shortened URLs</a></div>
</form>
{% endblock content %}