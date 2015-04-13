import remoteFinder

amazonAddress = '54.5.211.146'
amazonPort = 5001

finder = remoteFinder(amazonAddress,amazonPort)
finder.connectToAwsServer()
finder.uploadAddress()
remoteAddress = finder.getRemoteAddress()
finder.closeConnection()
finder.