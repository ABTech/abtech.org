---
layout: default
title: External Resources
permalink: /external/
nav_page: whatWeDo
nav_page_specific: external

# lists can be found in the JSON files in the _data folder in the root of the repo

---

# External Resources

<hr class="bg-primary"/>

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

<ul class="align-items-start align-content-center custom-list-columns-large-3 list-unstyled">
  {% assign sortedOrganizations = site.data.external_organizations | sort_natural: 'name' %}
  {% for organization in sortedOrganizations %}<li class="border-start border-secondary mb-1 ps-1"><a href="{{ organization.url }}" target="_blank">{{ organization.name }}</a></li>{% endfor %}
</ul>

## Manufacturers

Manufacturers of (most of) our equipment.

<ul class="align-items-start align-content-center custom-list-columns-4 list-unstyled">
  {% assign sortedManufacturers = site.data.external_manufacturers | sort_natural: 'name' %}
  {% for manufacturer in sortedManufacturers %}<li class="border-start border-secondary mb-1 ps-1"><a href="{{ manufacturer.url }}" target="_blank">{{ manufacturer.name }}</a></li>{% endfor %}
</ul>

