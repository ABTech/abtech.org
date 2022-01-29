---
layout: default
title: Request Event
permalink: /request/
nav_page: request
---

# Request Event

<hr class="bg-primary"/>

<noscript><style type="text/css">
.requestFormRow {
  display: none;
}
</style></noscript>
<form id="requestForm" class="col-12 col-md-10 col-lg-8 mx-auto mb-2 px-2" novalidate>
  <div class="row">
    <div class="alert alert-danger" role="alert">
      Please call <a href="tel:+14122682104" class="user-select-all">(412) 268-2104</a> to request an event with less than 48 hours notice.
    </div>
  </div>
  <noscript><div class="row">
    <div class="alert alert-warning" role="alert">
      This form requires JavaScript. Please enable JavaScript and refresh the page.
    </div>
  </div></noscript>
  <div class="row requestFormRow successHide">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" name="event_name"  class="form-control requestFormInput" id="request_eventName" required placeholder="Event Name" disabled maxlength="50">
        <label for="request_eventName">Event Name</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
  </div>
  <div class="row mb-1 requestFormRow successHide">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" name="organization" class="form-control requestFormInput" id="request_organization" required placeholder="Organization" aria-describedby="request_organization_help" disabled maxlength="75">
        <label for="request_organization">Organization</label>
        <div class="invalid-feedback"></div>
      </div>
      <div id="request_organization_help" class="form-text col-12 mb-3">
        <p>The hosting or sponsoring organization (i.e. who will be paying for our services)</p>
      </div>
    </div>
  </div>
  <div class="row mb-1 requestFormRow successHide">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" pattern="[a-zA-Z0-9 .-]+" name="oracle_string" class="form-control requestFormInput" id="request_oracle_string" placeholder="FUNDSRC-FUNC-ACTIVITY-ORG-ENTITY" aria-describedby="request_oracle_string_help" disabled maxlength="75">
        <label for="request_oracle_string">Oracle String (if known)</label>
        <div class="invalid-feedback"></div>
      </div>
      <div id="request_oracle_string_help" class="form-text col-12 mb-3">
        <p>Student organizations and individuals should leave this field blank</p>
      </div>
    </div>
  </div>
  <div class="row requestFormRow successHide">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" name="contact_name" class="form-control requestFormInput" id="request_contactName" required placeholder="Sam Abtek" required aria-describedby="request_contact_help" disabled pattern="\S+[ ]+\S+" minlength="3" maxlength="50">
        <label for="request_contactName">Contact Name (preferred and last)</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
  </div>
  <div class="row mb-1 requestFormRow successHide">
    <div class="mb-3 mb-md-0 col-md-6 gx-0 pe-md-2">
      <div class="form-floating">
        <input type="email" name="contact_email" class="form-control requestFormInput" id="request_contactEmail" required placeholder="name@andrew.cmu.edu" aria-describedby="request_contact_help" disabled>
        <label for="request_contactEmail">Contact Email</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
    <div class="mb-0 col-md-6 gx-0 ps-md-2">
      <div class="form-floating">
        <input type="tel" pattern="[ .()#+-ext]*(?:\d[ .()#+-ext]*){10,}" name="contact_phone" class="form-control requestFormInput" id="request_contactPhone" required placeholder="+1 412-268-2104" aria-describedby="request_contact_help" disabled>
        <label for="request_contactPhone">Contact Cell (+1 123-456-7890)</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
    <div id="request_contact_help" class="form-text col-12 mb-3 gx-0">
      <p>You will receive a confirmation email shortly after submitting this form</p>
    </div>
  </div>
  <div class="row requestFormRow successHide">
    <div class="mb-3 col-md-6 gx-0 pe-md-2">
      <div class="form-floating">
        <input type="date" name="start_date" class="form-control requestFormInput" id="request_startDate" required aria-describedby="request_time_help" disabled min="1973-01-01" value="1973-01-01">
        <label for="request_startDate">Start Date</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
    <div class="mb-3 col-md-6 gx-0 ps-md-2">
      <div class="form-floating">
        <input type="time" name="start_time" class="form-control requestFormInput" id="request_startTime" required aria-describedby="request_time_help" disabled>
        <label for="request_startTime">Start Time</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
  </div>
  <div class="row mb-1 requestFormRow successHide">
    <div class="mb-3 mb-md-0 col-md-6 gx-0 pe-md-2">
      <div class="form-floating">
        <input type="date" name="end_date" class="form-control requestFormInput" id="request_endDate" required aria-describedby="request_time_help" disabled min="1973-01-01" value="1973-01-01">
        <label for="request_endDate">End Date</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
    <div class="mb-0 col-md-6 gx-0 ps-md-2">
      <div class="form-floating">
        <input type="time" name="end_time" class="form-control requestFormInput" id="request_endTime" required aria-describedby="request_time_help" disabled>
        <label for="request_endTime">End Time</label>
        <div class="invalid-feedback"></div>
      </div>
    </div>
    <div id="request_time_help" class="form-text col-12 mb-3 gx-0">
      <p>If your dates and times are not yet finalized, please note them in the details section below.</p>
      <p><strong>Please submit at most one request per event.</strong> If your event has multiple dates with multiple parts (i.e. rehearsals, multiple setup times, etc.), then please note the additional parts in the details box below.</p>
      <p><strong>Please try to allow for least one week advance notice of the event.</strong> Larger events require more lead time (usually 2 weeks or more). We recommend that you contact us as soon as possible to make sure we can fit you in our schedule, as we frequently work multiple events simultaneously and have limited staff and equipment. <strong>Events requested less than a week in advance may incur a small late fee. Events requested less than 48 hours in advance will incur a larger late fee.</strong></p>
      <p>Changes (venue, times, equipment needs, etc.) or cancellations to the event less than 48 hours before the show may not be possible or may incur an additional late notice fee.</p>
    </div>
  </div>
  <div class="row mb-3 requestFormRow successHide">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" name="location" class="form-control requestFormInput" id="request_location" required placeholder="Rangos" aria-describedby="request_location_help" disabled minlength="4" maxlength="50">
        <label for="request_location">Location/Venue</label>
        <div class="invalid-feedback"></div>
        <div id="request_location_help" class="form-text">
          <p>Please state the precise venue (i.e. "UC Rangos 1 through 3" instead of just "Rangos")</p>
          <p><strong>Please contact us before reserving a venue and confirming show time, so that we can estimate the time required for our setup and teardown.</strong> Smaller shows may only require an hour for setup, but larger shows may require 8 hours or more. We need full access to the venue from the setup time through the end of our teardown, which can be for up to a few hours following the end of the show (depending on the complexity).</p></div>
      </div>
    </div>
  </div>
  <div class="row requestFormRow successHide">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <textarea name="details"  class="form-control requestFormInput" required placeholder="Details" id="request_details" style="height: 200px" aria-describedby="request_details_help" disabled></textarea>
        <label for="request_details">Details</label>
        <div class="invalid-feedback"></div>
        <div id="request_details_help" class="form-text">Please be sure to include:
          <ul>
            <li><strong>Event type:</strong> Describe the details of the event/show/activity so we can provide the right equipment and staff</li>
            <li><strong>Estimated timings:</strong> for the event and setup time, or if your event spans multiple days</li>
            <li><strong>Technical riders and contracts:</strong> If performers have provided you with technical "riders" or requirements in their contract, it is best for us to have a copy of these to ensure they are met. Additionally, contact information for the performer is often useful if we need to request a clarification on technical requirements.</li>
            <li><strong>Files:</strong> If you need to share any files with us, please reply to the confirmation email with the attachments. Alternatively, we can provide a Carnegie Mellon Google Shared Drive folder.</li>
            <li><strong>Any other relevant information or special requests</strong></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="row requestFormRow">
    <div class="gx-0">
      <div id="requestForm_error" class="alert alert-danger" role="alert" style="display: none">An error has occurred. Please try again later or send your request to <a href="mailto:abtech@andrew.cmu.edu" class="user-select-all">abtech@andrew.cmu.edu</a>.</div>
      <div id="requestForm_bad_request" class="alert alert-warning" role="alert" style="display: none"><strong>There was an issue with your request; please correct the issue and try again:</strong><br> <span id="requestForm_bad_request_msg"></span></div>
      <div id="requestForm_success" class="alert alert-success" role="alert" style="display: none">Event successfully requested! Please check your email and spam shortly for a confirmation.</div>
    </div>
  </div>
  <div class="row requestFormRow">
    <div class="gx-0">
      <button id="request_submit" type="submit" class="btn btn-primary requestFormInput" disabled>
        <span id="request_spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        Submit Request
      </button>
      <a id="request_another" class="btn btn-primary" href="{{ '/request/' | relative_url }}" style="display: none">Request Another Event</a>
    </div>
  </div>
