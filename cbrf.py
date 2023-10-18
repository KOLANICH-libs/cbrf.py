__all__ = ["ExchangeRate", "CentroBank"]
import datetime
import re
import typing
from decimal import Decimal
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/cbrf.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

import bs4
from Cache import Cache
from ratelimit import rate_limited

try:
	import httpx
except ImportError:
	import requests as httpx

__author__ = "KOLANICH"
__license__ = "Unlicense"
__copyright__ = r"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org/>
"""

CBR_BASE = "https://www.cbr.ru/"
uris = {
	"REST": [
		CBR_BASE + "scripts/XML_daily_eng.asp",
		"https://www.cbr-xml-daily.ru/daily_eng.xml"  # this API is not the official one, so we don't use it
	],
	"WSDL": CBR_BASE + "DailyInfoWebServ/DailyInfo.asmx?WSDL"
}

remap = {
	"charcode": "iso",
	"numcode": "isoNumCode",
	"name": "name",
	"nominal": "nominal",
	"value": "rate",
	"id": "id"
}
currencyCodeRx = re.compile("^[A-Z]{3}$")


class ExchangeRate:
	__slots__ = ("iso", "name", "nominal", "isoNumCode", "rate", "id")

	def __init__(self, **kwargs) -> None:
		if not currencyCodeRx.match(kwargs["iso"]):
			raise ValueError("iso must be a 3 char ISO currency code")
		self.iso = kwargs["iso"]
		self.name = kwargs["name"]
		self.id = kwargs["id"]
		self.nominal = int(kwargs["nominal"])
		self.isoNumCode = int(kwargs["isoNumCode"])
		self.rate = kwargs["rate"]
		if isinstance(self.rate, str):
			self.rate = Decimal(self.rate.replace(",", "."))
			# self.rate=float(self.rate.replace(",", "."))

	def __repr__(self) -> str:
		return self.__class__.__name__ + "{" + ", ".join((k + "=" + repr(getattr(self, k)) for k in self.__class__.__slots__)) + "}"


@rate_limited(0.5)
def downloadXml() -> str:
	resp = httpx.get(uris["REST"][0])
	try:
		resp.raise_for_status()
		return resp.text
	except:
		return None


defaultCacheFilename = "./" + "centrobank_rates.sqlite"
defaultObsolescenseSeconds = 3600 * 12


class CentroBank:
	def __init__(self, cacheFileName: str = defaultCacheFilename, obsolescenseSeconds: int = defaultObsolescenseSeconds) -> None:
		self.cache = Cache(cacheFileName)
		with self.cache as cache:
			try:
				self.last = datetime.datetime.fromtimestamp(cache["last_update"])
			except:
				self.last = datetime.datetime.fromtimestamp(0)

		self.obsolescenseSeconds = obsolescenseSeconds

		(self.byISO, self.byName) = self.__class__.buildIndexes(self.getExchangeRates())

	def getXmlByDate(self) -> str:
		with self.cache as cache:
			now = datetime.datetime.now()
			if self.last and (now - self.last).total_seconds() >= self.obsolescenseSeconds:
				xml = downloadXml()
				self.last = cache["last_update"] = now.timestamp()
				cache["xml"] = xml
			else:
				print("cached")
				xml = cache["xml"]
			return xml

	def getExchangeRates(self, xml: None = None) -> typing.Iterable[ExchangeRate]:
		if not xml:
			xml = self.getXmlByDate()
		soup = bs4.BeautifulSoup(xml, "lxml")
		res = []
		for valute in soup.select("valute"):
			curr = {}
			for child in valute.select("*"):
				curr[remap[child.name]] = child.text
			curr.update(valute.attrs)
			res.append(ExchangeRate(**curr))
		return res

	@classmethod
	def buildIndexes(cls, rates: typing.Iterable[ExchangeRate]) -> typing.Tuple[typing.Mapping[str, ExchangeRate], typing.Mapping[str, ExchangeRate]]:
		byISO = {}
		byName = {}
		for rate in rates:
			byISO[rate.iso] = rate
			byName[rate.name] = rate
		return (byISO, byName)


# try:
	# import zeep
	# client = zeep.Client(uris["WSDL"])
# except:
	# pass

baseCurrencyISOCode = "RUB"
try:
	from pint.converters import ScaleConverter
	from pint.definitions import DimensionDefinition, UnitDefinition
	from pint.util import ParserHelper, UnitsContainer

	# ruble=DimensionDefinition(baseCurrencyISOCode, None, [], "[money]")

	class CurrencyDefinition(UnitDefinition):
		"""Definition of a currency unit."""

		def __init__(
			self,
			name,
			symbol,
			aliases,
		):
			self.reference = reference
			self.is_base = is_base
			if isinstance(converter, string_types):
				converter = ParserHelper.from_string(converter)
				self.reference = UnitsContainer(converter)
				converter = ScaleConverter(converter.scale)
			super(UnitDefinition, self).__init__(name, symbol, aliases, converter)

	def constructCurrencyDefinition(rate):
		parserHelper = ParserHelper.from_word(baseCurrencyISOCode) * rate.rate
		unit = UnitDefinition(rate.iso, symbol=None, aliases=[rate.name.replace(" ", "_")], reference=UnitsContainer(parserHelper), is_base=False, converter=ScaleConverter(parserHelper))

		#return unit
		return rate.iso + " = " + str(rate.rate) + " " + baseCurrencyISOCode

	def populatePintUnitRegistry(ureg, rates):
		#ureg.define(ruble)
		ureg.define(baseCurrencyISOCode + " = [money]")
		for rate in rates:
			ureg.define(constructCurrencyDefinition(rate))

	__all__.append("populatePintUnitRegistry")
except:
	pass

try:
	from money.exchange import SimpleBackend

	class MoneyBackend(SimpleBackend):
		def __init__(self):
			cbr = CentroBank()
			super().__init__()
			self._base = baseCurrencyISOCode
			self._rates = {k: 1 / v.rate for k, v in cbr.byISO.items()}
			del cbr

	__all__.append("MoneyBackend")
except:
	pass

__all__ = tuple(__all__)
