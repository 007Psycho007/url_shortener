{% extends 'base.tpl' %}

{% block content %}
{% if message %}
<p>{{ message }}</p>
{% endif %}
    <form method="post">
    <table>
        <thead>
            <tr>
            <th scope="col">Short</th>
            <th scope="col">Long</th>
            <th scope="col">Delete</th>
            </tr>
        </thead>
        <tbody>
            
        {% for row in urls %}
            </tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>

                <td><button class="secondary" name="delete" type="submit" value="{{ row[0] }}">X</button></td>
            </tr>
        {% endfor %}
    </table>
    </form>
    <a href="/" role="button">Home</a>
{% endblock content %}