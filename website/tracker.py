# Make an event on tracker

from robobrowser import RoboBrowser
from django.conf import settings
import datetime

TRACKER = settings.TRACKER
TRACKER_LOGIN = TRACKER + 'members/sign_in'
TRACKER_EVENT = TRACKER + '/events/new'
EVENT_DATE = "event[eventdates_attributes][0]"

class Tracker(object):
    def __init__(self):
        self.browser = RoboBrowser(history=True, parser='html.parser')
        self.login()

    def login(self):
        self.browser.open(TRACKER_LOGIN)
        login_form = self.browser.get_form(id='new_member')

        login_form["member[login]"] = settings.TRACKER_LOGIN
        login_form["member[password]"] = settings.TRACKER_PASSWORD
        self.browser.session.headers['Referer'] = TRACKER
        self.browser.submit_form(login_form)

    def create_event(self, event, description):
        try:
            self.browser.open(TRACKER_EVENT)

            event_form = self.browser.get_form(id='new_event')

            event_form["event[title]"] = event["event_name"]
            event_form["event[contact_name]"] = event["contact"]
            event_form["event[contactemail]"] = event["email"]
            event_form[EVENT_DATE + "[description]"] = "Show"
            event_form[EVENT_DATE + "[location_ids][]"] = "70"

            start_date = event["start_date"]
            start_time = event["start_time"]
            end_date = event["end_date"]
            end_time = event["end_time"]

            event_form[EVENT_DATE + "[startdate(1i)]"] = str(start_date.year)
            event_form[EVENT_DATE + "[startdate(2i)]"] = str(start_date.month)
            event_form[EVENT_DATE + "[startdate(3i)]"] = str(start_date.day)
            event_form[EVENT_DATE + "[startdate(4i)]"] = str(start_time.hour)
            event_form[EVENT_DATE + "[startdate(5i)]"] = str(start_time.minute)
            event_form[EVENT_DATE + "[enddate(1i)]"] = str(end_date.year)
            event_form[EVENT_DATE + "[enddate(2i)]"] = str(end_date.month)
            event_form[EVENT_DATE + "[enddate(3i)]"] = str(end_date.day)
            event_form[EVENT_DATE + "[enddate(4i)]"] = str(end_time.hour)
            event_form[EVENT_DATE + "[enddate(5i)]"] = str(end_time.minute)
            event_form["event[notes]"] = description

            self.browser.submit_form(event_form)

            if "errors prohibited" in str(self.browser.parsed):
                return self.browser.find(id="errorExplanation")
            else:
                return self.browser.url
        except Exception as e:
            return "EXCEPTION! " + str(e)
