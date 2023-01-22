
def initialise_sync_api(api):
    bearer_token = 'Bearer %s' % api._token

    headers = {
        'Authorization': bearer_token,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = 'sync_token=*&resource_types=["all"]'

    try:
        response = requests.post(
            'https://api.todoist.com/sync/v9/sync', headers=headers, data=data)
    except Exception as e:
        logging.error(f"Error during initialise_sync_api: '{e}'")

    return json.loads(response.text)

def sync(api):
    # # This approach does not seem to work correctly.
    # BASE_URL = "https://api.todoist.com"
    # SYNC_VERSION = "v9"
    # SYNC_API = urljoin(BASE_URL, f"/sync/{SYNC_VERSION}/")
    # SYNC_ENDPOINT = "sync"
    # endpoint = urljoin(SYNC_API, SYNC_ENDPOINT)
    # task_data = post(api._session, endpoint, api._token, data=data)

    try:
        bearer_token = 'Bearer %s' % api._token

        headers = {
            'Authorization': bearer_token,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'sync_token=' + api.sync_token + \
            '&commands=' + json.dumps(api.queue)

        response = requests.post(
            'https://api.todoist.com/sync/v9/sync', headers=headers, data=data)

        if response.status_code == 200:
            return response.json()

        response.raise_for_status()
        return response.ok

    except Exception as e:
        logging.exception(
            'Error trying to sync with Todoist API: %s' % str(e))
        quit()