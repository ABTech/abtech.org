---
layout: default
permalink: /
nav_page: home
stylesheets:
 - '/assets/css/pages/index.css'
---


<div id="bg-carousel" class="carousel slide carousel-fade w-100 h-100" data-bs-touch="false" data-bs-ride="carousel" data-bs-interval="10000">
  <div class="carousel-inner w-100 h-100">
    {% for item in site.data.index_carousel %}
    <div class="carousel-item{% if forloop.first %} active{% endif %} w-100 h-100">
      <img src="{{  item | prepend: '/assets/img/carousel/' | append: '.jpg' | realtive_url }}" class="d-block w-100 h-100" alt="{{ item }}">
    </div>
    {% endfor %}
  </div>
</div>
<div id="bg-carousel-gradient" class="d-block w-100 h-100"></div>

<div class="row justify-content-center align-items-center align-items-sm-end h-100">
    <img src="{{ '/assets/img/abtech_flybynight_white.svg' | relative_url }}" class="img-fluid d-none d-sm-block col-6 col-xl-5 text-center" alt="AB Tech Logo" style="filter: drop-shadow(0 0 6px red);" />
    <p class="col-sm-10 col-11 text-white text-center p-3"><strong>The Activities Board Technical Committee</strong>, commonly known as <strong class="text-nowrap">AB Tech</strong>, is the production organization charged with handling the technical production of University sponsored events in and around Pittsburgh. We provide high quality, professional grade entertainment production services, including sound reinforcement, lighting design, and event management at heavily subsidized rates to the Pittsburgh community. Our clients include student groups, university faculty & administration, and various independent companies and other organizations. We coordinate associated needs and services such as multi-phase/high-load power, rigging & trussing, staging rentals, backline rentals, and more.</p>
</div>
