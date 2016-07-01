import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'bf0c6bbd'.decode('hex')
P2P_PORT = 9999
ADDRESS_VERSION = 76
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 9998
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'dashaddress' in (yield dashd.rpc_help()) and
            not (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'DASH'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Dash') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dash/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dash'), 'dash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.dashninja.pl/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.dashninja.pl/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.dashninja.pl/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
