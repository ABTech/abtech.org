---
layout: default
title: Join
permalink: /join/
nav_page: join
---

# Join

<hr class="bg-primary"/>

Membership in AB Tech is open to all Carnegie Mellon University students. In general, we recommend members have a good sense of humor and a willingness to push heavy stuff. If you have an interest in big speakers, fancy lighting, or being backstage at some of the coolest events on campus, AB Tech is the place to be.

Twice a year (September and January), AB Tech is at the Activities Fair along with other student organizations. Stop by, sign up, and we'll email you a place to show up to meet everyone else and start playing with some of the most awesome and expensive equipment in town. You can also check us out at our annual Sound and Light Studio during First-Year Orientation.

<span class="successHide">You can also sign up for our dlist right here, right now:</span>

<noscript><style type="text/css">
.joinFormRow {
  display: none;
}
</style></noscript>
<form id="joinForm" class="col-12 col-md-10 col-lg-8 mx-auto mb-2 px-2" novalidate>
  <noscript><div class="row">
    <div class="alert alert-warning" role="alert">
      This form requires JavaScript. Please enable JavaScript and refresh the page.
    </div>
  </div></noscript>
  <div class="row joinFormRow successHide">
    <div class="mb-3 gx-0 input-group input-group-lg">
      <input type="text" name="andrew_id"  class="form-control joinFormInput" id="join_andrew_id" required placeholder="Andrew ID" disabled minlength="3" maxlength="8" pattern="[a-z0-9]+" aria-describedby="join_andrew_id_domain" aria-label="Andrew ID">
      <span class="input-group-text" id="join_andrew_id_domain">@andrew.cmu.edu</span>
      <div class="invalid-feedback"></div>
    </div>
  </div>
  <div class="row mb-3 joinFormRow successHide">
    <div class="mb-3 mb-md-0 col-md-6 gx-0 pe-md-2">
      <div class="form-floating">
        <input type="text" name="preferred_name" class="form-control joinFormInput" id="join_preferred_name" required placeholder="Sam" disabled maxlength="50">
        <label for="join_preferred_name">Preferred Name</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
    <div class="mb-0 col-md-6 gx-0 ps-md-2">
      <div class="form-floating">
        <input type="text" name="last_name" class="form-control joinFormInput" id="join_last_name" required placeholder="Abtek" disabled maxlength="50">
        <label for="join_last_name">Last Name</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
  </div>
  <div class="row joinFormRow">
    <div class="gx-0">
      <div id="joinForm_error" class="alert alert-danger" role="alert" style="display: none">An error has occurred. Please try again later or send an email to <a href="mailto:abtech@andrew.cmu.edu" class="user-select-all">abtech@andrew.cmu.edu</a>.</div>
      <div id="joinForm_bad_request" class="alert alert-warning" role="alert" style="display: none"><strong>There was an issue with your request; please correct the issue and try again:</strong><br> <span id="joinForm_bad_request_msg"></span></div>
      <div id="joinForm_success" class="alert alert-success" role="alert" style="display: none">Success! Please check your email and spam shortly for an email.</div>
    </div>
  </div>
  <div class="row joinFormRow">
    <div class="gx-0">
      <button id="join_submit" type="submit" class="btn btn-primary joinFormInput" disabled>
        <span id="join_spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        Join AB Tech
      </button>
    </div>
  </div>
</form>

Generally our most extensive new member orientation event is held shortly after the September Activities Fair, but we encourage you to join at any time. Almost all of our training is done "on the job," and most of our members knew very little to nothing before they joined. After your sixth event, you'll "learn our secret handshake" and be considered a full member. AB Tech has no dues, no mandatory events/participation, and no other special requirements to stay a member: just show up to events when you have time!

Other options for joining AB Tech include:
 - **Emailing <a href="mailto:abtech@andrew.cmu.edu" class="user-select-all">abtech@andrew.cmu.edu</a>.** Again, we'll send you some places you might spot us in the future.
 - **Stopping by at an event.** Follow the loud music to its source, and you have probably stumbled across some techies. Say Hi!
 - **Following a friend!** Our members are fine, upstanding students at Carnegie Mellon (or so we hope), and should know our schedule. 

