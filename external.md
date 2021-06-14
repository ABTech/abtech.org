---
layout: default
title: External Resources
permalink: /external/
nav_page: whatWeDo
nav_page_specific: external

# lists can be found in the JSON files in the _data folder in the root of the repo

---

# External Resources

------

## Contractors

AB Tech regularly works with these local vendors. If AB Tech is unavailable to support your event, we may refer you to one of these vendors.

<table class="table table-borderless table-sm w-auto m-auto">
  {% for contractor in site.data.external_contractors %}<tr>
    <td><a href="{{ contractor.url }}" target="_blank">{{ contractor.name }}</a></td>
    <td>{{ contractor.desc }}</td>
  </tr>
  {% endfor %}
</table>


## Organizations

Our regular clients, collaborators, providers, supporters, and affiliations.

<ul class="d-flex flex-wrap flex-column align-items-start align-content-center custom-multicolumn-list">
  {% for organization in site.data.external_organizations %}<li class="mx-5"><a href="{{ organization.url }}" target="_blank">{{ organization.name }}</a></li>{% endfor %}
</ul>

## Manufacturers

Manufacturers of (most of) our equipment.

<ul class="d-flex flex-wrap flex-column align-items-start align-content-center custom-multicolumn-list">
  {% for manufacturer in site.data.external_manufacturers %}<li class="mx-5"><a href="{{ manufacturer.url }}" target="_blank">{{ manufacturer.name }}</a></li>{% endfor %}
</ul>

