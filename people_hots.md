---
layout: default
title: Heads of Tech
permalink: /people/hots/
nav_page: people
nav_page_specific: hots

# lists can be found in the JSON files in the _data folder in the root of the repo

---

# Heads of Tech (HoTs)

------

<div class="col-12 col-sm-8 col-lg-6 col-xl-4 m-auto">
  <table class="table table-striped table-bordered border-primary table-sm text-center">
    <thead><tr class="bg-primary text-white">
        <th scope="col">Year</th>
        <th scope="col">Head(s) of Tech</th>
    </tr></thead>
    <tbody>
        {% for hot in site.data.people_hots_hots %}<tr{% if forloop.first %} class="border-bottom-3"{% endif %}>
            <td>{{ hot.year }}</td>
            <td>{{ hot.name }}</td>
        </tr>
        {% endfor %}
    </tbody>
  </table>
</div>
