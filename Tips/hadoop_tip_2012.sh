chmod +x tip_map.py
chmod +x tip_reduce.py

hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduce=1 \
    -file tip_map.py -mapper tip_map.py \
    -file tip_reduce.py -reducer tip_reduce.py \
    -input /Volumes/750GB/hahn/big_data/taxi/2012/TripFareJoin/part-00000 \
    -output /Volumes/750GB/hahn/big_data/taxi/2012/TripFareTip/
