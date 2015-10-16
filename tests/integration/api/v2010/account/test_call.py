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


class CallTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
