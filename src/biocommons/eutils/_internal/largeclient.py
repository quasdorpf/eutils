# -*- coding: utf-8 -*-

import logging
import os

import lxml.etree as le

from .exceptions import EutilsError
from .queryservice import QueryService
from .xmlfacades.dbsnp import ExchangeSet
from .xmlfacades.einforesult import EInfoResult
from .xmlfacades.entrezgeneset import EntrezgeneSet
from .xmlfacades.esearchresult import ESearchResult
from .xmlfacades.gbset import GBSet
from .xmlfacades.pubmedarticleset import PubmedArticleSet
from .xmlfacades.pubmedcentralarticleset import PubmedCentralArticleSet
from .client import Client


logger = logging.getLogger(__name__)


class LargeClient(Client):
    """modified Client to allow for larger returns from queries"""

    def __init__(self, cache=False, api_key=None, retmax=250):
        """
        :param str cache: passed to QueryService, which see for explanation
        :param str api_key: API key from NCBI
        :raises EutilsError: if cache file couldn't be created

        """
        default_args = {"retmode": "xml", "usehistory": "y", "retmax": retmax}

        self._qs = QueryService(cache=cache, api_key=api_key, default_args=default_args)

# <LICENSE>
# Copyright 2015 eutils Committers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
# </LICENSE>
