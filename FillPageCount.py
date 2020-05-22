#  This file is part of Mylar.
#
#  Mylar is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Mylar is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Mylar.  If not, see <http://www.gnu.org/licenses/>.
import os, sys, locale
import argparse
import errno
import shutil
import time
import threading
import signal

sys.path.insert(1, os.path.join(os.path.dirname(__file__), 'lib'))

import mylar

from mylar import webstart, logger, filechecker, versioncheck, maintenance

import argparse

from mylar import helpers

helpers.fillPageCountfromMetaInfo('Wildstorm')


