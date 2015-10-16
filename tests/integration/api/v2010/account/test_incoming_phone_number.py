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


class IncomingPhoneNumberTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_requirements": "none",
                "api_version": "2010-04-01",
                "beta": false,
                "capabilities": {
                    "mms": true,
                    "sms": false,
                    "voice": true
                },
                "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",
                "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",
                "friendly_name": "(808) 925-5327",
                "phone_number": "+18089255327",
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_application_sid": "",
                "sms_fallback_method": "POST",
                "sms_fallback_url": "",
                "sms_method": "POST",
                "sms_url": "",
                "status_callback": "",
                "status_callback_method": "POST",
                "trunk_sid": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "voice_application_sid": "",
                "voice_caller_id_lookup": false,
                "voice_fallback_method": "POST",
                "voice_fallback_url": null,
                "voice_method": "POST",
                "voice_url": null
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .incoming_phone_numbers(sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
