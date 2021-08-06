Getting realtime stock data from API and storing it in HDFS using Python and FLUME

step 1) Get your own api key from www.alphavantage.co and we can get our own key by giving some basic information

step 2) write a python script for getting data from api and the python file name is Stocks_api.py

step3) configure flume config file

    agent1.sources = tail
    agent1.channels = Channel-2
    agent1.sinks = sink-1
    agent1.sources.tail.type = exec
    agent1.sources.tail.command = python3 /home/ayur/HadoopProgram/ApacheFlume/Stock_data/Stocks_api.py
    agent1.sources.tail.channels = Channel-2

    agent1.sinks.sink-1.channel = Channel-2
    agent1.sinks.sink-1.type = hdfs
    agent1.sinks.sink-1.hdfs.path = hdfs://localhost:9000//flume-practice
    agent1.sinks.sink-1.hdfs.fileType = DataStream
    agent1.sinks.sink-1.hdfs.rollInterval = 60
    agent1.sinks.sink-1.hdfs.rollSize = 0
    agent1.sinks.sink-1.hdfs.rollCount = 0

    agent1.channels.Channel-2.type = memory
    agent1.channels.Channel-2.keep-alive = 60 
    agent1.channels.Channel-2.transactionCapacity = 1000 
    agent1.channels.Channel-2.capacity = 1000000 

Here we are setting our source as exec and our agent is agent1.
Our channel name is channel-2 and our sink is sink-1
Then we are setting our command as our python file and we set our hdfs path.

step 4) run flume agent command to get this data
> bin/flume-ng agent –conf ./conf/ -f conf/stocklive.conf -n agent1 -Dflume.root.logger=DEBUG


