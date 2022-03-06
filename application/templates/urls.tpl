{% extends 'base.tpl' %}

{% block content %}
    <table>
        <thead>
            <tr>
            <th scope="col">Short</th>
            <th scope="col">Long</th>
            </tr>
        </thead>
        <tbody>
            
        {% for row in urls %}
            </tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
            </tr>
        {% endfor %}
    </table>
    <a href="/" role="button">Home</a>
{% endblock content %}