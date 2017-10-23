cbrf.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=======
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/cbrf.py/workflows/CI/master/cbrf-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/cbrf.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/cbrf.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/cbrf.py.svg)](https://libraries.io/github/KOLANICH-libs/cbrf.py)
[![Стиль кода: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

Библиотека получает курсы обмена валют через [официальное API](https://www.cbr.ru/scripts/root.asp) [Центробанка РФ](https://www.cbr.ru/) .

Внимание
----------------
Я НЕ РАБОТАЮ НА ЦЕНТРОБАНК И НЕ СВЯЗАН С НИМ. Я ПРОСТО ГРАЖДАНИН И РЕЗИДЕНТ РФ И ПОЭТОМУ ВЫНУЖДЕН ИСПОЛЬЗОВАТЬ ОФИЦИАЛЬНЫЙ КУРС ДЛЯ ПЕРЕСЧЁТА СТОИМОСТИ ТОВАРОВ В РУБЛИ.
ПУБЛИКАЦИЯ ЭТОЙ БИБЛИОТЕКИ НЕ ДОЛЖНА ПОНИМАТЬСЯ КАК ПРОДВИЖЕНИЕ КАКОЙ ЛИБО ПОЛИТИКИ, БАНКА, УСТАНОВЛЕННЫХ ИМ ОБМЕННЫХ КУРСОВ ИЛИ ЕГО ПОЗИЦИИ, ИЛИ КАК СОВЕТ.
БИБЛИОТЕКА ОПУБЛИКОВАНА ЗДЕСЬ ИСКЛЮЧИТЕЛЬНО ДЛЯ УДОБСТВА ЛЮДЕЙ, КОТОРЫМ ПРИХОДИТСЯ ИСПОЛЬЗОВАТЬ ОБМЕННЫЕ КУРСЫ ЦЕНТРОБАНКА.
НИКАКИХ ГАРАНТИЙ НЕ ПРЕДОСТАВЛЯЕТСЯ. Я НЕ НЕСУ НИКАКОЙ ОТВЕТСТВЕННОСТИ ЗА КАЧЕСТВО ИЛИ ДЕЙСТВИЯ БИБЛИОТЕКИ ИЛИ БАНКА, ДОСТОВЕРНОСТЬ ДАННЫХ, ОБМЕННЫЕ КУРСЫ, ЛЮБЫЕ ДРУГИЕ ПОТЕРИ ИЛИ УБЫТКИ, ПОТЕРЯННУЮ, ПОДРАЗУМЕВАЕМУЮ ИЛИ ВЫДУМАННУЮ ПРИБЫЛЬ, И ВООБЩЕ ЧТО ЛИБО. ПОЖАЛУЙСТА, ПРОСМОТРИТЕ [ФАЙЛ С (РАЗ)ЛИЦЕНЗИЕЙ](./UNLICENSE) ДЛЯ БОЛЕЕ ПОДРОБНОЙ ИНФОРМАЦИИ О ЛИЦЕНЗИИ.


Получение курсов
-----------------------------
```python
from cbrf import CentroBank
cb=CentroBank()
print(cb.byISO["USD"])
```


использование с `money`
--------------
```python
import money
from cbrf import MoneyBackend
money.xrates.install(MoneyBackend())
money.Money(1, "USD").to("RUB")
```

использование с `pint`
--------------------
!!! Внимание: на данный момент не используется тип ```Decimal``` . Вероятна потеря точности !!!
```python
import pint
from cbrf import populatePintUnitRegistry
ureg = pint.UnitRegistry(None)
populatePintUnitRegistry(ureg, cb.byISO.values())
ureg("1 USD").to(ureg.RUB)
```
