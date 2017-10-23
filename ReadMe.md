cbrf.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=======
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/cbrf.py/workflows/CI/master/cbrf-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/cbrf.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/cbrf.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/cbrf.py.svg)](https://libraries.io/github/KOLANICH-libs/cbrf.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

Gets currency exchange rates from [the official API](https://www.cbr.ru/scripts/root.asp) of [CentroBank of the Russian Federation](https://www.cbr.ru/) .

Disclaimer
----------
I AM NOT AFFILIATED WITH THE CENTROBANK. I'M JUST A CITIZEN AND RESIDENT OF RUSSIA SO I HAVE TO TRANSLATE PRICES USING THE CENTROBANK EXCHANGE RATE WHEN PROVIDING MY BOSS WITH THE RATIONALE THAT SOMETHING IS NEEDED.
NEITHER CREATING NOR PUBLISHING OF THIS LIBRARY CAN BE UNDERSTOOD AS PROMOTING ANY POLITICS, THE BANK, ITS EXCHANGE RATES OR ITS POSITION OR ANY FINANCIAL ADVISE.
THE LIBRARY IS POSTED HERE ONLY FOR CONVENIENCE FOR THE PEOPLE WHO HAVE TO USE THE EXCHANGE RATES BY CB RF.
NO GUARANTEE IS PROVIDED. I HOLD NO LIABILITY FOR ITS ACTIONS, QUALITY, CORRECTNESS OF DATA, EXCHANGE RATES, OR ANY OTHER LOSSES, LOST OR IMPLIED OR ASSUMED PROFIT, OR ANYTHING ELSE. PLEASE, SEE THE [(UN)LICENSE FILE](./UNLICENSE) FOR MORE INFO ABOUT THE LICENSE.


Getting the rates
----------
```python
from cbrf import CentroBank
cb=CentroBank()
print(cb.byISO["USD"])
```


`money` integration
--------------
```python
import money
from cbrf import MoneyBackend
money.xrates.install(MoneyBackend())
money.Money(1, "USD").to("RUB")
```

`pint` integration
--------------
!!! WARNING: FOR NOW IT DOESN'T USE `Decimal` type. Precision loss is likely to occur !!!
```python
import pint
from cbrf import populatePintUnitRegistry
ureg = pint.UnitRegistry(None)
populatePintUnitRegistry(ureg, cb.byISO.values())
ureg("1 USD").to(ureg.RUB)
```
