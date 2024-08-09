from .apirequest import ApiRequest

BASE_URL = 'https://api.revanced.app'

ENDPOINTS: dict[str, ApiRequest] = {
    'announcements': ApiRequest(f'{BASE_URL}/v2/announcements'),
    'patches_latest': ApiRequest(f'{BASE_URL}/v3/patches/latest'),
    'patches_latest_list': ApiRequest(f'{BASE_URL}/v3/patches/latest/list'),
    'patches_latest_version': ApiRequest(f'{BASE_URL}/v3/patches/latest/version'),
    'patches_keys': ApiRequest(f'{BASE_URL}/v3/patches/keys'),
    'manager_latest': ApiRequest(f'{BASE_URL}/v3/manager/latest'),
    'manager_latest_version': ApiRequest(f'{BASE_URL}/v3/manager/latest/version'),
    'contributors': ApiRequest(f'{BASE_URL}/v3/contributors'),
    'team': ApiRequest(f'{BASE_URL}/v3/team'),
    'about': ApiRequest(f'{BASE_URL}/v3/about'),
    'ping': ApiRequest(f'{BASE_URL}/v3/ping'),
    'rate_limit': ApiRequest(f'{BASE_URL}/v3/backend/rate_limit')
}