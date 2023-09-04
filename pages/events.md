---
layout: default
title: Events Archive
permalink: /events/
nav_page: events
stylesheets:
 - '/assets/css/pages/events.css'
---

# Events Archive

<hr class="bg-primary"/>

Over the years, AB Tech has had the pleasure of working with a number of major acts, although they weren't necessarily that big at the time. This list covers major shows produced in whole or part by Tech since its creation.

<div class="sticky-top bg-body w-100 pt-1 pb-1 border-bottom border-primary border-2" id="eventTabsStickyContainer">
  <ul class="nav nav-pills nav-fill" id="eventsTabs" role="tablist">
  {% for tab in site.data.events_events %}
    <li class="nav-item" role="presentation">
      <button class="nav-link{% if forloop.first %} active{% endif %}" id="events-{{ tab[0] }}-tab" data-bs-toggle="pill" data-bs-target="#events-{{ tab[0] }}" type="button" role="tab" aria-controls="events-{{ tab[0] }}" aria-selected="{% if forloop.first %}true{% else %}false{% endif %}">{{ tab[0] }}</button>
    </li>
  {% endfor %}
  </ul>
</div>
<div class="tab-content" id="eventsTabsContent">
  {% for tab in site.data.events_events %}
  <div class="tab-pane fade{% if forloop.first %} show active{% endif %}" id="events-{{ tab[0] }}" role="tabpanel" aria-labelledby="events-{{ tab[0] }}-tab">
    {% for group in tab[1] %}
    <div class="card border-0 rounded-0">
      <h5 class="card-header rounded-0 bg-secondary text-white">{{ group[0] }}</h5>
      <ul class="list-group list-group-flush">
          {% for event in group[1] %}
          <li class="list-group-item">
            <div class="row">
              <strong class="col-4 col-sm-6 col-md-8">{{ event.name }}</strong>
              <div class="col-4 col-sm-3 col-md-2">{{ event.date | date: "%B %-d" }}</div>
              <div class="col-4 col-sm-3 col-md-2">{{ event.venue }}</div>
              <div class="col-12 text-muted">{{ event.desc }}</div>
            </div>
          </li>
          {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>
  {% endfor %}
</div>
