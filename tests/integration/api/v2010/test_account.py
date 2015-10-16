# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class AccountTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "auth_token": "AUTHTOKEN",
                "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
                "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
                "friendly_name": "Test Account",
                "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "owner_account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "active",
                "subresource_uris": {
                    "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                    "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                    "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                    "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                    "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                    "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
                },
                "type": "Full",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
