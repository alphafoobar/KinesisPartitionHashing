import hashlib


class Shard:
    def __init__(self, name, starting_hash, ending_hash):
        self.counter = 0
        self.name = name
        self.startingHash = starting_hash
        self.endingHash = ending_hash

BTC_USD = "6ea0d2ef-6dd0-4adb-ad32-f7f3db58ccbe"
LTC_USD = "2cbedd6a-dca2-48b1-a9db-9a1b24c2f85c"
ETH_USD = "bff074a3-3564-4479-a4bd-c49766acc63c"
XRP_USD = "89426269-ec59-4bef-9393-e50fd84f14cf"
XRP_BTC = "bb999433-d36d-42e9-9a2e-af1d3219c9ac"
EOS_USD = "5f5b8426-35b7-41df-a17a-84a4a6777b48"
EOS_BTC = "b884f3b1-23b4-4c9e-b95b-29a53165fecd"
BITFINEX = "7f26d058-318d-440c-9b55-486eabd8a065"
BITSTAMP = "48ca12fa-f5f4-484a-9945-84825030c8cd"
BTSE = "ec946827-a994-4d1f-9c5b-ef3ac944b270"
COINBASE_PRO = "65cf072d-2ffa-48f8-9497-6654234f52e3"
KRAKEN = "fa75a209-f460-4195-bbcc-56eb72286e3d"
BITTREX = "2eccd6dd-e073-4767-942d-24301dd9cad8"
GEMINI = "48ea171d-928b-4509-a209-e7a6dd7392d1"
BINANCE = "a05e02d1-2789-49a3-aa83-1d3c9a442ea8"

keys_market_first = [
    # Binance
    EOS_BTC + BINANCE,
    XRP_BTC + BINANCE,
    # Bitfinex                           +
    BTC_USD + BITFINEX,
    LTC_USD + BITFINEX,
    ETH_USD + BITFINEX,
    XRP_USD + BITFINEX,
    EOS_USD + BITFINEX,
    EOS_BTC + BITFINEX,
    # Bitstamp                           +
    BTC_USD + BITSTAMP,
    LTC_USD + BITSTAMP,
    ETH_USD + BITSTAMP,
    XRP_USD + BITSTAMP,
    # Bittrex                            +
    XRP_USD + BITTREX,
    EOS_BTC + BITTREX,
    BTC_USD + BITTREX,
    LTC_USD + BITTREX,
    ETH_USD + BITTREX,
    # BTSE                               +
    BTC_USD + BTSE,
    LTC_USD + BTSE,
    ETH_USD + BTSE,
    # Coinbase Pro                       +
    BTC_USD + COINBASE_PRO,
    LTC_USD + COINBASE_PRO,
    ETH_USD + COINBASE_PRO,
    XRP_USD + COINBASE_PRO,
    EOS_USD + COINBASE_PRO,
    EOS_BTC + COINBASE_PRO,
    XRP_BTC + COINBASE_PRO,
    # Gemini                             +
    BTC_USD + GEMINI,
    LTC_USD + GEMINI,
    ETH_USD + GEMINI,
    # Kraken                             +
    BTC_USD + KRAKEN,
    LTC_USD + KRAKEN,
    ETH_USD + KRAKEN,
    XRP_USD + KRAKEN,
    EOS_USD + KRAKEN,
    EOS_BTC + KRAKEN,
]

keys_market_only = [
    BTC_USD,
    LTC_USD,
    ETH_USD,
    XRP_USD,
    EOS_USD,
    EOS_BTC,
    XRP_BTC
]

