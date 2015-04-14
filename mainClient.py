__author__ = 'Stephen'

import remoteFinder

client = remoteFinder.RemoteFinder('client', '127.0.0.1', 5001)
client.uploadLocalAddressToAWS()
