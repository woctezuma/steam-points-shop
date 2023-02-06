# Objective: find games which appear on SteamCardExchange, but have been removed from Steam Points Shop.

from download_steam_card_exchange import load_data_from_steam_card_exchange
from download_steam_points_shop import load_data_from_steam_points_shop
from utils import get_urls_for_markdown_display


def find_app_ids_removed_from_steam_points_shop(force_download=False, verbose=False):
    steam_card_exchange_dico = load_data_from_steam_card_exchange(
        force_download=force_download,
    )
    steam_card_exchange_app_ids = set(steam_card_exchange_dico.keys())

    steam_points_shop_dico = load_data_from_steam_points_shop(
        force_download=force_download,
    )
    steam_points_shop_app_ids = set(steam_points_shop_dico.keys())

    removed_app_ids = steam_card_exchange_app_ids.difference(steam_points_shop_app_ids)

    removed_app_ids = sorted(removed_app_ids, key=int)

    print(f"# {len(removed_app_ids)} games removed from Steam Points Shop.")

    if verbose:
        for app_id in removed_app_ids:
            app_info = steam_card_exchange_dico[app_id]

            print(
                "-   {} (appID = {}): {}".format(
                    app_info["name"],
                    app_id,
                    get_urls_for_markdown_display(app_id),
                ),
            )

    return removed_app_ids


if __name__ == "__main__":
    removed_app_ids = find_app_ids_removed_from_steam_points_shop(
        force_download=True,
        verbose=True,
    )
