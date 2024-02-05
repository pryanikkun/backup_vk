from urllib.parse import urlencode

APP_ID = '51846714'
OAUTH_BASE_URL = 'https://oauth.vk.com/authorize'
params = {
    'client_id': APP_ID,
    'redirect_uri': 'https://example.com/callback',
    'display': 'page',
    'scope': 'photos',
    'response_type': 'token',
    'state': 123456,
}
# #
oauth_url = f'{OAUTH_BASE_URL}?{urlencode(params)}'
print(oauth_url)
