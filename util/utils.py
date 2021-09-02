import pytz
from datetime import datetime


def format_cnpj(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'


def parse_value_to_float(value):
    try:
        return float(value.to_decimal())
    except AttributeError:
        return float(value)
    except TypeError:
        raise ('Unsupported type for common float')


def localize_date(date_time: datetime, timezone: str) -> datetime:
    local_timezone = pytz.timezone(timezone)
    local_datetime = local_timezone.localize(date_time)
    utc_datetime = local_datetime.astimezone(pytz.utc)
    return utc_datetime


def try_localize_utc(date_time: datetime) -> datetime:
    try:
        utc_date_time = pytz.utc.localize(date_time)
    except ValueError:
        utc_date_time = date_time
    return utc_date_time
