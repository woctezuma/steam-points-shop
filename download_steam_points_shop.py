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

        print(f"Saving response to {steam_points_shop_file_name}.")
        with open(steam_points_shop_file_name, "w", encoding="utf-8") as f:
            json.dump(response, f)

    else:
        print(f"Download failed with status code {status_code}.")
        response = None

    return response


def parse_steam_points_shop_api_response(response, verbose=False):
    dico = {}

    for app_info in response["response"]["apps"]:
        app_id = str(app_info["appid"])

        dico[app_id] = {}
        dico[app_id]["app_id"] = int(app_id)

    if verbose:
        print(f"Parsing response: {len(dico)} games have been found.")

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
            print(f"Loading response from {steam_points_shop_file_name}.")

        with open(steam_points_shop_file_name, encoding="utf-8") as f:
            response = json.load(f)

    except FileNotFoundError:
        print(f"File {steam_points_shop_file_name} not found.")
        response = get_steam_points_shop_api_response(steam_points_shop_file_name)

    dico = parse_steam_points_shop_api_response(response, verbose=verbose)

    return dico


if __name__ == "__main__":
    dico = load_data_from_steam_points_shop()
