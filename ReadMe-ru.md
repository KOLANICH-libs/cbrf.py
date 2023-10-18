cbrf.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=======
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/cbrf.py/workflows/CI/master/cbrf-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/cbrf.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/cbrf.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/cbrf.py.svg)](https://libraries.io/github/KOLANICH-libs/cbrf.py)
[![Стиль кода: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**Нам пришлось переехать на https://codeberg.org/KOLANICH-libs/cbrf.py, берите новые версии там.**

Под предлогом "большей безопасности" купленный Micro$oft GitHub начал [дискриминацию против тех, кто входит в аккаунт только по паролю](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/), в то же время будучи заинтересована коммерчески в успехе и широком внедрении [спецификаций FIDO](https://fidoalliance.org/specifications/download/) и [реализации Windows Hello](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422), которые [они продвигают как замену паролям](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). Это приведёт к плачевнным последствиям и абсолютно недопустимо, [прочитайте почему](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

Кто не хочет участвовать в строительстве своей цифровой тюрьмы, тем рекомендуется последовать примеру и свалить подальше от GitHub и Micro$oft. Вот [список альтернатив alternatives и некоторых причин сделать это](https://github.com/orgs/community/discussions/49869). Если они удалят дискуссию - есть хорошо известные места, в которых есть копии удалённого контента. [Прочитайте, почему вам тоже надо свалить с GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

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
