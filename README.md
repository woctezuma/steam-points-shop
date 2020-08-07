# Steam Points Shop

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to find games which have been removed from the [Steam Points Shop](https://store.steampowered.com/points/shop/).

The Steam Points Shop is a loyalty program for Steam.
It allows to exchange loyalty points for items (profile backgrounds, emoticons) which are otherwise available by spending money:
-   either by collecting a complete set of trading cards, then crafting badges, to have a *chance* to obtain one of many items (at least three) of different rarity.
-   or by directly purchasing the item from another user via the Steam Market.

Interestingly, some games are excluded from the Steam Points Shop, or removed by request of the game developers.
The complete list is not public, but can be inferred from public data.

![Cover: reply by Steam Support](https://github.com/woctezuma/steam-points-shop/wiki/img/steam_support.png)

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python find_removed_games.py
```

## Results

The [Wiki](https://github.com/woctezuma/steam-points-shop/wiki) shows a list of removed games.

## References

-   [Steam Points Shop](https://store.steampowered.com/points/shop/)
-   [`steam-market`](https://github.com/woctezuma/steam-market): find arbitrages on the Steam Market.

<!-- Definitions -->

[build]: <https://travis-ci.org/woctezuma/steam-points-shop>
[build-image]: <https://travis-ci.org/woctezuma/steam-points-shop.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/steam-points-shop/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/steam-points-shop/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/steam-points-shop/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/steam-points-shop>
[codecov-image]: <https://codecov.io/gh/woctezuma/steam-points-shop/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/steam-points-shop>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/ace838db0059444dbc0e2dc3388e12d9>
