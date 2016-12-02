# Make an event on tracker

from robobrowser import RoboBrowser
from django.conf import settings
import datetime

TRACKER = 'https://tracker.abtech.org/'
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

            startdate = datetime.datetime.now() + datetime.timedelta(days=365)
            enddate = startdate + datetime.timedelta(days=1)
            event_form[EVENT_DATE + "[startdate(1i)]"] = str(startdate.year)
            event_form[EVENT_DATE + "[startdate(2i)]"] = str(startdate.month)
            event_form[EVENT_DATE + "[startdate(3i)]"] = str(startdate.day)
            event_form[EVENT_DATE + "[enddate(1i)]"] = str(enddate.year)
            event_form[EVENT_DATE + "[enddate(2i)]"] = str(enddate.month)
            event_form[EVENT_DATE + "[enddate(3i)]"] = str(enddate.day)
            event_form["event[notes]"] = description

            self.browser.submit_form(event_form)

            if "errors prohibited" in str(self.browser.parsed):
                return self.browser.find(id="errorExplanation")
            else:
                return self.browser.url
        except Exception as e:
            return "EXCEPTION! " + str(e)