<script type="text/javascript">
  var join_form_disabled = true
  var formInputs = document.getElementsByClassName('joinFormInput')
  var formSuccessHide = document.getElementsByClassName('successHide')
  var formAlertError = document.getElementById('joinForm_error')
  var formAlertBadRequest = document.getElementById('joinForm_bad_request')
  var formAlertSuccess = document.getElementById('joinForm_success')
  var formAlertBadRequestMsg = document.getElementById('joinForm_bad_request_msg')
  var formJoinSubmit = document.getElementById('join_submit')
  var formJoinSpinner = document.getElementById('join_spinner')
  var form = document.getElementById('joinForm')
  form.addEventListener('submit', join_form_submit)

  function join_form_show_validation (event) {
    Array.prototype.slice.call(formInputs).forEach(input => {
      let nextSibling = input.nextSibling
      while (nextSibling) {
        if (nextSibling.nodeType == Node.ELEMENT_NODE && nextSibling.classList.contains('invalid-feedback')) {
          nextSibling.innerHTML = input.validationMessage
          break
        }
        nextSibling = nextSibling.nextSibling
      }
    })
  }

  form.addEventListener('input', join_form_show_validation)
  form.addEventListener('submit', join_form_show_validation)

  function join_form_submit(event) {
    event.preventDefault()
    if (join_form_disabled === false) {
      if (!form.checkValidity()) {
        event.stopPropagation()
        form.classList.add('was-validated')
        form.querySelector(':invalid').focus()
        return
      }
      form.classList.add('was-validated')
      form_disable()
      var request = new XMLHttpRequest()
      request.open('POST', '{% if jekyll.environment == "development" %}{{ 'http://localhost:3000/joinrequest' | relative_url }}{% else %}{{ '/joinrequest' | relative_url }}{% endif %}', true)
      request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
      request.onreadystatechange = function join_form_status() {
        if (request.readyState === 4) {
          if (request.status === 200) {
            formAlertSuccess.style.display = 'block'
            formJoinSubmit.style.display = 'none'
            formJoinSpinner.style.display = 'none'
            for (var i = 0; i < formSuccessHide.length; i++) formSuccessHide[i].style.display = 'none'
            form.reset()
          } else if (request.status >= 400 && request.status < 500) {
            jsonMsg = []
            try {
              jsonMsg = JSON.parse(request.response)
            } catch (err) {
              formAlertError.style.display = 'block'
              form_ready()
            }
            if (jsonMsg.length > 0) {
              msg = '<ul>'
              jsonMsg.forEach(item => {
                el = document.createElement('li')
                el.appendChild(document.createTextNode(item))
                msg += el.outerHTML
              })
              msg += '</ul>'
              formAlertBadRequestMsg.innerHTML = msg
              formAlertBadRequest.style.display = 'block'
              form_ready()
            }
          } else {
            formAlertError.style.display = 'block'
            form_ready()
          }
        }
      }
      formDataPairs = []
      for (var i = 0; i < formInputs.length; i++) {
        formDataPairs.push(encodeURIComponent(formInputs[i].name) + '=' + encodeURIComponent(formInputs[i].value))
      }
      var urlEncodedData = formDataPairs.join('&').replace(/%20/g, '+')
      request.send(urlEncodedData);
    }
  }

  function form_ready() {
    formJoinSpinner.style.display = 'none'
    join_form_disabled = false
    for (var i = 0; i < formInputs.length; i++) formInputs[i].disabled = false
    form.disabled = false
  }

  function form_disable() {
    formJoinSpinner.style.display = ''
    for (var i = 0; i < formInputs.length; i++) formInputs[i].disabled = true
    form.disabled = true
    formAlertError.style.display = 'none'
    formAlertBadRequest.style.display = 'none'
    formAlertSuccess.style.display = 'none'
    formAlertBadRequestMsg.innerHTML = ""
  }

  if (document.readyState != 'loading') form_ready()
  else document.addEventListener('DOMContentLoaded', form_ready)
</script>
