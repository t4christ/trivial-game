from requests import get, post
import os


class SmsClient(object):
    """
    A simple client for the Infobip SMS API.
    """

    def __init__(self, api_key=None,
                       api_url='https://api.infobip.com/sms',
                       sender_id='WStreams'):
        api_key = api_key or os.getenv('SMS_API_KEY')
        self._headers = {'authorization': "Basic U2VjdXJlTWVkaWE6VU9aTzhOeTYkNDE3"}
        # self._headers = {'Authorization': 'App %s' % api_key}
        self._api_url = api_url
        self._sender_id = sender_id

    def _request(self, method, url, data):
        url = '{base}{url}'.format(base=self._api_url, url=url)
        res = method(url, json=data, headers=self._headers)
        res.raise_for_status()
        return res.json()

    def send(self, **kwargs):
        """
        Send a single text message.

        Parameters::

            from: string
                  Represents sender ID and it can be alphanumeric or numeric. 
                  Alphanumeric sender IDs should be between 3 and 11 characters long;
                  numeric sender IDs should be between 3 and 14 characters.
              to: string, required
                  Destination address must be in international format.
            text: string
                  Text of the message to be sent.
        """
        assert 'to' in kwargs, 'A destination address is required.'
        assert 'text' in kwargs, 'A message is required.'
        data = dict({'from': self._sender_id}, **kwargs)
        return self._request(post, '/1/text/single', data)

    def send_many(self, messages):
        """
        Send multiple text messages to one or more destination numbers.

        Parameters::

            from: string
                  Represents sender ID and it can be alphanumeric or numeric. 
                  Alphanumeric sender IDs should be between 3 and 11 characters long;
                  numeric sender IDs should be between 3 and 14 characters.
              to: list of strings, required
                  Destination address must be in international format.
            text: string
                  Text of the message to be sent.
        """
        assert hasattr(messages, '__iter__'), 'Expected: iterable of dicts containing {to, text}.'
        data = [dict({'from': self._sender_id}, **message) for message in messages]
        return self._request(post, '/1/text/multi', {'messages': data})

    def status(self, msg_id):
        """
        Get one-time delivery reports for a text message.

        Parameters::

            messageid: string
                       The ID that uniquely identifies the text message (retrieved
                       from the response returned by `send(...)`).
        """
        return self._request(get, '/1/reports', {'messageid': msg_id})
