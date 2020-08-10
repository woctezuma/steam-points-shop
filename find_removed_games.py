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

    print(
        "\n# Detection results: {} games missing from SteamCardExchange.".format(
            len(missing_app_ids)
        )
    )
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


def find_app_ids_removed_from_steam_points_shop(verbose=False):
    steam_card_exchange_dico = load_data_from_steam_card_exchange()
    steam_card_exchange_app_ids = set(steam_card_exchange_dico.keys())

    steam_points_shop_dico = load_data_from_steam_points_shop()
    steam_points_shop_app_ids = set(steam_points_shop_dico.keys())

    removed_app_ids = steam_card_exchange_app_ids.difference(steam_points_shop_app_ids)

    removed_app_ids = sorted(removed_app_ids, key=int)

    print(
        "\n# Detection results: {} games removed from Steam Points Shop.".format(
            len(removed_app_ids)
        )
    )

    if verbose:
        for app_id in removed_app_ids:
            app_info = steam_card_exchange_dico[app_id]

            print(
                "-   {} (appID = {}): {}".format(
                    app_info["name"], app_id, get_urls_for_markdown_display(app_id),
                )
            )

    return removed_app_ids


def main(verbose=False):
    missing_app_ids = find_app_ids_missing_from_steam_card_exchange(verbose=verbose)
    removed_app_ids = find_app_ids_removed_from_steam_points_shop(verbose=verbose)

    return True


if __name__ == "__main__":
    main(verbose=True)
