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


class ShortCodeTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": null,
                "date_updated": null,
                "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
                "short_code": "99990",
                "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_fallback_method": "POST",
                "sms_fallback_url": null,
                "sms_method": "POST",
                "sms_url": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .sms \
                             .short_codes(sid="SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
