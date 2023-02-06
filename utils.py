# Code inspired from:
#   https://github.com/woctezuma/steam-market/blob/master/utils.py

from pathlib import Path


def get_data_folder():
    data_folder = "data/"
    Path(data_folder).mkdir(exist_ok=True)

    return data_folder


def get_steamcardexchange_file_name():
    steam_card_exchange_file_name = get_data_folder() + "steam_card_exchange.json"

    return steam_card_exchange_file_name


def get_steam_points_shop_file_name():
    steam_points_shop_file_name = get_data_folder() + "steam_points_shop.json"

    return steam_points_shop_file_name


def get_steamcardexchange_url(app_id):
    url = "https://www.steamcardexchange.net/index.php?gamepage-appid-{}/".format(
        app_id,
    )

    return url


def get_steam_db_url(app_id):
    url = "https://steamdb.info/app/{}/".format(app_id)

    return url


def get_steam_points_shop_url(app_id):
    url = "https://store.steampowered.com/points/shop/app/{}".format(app_id)

    return url


def get_urls_for_markdown_display(app_id):
    urls_for_markdown_display = (
        "[SteamDB]({}) ; [SteamCardExchange]({}) ; [Steam Points Shop]({})".format(
            get_steam_db_url(app_id),
            get_steamcardexchange_url(app_id),
            get_steam_points_shop_url(app_id),
        )
    )

    return urls_for_markdown_display