</form>

<script type="text/javascript">
  var request_form_disabled = true
  var formInputs = document.getElementsByClassName('requestFormInput')
  var formSuccessHide = document.getElementsByClassName('successHide')
  var formAlertError = document.getElementById('requestForm_error')
  var formAlertBadRequest = document.getElementById('requestForm_bad_request')
  var formAlertSuccess = document.getElementById('requestForm_success')
  var formAlertBadRequestMsg = document.getElementById('requestForm_bad_request_msg')
  var formRequestSubmit = document.getElementById('request_submit')
  var formRequestAnother = document.getElementById('request_another')
  var formRequestSpinner = document.getElementById('request_spinner')
  var form = document.getElementById('requestForm')
  var formStartDate = document.getElementById("request_startDate")
  var formStartTime = document.getElementById("request_startTime")
  var formEndDate = document.getElementById("request_endDate")
  var formEndTime = document.getElementById("request_endTime")
  form.addEventListener('submit', request_form_submit)

  function checkEventEnd () {
    var startDate = formStartDate.value
    var startTime = formStartTime.value
    var endDate = formEndDate.value
    var endTime = formEndTime.value
    var start = new Date(startDate + " " + startTime)
    var end = new Date(endDate + " " + endTime)
    msg = ''
    if (end <= start) {
      msg = 'End date and time must be after start date and time.'
    }
    formEndDate.setCustomValidity(msg)
    formEndTime.setCustomValidity(msg)
  }

  function request_form_show_validation (event) {
    checkEventEnd()
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

  form.addEventListener('input', request_form_show_validation)
  form.addEventListener('submit', request_form_show_validation)

  function request_form_submit(event) {
    event.preventDefault()
    if (request_form_disabled === false) {
      if (!form.checkValidity()) {
        event.stopPropagation()
        form.classList.add('was-validated')
        form.querySelector(':invalid').focus()
        return
      }
      form.classList.add('was-validated')
      form_disable()
      var request = new XMLHttpRequest()
      request.open('POST', '{% if jekyll.environment == "development" %}{{ 'http://localhost:3000/eventrequest' | relative_url }}{% else %}{{ '/eventrequest' | relative_url }}{% endif %}', true)
      request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
      request.onreadystatechange = function request_form_status() {
        if (request.readyState === 4) {
          if (request.status === 200) {
            formAlertSuccess.style.display = 'block'
            formRequestSubmit.style.display = 'none'
            formRequestSpinner.style.display = 'none'
            for (var i = 0; i < formSuccessHide.length; i++) formSuccessHide[i].style.display = 'none'
            form.reset()
            formRequestAnother.style.display = ''
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
    formRequestSpinner.style.display = 'none'
    request_form_disabled = false
    for (var i = 0; i < formInputs.length; i++) formInputs[i].disabled = false
    form.disabled = false
  }

  function form_disable() {
    formRequestSpinner.style.display = ''
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
