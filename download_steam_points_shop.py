import json

import requests

from utils import get_steam_points_shop_file_name


def get_steam_points_shop_api_url():
    url = "https://api.steampowered.com/ILoyaltyRewardsService/GetEligibleApps/v1/"

    return url


def get_steam_points_shop_api_response(steam_points_shop_file_name=None):
    if steam_points_shop_file_name is None:
        steam_points_shop_file_name = get_steam_points_shop_file_name()

    print("Downloading response from Steam Points Shop.")

    response_data = requests.get(url=get_steam_points_shop_api_url())

    status_code = response_data.status_code

    if status_code == 200:
        response = response_data.json()

        print("Saving response to {}.".format(steam_points_shop_file_name))
        with open(steam_points_shop_file_name, "w", encoding="utf-8") as f:
            json.dump(response, f)

    else:
        print("Download failed with status code {}.".format(status_code))
        response = None

    return response


def parse_steam_points_shop_api_response(response, verbose=False):
    dico = dict()

    for app_info in response["response"]["apps"]:
        app_id = str(app_info["appid"])

        dico[app_id] = dict()
        dico[app_id]["app_id"] = int(app_id)

    if verbose:
        print("Parsing response: {} games have been found.".format(len(dico)))

    return dico


def load_data_from_steam_points_shop(
    steam_points_shop_file_name=None,
    force_download=False,
    verbose=False,
):
    if steam_points_shop_file_name is None:
        steam_points_shop_file_name = get_steam_points_shop_file_name()

    if force_download:
        response = get_steam_points_shop_api_response(steam_points_shop_file_name)

    try:
        if verbose:
            print("Loading response from {}.".format(steam_points_shop_file_name))

        with open(steam_points_shop_file_name, "r", encoding="utf-8") as f:
            response = json.load(f)

    except FileNotFoundError:
        print("File {} not found.".format(steam_points_shop_file_name))
        response = get_steam_points_shop_api_response(steam_points_shop_file_name)

    dico = parse_steam_points_shop_api_response(response, verbose=verbose)

    return dico


if __name__ == "__main__":
    dico = load_data_from_steam_points_shop()
