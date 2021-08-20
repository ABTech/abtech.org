---
layout: default
title: Request Event
permalink: /request/
nav_page: request
---

<h1>Request Event</h1>

<form class="col-12 col-md-10 col-lg-8 mx-auto mb-2 px-2">
  <div class="row">
    <div class="alert alert-danger" role="alert">
      Please call <a href="tel:+14122682104" class="user-select-all">(412) 268-2104</a> to request an event with less than 48 hours notice.
    </div>
  </div>
  <div class="row">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" class="form-control" id="request_eventName" required placeholder="Event Name">
        <label for="request_eventName">Event Name</label>
      </div>
    </div>
  </div>
  <div class="row mb-1">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" class="form-control" id="request_organization" required placeholder="Organization" aria-describedby="request_organization_help">
        <label for="request_organization">Organization</label>
      </div>
      <div id="request_organization_help" class="form-text col-12 mb-3">
        <p>The hosting or sponsoring organization (i.e. who will be paying for our services)</p>
      </div>
    </div>
  </div>
  <div class="row mb-1">
    <div class="mb-3 mb-md-0 col-md-6 gx-0 pe-2">
      <div class="form-floating">
        <input type="text" class="form-control" id="request_contactName" required placeholder="Sam Abtek" required aria-describedby="request_contact_help">
        <label for="request_contactName">Contact Name</label>
      </div>
    </div>
    <div class="mb-0 col-md-6 gx-0 ps-2">
      <div class="form-floating">
        <input type="email" class="form-control" id="request_contactEmail" required placeholder="name@andrew.cmu.edu" aria-describedby="request_contact_help">
        <label for="request_contactEmail">Contact Email</label>
      </div>
    </div>
    <div id="request_contact_help" class="form-text col-12 mb-3">
      <p>You will receive a confirmation email shortly after submitting this form.</p>
    </div>
  </div>
  <div class="row">
    <div class="mb-3 col-md-6 gx-0 pe-2">
      <div class="form-floating">
        <input type="date" class="form-control" id="request_startDate" required aria-describedby="request_time_help">
        <label for="request_startDate">Start Date</label>
      </div>
    </div>
    <div class="mb-3 col-md-6 gx-0 ps-2">
      <div class="form-floating">
        <input type="time" class="form-control" id="request_startTime" required aria-describedby="request_time_help">
        <label for="request_startTime">Start Time</label>
      </div>
    </div>
  </div>
  <div class="row mb-1">
    <div class="mb-3 mb-md-0 col-md-6 gx-0 pe-2">
      <div class="form-floating">
        <input type="date" class="form-control" id="request_endDate" required aria-describedby="request_time_help">
        <label for="request_endDate">End Date</label>
      </div>
    </div>
    <div class="mb-0 col-md-6 gx-0 ps-2">
      <div class="form-floating">
        <input type="time" class="form-control" id="request_endTime" required aria-describedby="request_time_help">
        <label for="request_endTime">End Time</label>
      </div>
    </div>
    <div id="request_time_help" class="form-text col-12 mb-3">
      <p>If your dates and times are not yet finalized, please note them in the details section below.</p>
      <p><strong>Please try to allow for least one week advance notice of the event.</strong> Larger events require more lead time (usually 2 weeks or more). We recommend that you contact us as soon as possible to make sure we can fit you in our schedule, as we frequently work multiple events simultaneously and have limited staff and equipment. <strong>Events requested less than a week in advance may incur a small late fee. Events requested less than 48 hours in advance will incur a larger late fee.</strong></p>
      <p>Changes (venue, times, equipment needs, etc.) or cancellations to the event less than 48 hours before the show may not be possible or may incur an additional late notice fee.</p>
    </div>
  </div>
  <div class="row mb-3">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <input type="text" class="form-control" id="request_location" required placeholder="Rangos" aria-describedby="request_location_help">
        <label for="request_location">Location/Venue</label>
        <div id="request_location_help" class="form-text">
          <p>Please state the precise venue (i.e. "UC Rangos 1 through 3" instead of just "Rangos")</p>
          <p><strong>Please contact us before reserving a venue and confirming show time, so that we can estimate the time required for our setup and teardown.</strong> Smaller shows may only require an hour for setup, but larger shows may require 8 hours or more. We need full access to the venue from the setup time through the end of our teardown, which can be for up to a few hours following the end of the show (depending on the complexity).</p></div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="mb-3 gx-0">
      <div class="form-floating">
        <textarea class="form-control" placeholder="Details" id="request_details" style="height: 200px" aria-describedby="request_details_help"></textarea>
        <label for="request_details">Details</label>
        <div id="request_details_help" class="form-text">Please be sure to include:
          <ul>
            <li><strong>Event type:</strong> Describe the details of the event/show/activity so we can provide the right equipment and staff</li>
            <li><strong>Estimated timings:</strong> for the event and setup time, or if your event spans multiple days</li>
            <li><strong>Technical riders and contracts:</strong> If performers have provided you with technical "riders" or requirements in their contract, it is best for us to have a copy of these to ensure they are met. Additionally, contact information for the performer is often useful if we need to request a clarification on technical requirements.</li>
            <li><strong>Any other relevant information or special requests</strong></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <button type="submit" class="btn btn-primary">Submit Request</button>
</form>
