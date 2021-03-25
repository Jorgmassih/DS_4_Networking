import time
import requests
from random import sample


def get_tracklists(artist_id: int = 57620, releases_n: int = 5) -> list:
    """Get lists of tracklists from an amount of random releases. This function uses an
  external API to get the metada from discogs.com. 

    Parameters
    ----------
    artist_id : int, optional
        Identify a particular Artist in the Discogs DB. By default, setted value is
        Buddy Rich's ID.
    releases_n : int, optional
        Number of releases to use (5 is the default)

    Returns
    -------
    list
        A list of dicts with the release name as key and tracklist as value, in everyone.
  """

    # Getting the releases
    url = "https://api.discogs.com/artists/{}/releases".format(artist_id)
    response = requests.request(
        "GET",
        url,
    ).json()['releases']
    releases = [(release['id'], release['title']) for release in response
                if release['type'] == 'master']

    # Filtering and selecting the releases
    random_rels = sample(releases, k=releases_n)

    # Getting the info about the releases
    url = "https://api.discogs.com/masters/{}"
    tracklists_names = []

    # Isolating tracklist section from every release
    for rel in random_rels:
        tracklists = requests.request('GET',
                                      url.format(rel[0])).json()['tracklist']
        # Time to await to avoid response denegation from api.discogs.com due
        # the amount of requests in a short time lapse
        time.sleep(0.5)

        tracklists_names.append({
            rel[1]: [
                track['title'] for track in tracklists
                if track['type_'] == 'track'
            ]
        })

    return tracklists_names
