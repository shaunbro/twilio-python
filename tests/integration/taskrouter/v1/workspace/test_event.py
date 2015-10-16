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


class EventTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "actor_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "actor_type": "workspace",
                "actor_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "description": "Worker JustinWorker updated to Idle Activity",
                "event_data": {
                    "worker_activity_name": "Offline",
                    "worker_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "worker_attributes": "{}",
                    "worker_name": "JustinWorker",
                    "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "worker_time_in_previous_activity": "26",
                    "workspace_name": "WorkspaceName",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                },
                "event_date": "2015-02-07T00:32:41Z",
                "event_type": "worker.activity",
                "resource_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource_type": "worker",
                "resource_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source": "twilio",
                "source_ip_address": "1.2.3.4",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events/EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        self.twilio.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .events(sid="EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events/EVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        ))
