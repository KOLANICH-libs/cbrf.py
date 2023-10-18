cbrf.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=======
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/cbrf.py/workflows/CI/master/cbrf-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/cbrf.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/cbrf.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/cbrf.py.svg)](https://libraries.io/github/KOLANICH-libs/cbrf.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-libs/cbrf.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

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
