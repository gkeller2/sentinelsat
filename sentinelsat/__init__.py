__version__ = '0.12.1'

# Import for backwards-compatibility
from . import sentinel

from .exceptions import InvalidChecksumError, SentinelAPIError
from .sentinel import SentinelAPI, read_geojson, geojson_to_wkt, format_query_date
