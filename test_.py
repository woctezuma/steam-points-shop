import unittest

import download_steam_card_exchange
import download_steam_points_shop
import find_missing_games
import find_removed_games
import utils


class TestDownloadSteamCardExchangeMethods(unittest.TestCase):
    def test_get_steamcardexchange_api_url(self):
        url = download_steam_card_exchange.get_steamcardexchange_api_url()
        assert url.startswith("https://www.steamcardexchange.net/")

    def test_get_steamcardexchange_api_params(self):
        params = download_steam_card_exchange.get_steamcardexchange_api_params()
        assert "GetBoosterPrices" in params

    def test_get_steamcardexchange_api_response(self):
        response = download_steam_card_exchange.get_steamcardexchange_api_response()
        assert response is not None

    def test_parse_steamcardexchange_api_response(self):
        response = download_steam_card_exchange.get_steamcardexchange_api_response()
        dico = download_steam_card_exchange.parse_steamcardexchange_api_response(
            response,
            verbose=True,
        )
        assert len(dico) > 0

    def test_load_data_from_steam_card_exchange(self):
        dico = download_steam_card_exchange.load_data_from_steam_card_exchange(
            force_download=True,
            verbose=True,
        )
        assert len(dico) > 0


class TestDownloadSteamPointsShopMethods(unittest.TestCase):
    def test_get_steam_points_shop_api_url(self):
        url = download_steam_points_shop.get_steam_points_shop_api_url()
        assert url.startswith("https://api.steampowered.com/")

    def test_get_steam_points_shop_api_response(self):
        response = download_steam_points_shop.get_steam_points_shop_api_response()
        assert response is not None

    def test_parse_steam_points_shop_api_response(self):
        response = download_steam_points_shop.get_steam_points_shop_api_response()
        dico = download_steam_points_shop.parse_steam_points_shop_api_response(
            response,
            verbose=True,
        )
        assert len(dico) > 0

    def test_load_data_from_steam_points_shop(self):
        dico = download_steam_points_shop.load_data_from_steam_points_shop(
            force_download=True,
            verbose=True,
        )
        assert len(dico) > 0


class TestFindMissingGamesMethods(unittest.TestCase):
    def test_find_app_ids_missing_from_steam_card_exchange(self):
        missing_app_ids = (
            find_missing_games.find_app_ids_missing_from_steam_card_exchange(
                force_download=True,
                verbose=True,
            )
        )
        assert len(missing_app_ids) >= 0


class TestFindRemovedGamesMethods(unittest.TestCase):
    def test_find_app_ids_removed_from_steam_points_shop(self):
        removed_app_ids = (
            find_removed_games.find_app_ids_removed_from_steam_points_shop(
                force_download=True,
                verbose=True,
            )
        )
        assert len(removed_app_ids) > 0


class TestUtilsMethods(unittest.TestCase):
    def test_get_data_folder(self):
        data_folder = utils.get_data_folder()
        assert data_folder == "data/"

    def test_get_steamcardexchange_file_name(self):
        steam_card_exchange_file_name = utils.get_steamcardexchange_file_name()
        assert steam_card_exchange_file_name == "data/steam_card_exchange.json"

    def test_get_steam_points_shop_file_name(self):
        steam_points_shop_file_name = utils.get_steam_points_shop_file_name()
        assert steam_points_shop_file_name == "data/steam_points_shop.json"

    def test_get_steamcardexchange_url(self):
        app_id = None
        url = utils.get_steamcardexchange_url(app_id)
        assert url.startswith("https://www.steamcardexchange.net/")

    def test_get_steam_db_url(self):
        app_id = None
        url = utils.get_steam_db_url(app_id)
        assert url.startswith("https://steamdb.info/")

    def test_get_steam_points_shop_url(self):
        app_id = None
        url = utils.get_steam_points_shop_url(app_id)
        assert url.startswith("https://store.steampowered.com/points/shop/")

    def test_get_urls_for_markdown_display(self):
        app_id = None
        text = utils.get_urls_for_markdown_display(app_id)
        assert len(text) > 0


if __name__ == "__main__":
    unittest.main()
