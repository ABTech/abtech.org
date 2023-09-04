---
layout: default
title: Current Crew
permalink: /people/
nav_page: people
nav_page_specific: currentCrew

# lists can be found in the JSON files in the _data folder in the root of the repo

---

<h1 class="text-center pt-4"> Current Crew </h1>

<hr class="bg-primary"/>

## Officers

<div class="row row-cols-1 row-cols-lg-2 g-4 mb-3">
  {% for officer in site.data.people_currentcrew_officers %}<div class="col">
    <div class="card h-100 rounded border-primary border-1 bg-light">
      <div class="row g-0">
        <div class="col-sm-4">
          <img src="{{ officer.img | prepend: '/assets/img/officers/' | realtive_url }}" alt="Photo of {{ officer.name }}" class="img-fluid rounded">
        </div>
        <div class="col-sm-8">
          <div class="card-body">
            <h3 class="card-title user-select-none">{{ officer.name }}</h3>
            <p class="card-text"><span class="text-muted">{{ officer.title }}</span></p>
            <p class="card-text">{{ officer.desc }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  {% endfor %}
</div>

## General Members

<ul class="align-items-start align-content-center custom-list-columns-4 list-unstyled">
  {% assign sortedGeneralMembers = site.data.people_currentcrew_generalmembers | sort_natural: 'last_name' %}
  {% for member in sortedGeneralMembers %}<li class="border-start border-secondary mb-1 ps-1 user-select-none">{{ member.first_name }} {{ member.last_name }}</li>{% endfor %}
</ul>

