import sys
import os
import requests
import xbmc
import urllib
import urllib2
import urlparse
import json
import xbmcvfs
import requests
import xbmcaddon
import xbmcgui,xbmcplugin
from bs4 import BeautifulSoup
import time


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

try:
    loc = [i for i in requests.get('http://www.rrys.tv', allow_redirects=False).text.split() if 'location.href' in i ][0]
    loc = loc.split('=')[1].strip('"').strip("'")
    # http://www.zmz2019.com/rrys/index.html to http://www.zmz2019.com
    ZIMUZU_BASE = "/".join(loc.split('/')[:3])
except:
    ZIMUZU_BASE = 'http://www.rrys2019.com/'

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__cwd__        = xbmc.translatePath( __addon__.getAddonInfo('path') ).decode("utf-8")
__profile__    = xbmc.translatePath( __addon__.getAddonInfo('profile') ).decode("utf-8")
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ) ).decode("utf-8")
__temp__       = xbmc.translatePath( os.path.join( __profile__, 'temp') ).decode("utf-8")

ZIMUZU_API = ZIMUZU_BASE + '/search?keyword=%s&type=subtitle'
UserAgent  = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'

def log(module, msg):
    xbmc.log((u"%s::%s - %s" % (__scriptname__,module,msg,)).encode('utf-8'),level=xbmc.LOGERROR )

log(sys._getframe().f_code.co_name, "script id is %s" % __scriptid__)
log(sys._getframe().f_code.co_name, "__scriptname__ id is %s" %__scriptname__)
log(sys._getframe().f_code.co_name, "__cwd__ id is %s" % __cwd__)
log(sys._getframe().f_code.co_name, "__profile__ id is %s" % __profile__)
log(sys._getframe().f_code.co_name, "__resource__ id is %s" % __resource__)
log(sys._getframe().f_code.co_name, "__temp__ id is %s" % __temp__)
log(sys._getframe().f_code.co_name, "ZIMUZU_API id is %s" % ZIMUZU_API)

log(sys._getframe().f_code.co_name, "sys.argv[0] is %s" % sys.argv[0])
log(sys._getframe().f_code.co_name, "sys.argv[1] is %s" % sys.argv[1])
log(sys._getframe().f_code.co_name, "sys.argv[2] is %s" % sys.argv[2])

xbmcplugin.endOfDirectory(int(sys.argv[1]))