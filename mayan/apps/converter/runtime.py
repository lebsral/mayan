from __future__ import absolute_import

from .conf.settings import GRAPHICS_BACKEND
from .exceptions import OfficeBackendError
from .office_converter import OfficeConverter
from .utils import load_backend

try:
    office_converter = OfficeConverter()
except OfficeBackendError:
    office_converter = None

try:
    backend = load_backend().ConverterClass()
except ImproperlyConfigured:
    raise ImproperlyConfigured(u'Missing or incorrect converter backend: %s' % GRAPHICS_BACKEND)