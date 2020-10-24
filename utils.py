# Code inspired from:
#   https://github.com/woctezuma/steam-market/blob/master/utils.py

from pathlib import Path


def get_data_folder():
    data_folder = "data/"
    Path(data_folder).mkdir(exist_ok=True)

    return data_folder


def get_steamcardexchange_file_name():
    return get_data_folder() + "steam_card_exchange.json"


def get_steam_points_shop_file_name():
    return get_data_folder() + "steam_points_shop.json"


def get_steamcardexchange_url(app_id):
    return "https://www.steamcardexchange.net/index.php?gamepage-appid-{}/".format(
        app_id
    )


def get_steam_db_url(app_id):
    return "https://steamdb.info/app/{}/".format(app_id)


def get_steam_points_shop_url(app_id):
    return "https://store.steampowered.com/points/shop/app/{}".format(app_id)


def get_urls_for_markdown_display(app_id):
    return "[SteamDB]({}) ; [SteamCardExchange]({}) ; [Steam Points Shop]({})".format(
        get_steam_db_url(app_id),
        get_steamcardexchange_url(app_id),
        get_steam_points_shop_url(app_id),
    )
