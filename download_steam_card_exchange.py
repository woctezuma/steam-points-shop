# Code inspired from:
#   https://github.com/woctezuma/steam-market/blob/master/download_steam_card_exchange.py

import json

import requests

from utils import get_steamcardexchange_file_name


def get_steamcardexchange_api_url():
    url = "https://www.steamcardexchange.net/api/request.php"

    return url


def get_steamcardexchange_api_params():
    params = {
        "GetBoosterPrices": "",
    }

    return params


def get_steamcardexchange_api_response(steamcardexchange_file_name=None):
    if steamcardexchange_file_name is None:
        steamcardexchange_file_name = get_steamcardexchange_file_name()

    print("Downloading response from SteamCardExchange.")

    response_data = requests.get(
        url=get_steamcardexchange_api_url(),
        params=get_steamcardexchange_api_params(),
    )

    status_code = response_data.status_code

    if status_code == 200:
        response = response_data.json()

        print(f"Saving response to {steamcardexchange_file_name}.")
        with open(steamcardexchange_file_name, "w", encoding="utf-8") as f:
            json.dump(response, f)

    else:
        print(f"Download failed with status code {status_code}.")
        response = None

    return response


def parse_steamcardexchange_api_response(response, verbose=False):
    dico = {}

    if "data" in response:
        for app_info in response["data"]:
            app_id = str(app_info[0][0])
            app_name = app_info[0][1]

            dico[app_id] = {}
            dico[app_id]["app_id"] = int(app_id)
            dico[app_id]["name"] = app_name

    if verbose:
        print(f"Parsing response: {len(dico)} games have been found.")

    return dico


def load_data_from_steam_card_exchange(
    steamcardexchange_file_name=None,
    force_download=False,
    verbose=False,
):
    if steamcardexchange_file_name is None:
        steamcardexchange_file_name = get_steamcardexchange_file_name()

    if force_download:
        response = get_steamcardexchange_api_response(steamcardexchange_file_name)

    try:
        if verbose:
            print(f"Loading response from {steamcardexchange_file_name}.")

        with open(steamcardexchange_file_name, encoding="utf-8") as f:
            response = json.load(f)

    except FileNotFoundError:
        print(f"File {steamcardexchange_file_name} not found.")
        response = get_steamcardexchange_api_response(steamcardexchange_file_name)

    dico = parse_steamcardexchange_api_response(response, verbose=verbose)

    return dico


if __name__ == "__main__":
    dico = load_data_from_steam_card_exchange()
