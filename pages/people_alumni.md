---
layout: default
title: Alumni
permalink: /people/alumni/
nav_page: people
nav_page_specific: alumni
---

# Alumni

<hr class="bg-primary"/>

If you are an AB Tech alumnus and you aren't listed here, or just want to get in touch, drop us a line at [alumni@abtech.org](mailto:alumni@abtech.org).

Alumni should also be aware that a mailing list exists for their use.

To join, [visit http://abtech.org/mailman/listinfo/ghosts](http://abtech.org/mailman/listinfo/ghosts){:target="_blank"}. Posts go to [ghosts@abtech.org](mailto:ghosts@abtech.org).

## Partial Alumni List

<ul class="align-items-start align-content-center custom-list-columns-4 list-unstyled">
  {% assign sortedAlumni = site.data.people_currentcrew_alumni | sort_natural: 'last_name' %}
  {% for alum in sortedAlumni %}<li class="border-start border-secondary mb-1 ps-1"><span class="user-select-none">{{ alum.first_name }} {{ alum.last_name }}</span>{% if alum.mail != null %} [<a href="mailto:{{alum.mail}}">mail</a>]{% endif %}{% if alum.url != null %} [<a href="{{alum.url}}">web</a>]{% endif %}</li>{% endfor %}
</ul>