keys_market_string = [
    'EOSBTC',
    'XRPBTC',
    "tBTCUSD",
    "tLTCUSD",
    "tETHUSD",
    "tXRPUSD",
    "tEOSUSD",
    "tEOSBTC"
    'btcusd'
    'ltcusd',
    'ethusd',
    'xrpusd'
    'USD-XRP',
    'BTC-EOS',
    'USD-BTC',
    'USD-LTC',
    'USD-ETH',
    'BTC-USD_0',
    'LTC-USD_0',
    'ETH-USD_0',
    'BTC-USD',
    'LTC-USD',
    'ETH-USD',
    'XRP-USD',
    'EOS-USD',
    'EOS-BTC',
    'XRP-BTC',
    'BTCUSD'
    'LTCUSD',
    'ETHUSD',
    'XBT/USD',
    'LTC/USD',
    'ETH/USD',
    'XRP/USD',
    'EOS/USD',
    'EOS/XBT',
]

keys_exchange_first = [
    # Binance
    BINANCE + EOS_BTC,
    BINANCE + XRP_BTC,
    # Bitfinex
    BITFINEX + BTC_USD,
    BITFINEX + LTC_USD,
    BITFINEX + ETH_USD,
    BITFINEX + XRP_USD,
    BITFINEX + EOS_USD,
    BITFINEX + EOS_BTC,
    # Bitstamp
    BITSTAMP + BTC_USD,
    BITSTAMP + LTC_USD,
    BITSTAMP + ETH_USD,
    BITSTAMP + XRP_USD,
    # Bittrex
    BITTREX + XRP_USD,
    BITTREX + EOS_BTC,
    BITTREX + BTC_USD,
    BITTREX + LTC_USD,
    BITTREX + ETH_USD,
    # BTSE
    BTSE + BTC_USD,
    BTSE + LTC_USD,
    BTSE + ETH_USD,
    # Coinbase Pro
    COINBASE_PRO + BTC_USD,
    COINBASE_PRO + LTC_USD,
    COINBASE_PRO + ETH_USD,
    COINBASE_PRO + XRP_USD,
    COINBASE_PRO + EOS_USD,
    COINBASE_PRO + EOS_BTC,
    COINBASE_PRO + XRP_BTC,
    # Gemini
    GEMINI + BTC_USD,
    GEMINI + LTC_USD,
    GEMINI + ETH_USD,
    # Kraken
    KRAKEN + BTC_USD,
    KRAKEN + LTC_USD,
    KRAKEN + ETH_USD,
    KRAKEN + XRP_USD,
    KRAKEN + EOS_USD,
    KRAKEN + EOS_BTC,
]

keys_exchange_somehow = [
    # Coinbase
    'CB_' + BTC_USD,
    'CB_' + LTC_USD,
    'CB_' + ETH_USD,
    'CB_' + XRP_USD,
    'CB_' + EOS_USD,
    'CB_' + EOS_BTC,
    'CB_' + XRP_BTC,
    # Bitfinex
    'BF_' + BTC_USD,
    'BF_' + LTC_USD,
    'BF_' + ETH_USD,
    'BF_' + XRP_USD,
    'BF_' + EOS_USD,
    'BF_' + EOS_BTC,
]

shards = [
    Shard("shard1", 0, 42535295865117307932921825928971026431),
    Shard("shard2", 42535295865117307932921825928971026432, 85070591730234615865843651857942052863),
    Shard("shard3", 85070591730234615865843651857942052864, 127605887595351923798765477786913079295),
    Shard("shard4", 127605887595351923798765477786913079296, 170141183460469231731687303715884105727),
    Shard("shard5", 170141183460469231731687303715884105728, 212676479325586539664609129644855132159),
    Shard("shard6", 212676479325586539664609129644855132160, 255211775190703847597530955573826158591),
    Shard("shard7", 297747071055821155530452781502797185024, 340282366920938463463374607431768211455),
    Shard("shard8", 255211775190703847597530955573826158592, 297747071055821155530452781502797185023)
]

for x in keys_market_first:
    hashedKey = int(hashlib.md5(str(x).encode('utf-8')).hexdigest(), 16)
    for shard in shards:
        if shard.startingHash <= hashedKey <= shard.endingHash:
            shard.counter += 1
            print(x, '\t', hashedKey, '\t', shard.name)
            continue

for shard in shards:
    print(shard.name, ':', shard.counter)
