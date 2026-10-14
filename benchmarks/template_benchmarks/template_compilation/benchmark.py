from textwrap import dedent

from django import template

from ...utils import bench_setup


class TemplateCompile:
    def setup(self):
        bench_setup()

    def time_template_compile(self):
        template.Template(
            """
            {% for v in vals %}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
                {{ v }}
            {% endfor %}
        """
        )

    def time_template_compile_full(self):
        template.Template(dedent("""
        {% extends "base.html" %}

        {% block title %}Projects — {{ organization.name }}{% endblock %}

        {% block content %}
        <header>
            <h1>{{ organization.name }}</h1>
            <p>{{ organization.description|default:"Your team's projects." }}</p>
            {% if perms.projects.add_project %}
                <a href="{% url 'project-create' %}">New project</a>
            {% endif %}
        </header>

        <form method="get">
            <label for="search">Search projects</label>
            <input id="search" name="q" value="{{ query|default:'' }}">
            <button type="submit">Search</button>
        </form>

        <ul class="projects">
            {% for project in page_obj %}
                <li class="{% cycle 'odd' 'even' %}">
                    <h2>
                        <a href="{% url 'project-detail' project.pk %}">
                            {{ project.name }}
                        </a>
                    </h2>
                    <p>{{ project.description|truncatewords:30 }}</p>
                    <dl>
                        <dt>Owner</dt>
                        <dd>{{ project.owner.get_full_name|default:"Unassigned" }}</dd>
                        <dt>Updated</dt>
                        <dd>{{ project.updated_at|date:"M j, Y" }}</dd>
                    </dl>
                    {% if project.archived %}
                        <span class="badge">Archived</span>
                    {% elif project.overdue %}
                        <span class="badge warning">Overdue</span>
                    {% endif %}
                    {% include "projects/actions.html" with project=project only %}
                </li>
            {% empty %}
                <li>No projects found.</li>
            {% endfor %}
        </ul>

        {% if page_obj.has_other_pages %}
            <nav aria-label="Pagination">
                {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}&amp;q={{ query|urlencode }}">
                        Previous
                    </a>
                {% endif %}
                <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
                {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}&amp;q={{ query|urlencode }}">
                        Next
                    </a>
                {% endif %}
            </nav>
        {% endif %}
        {% endblock %}
        """))
