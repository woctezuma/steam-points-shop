# Objective: find games which appear on Steam Points Shop, but are missing from SteamCardExchange.

from utils import get_urls_for_markdown_display
from download_steam_card_exchange import load_data_from_steam_card_exchange
from download_steam_points_shop import load_data_from_steam_points_shop
import steamspypi


def find_app_ids_missing_from_steam_card_exchange(verbose=False):
    steamspy_dico = steamspypi.load()

    steam_card_exchange_dico = load_data_from_steam_card_exchange()
    steam_card_exchange_app_ids = set(steam_card_exchange_dico.keys())

    steam_points_shop_dico = load_data_from_steam_points_shop()
    steam_points_shop_app_ids = set(steam_points_shop_dico.keys())

    missing_app_ids = steam_points_shop_app_ids.difference(steam_card_exchange_app_ids)

    missing_app_ids = sorted(missing_app_ids, key=int)

    print("# {} games missing from SteamCardExchange.".format(len(missing_app_ids)))
    if verbose:
        for app_id in missing_app_ids:
            try:
                app_info = steamspy_dico[app_id]
            except KeyError:
                app_info = {"name": None}

            print(
                "-   {} (appID = {}): {}".format(
                    app_info["name"], app_id, get_urls_for_markdown_display(app_id),
                )
            )

    return missing_app_ids


if __name__ == "__main__":
    missing_app_ids = find_app_ids_missing_from_steam_card_exchange(verbose=True)
