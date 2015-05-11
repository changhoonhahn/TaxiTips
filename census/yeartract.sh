hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduces=0 \
-file censusmap.py -mapper censusmap.py \
-input /Volumes/750GB/hahn/big_data/taxi/2013/TripFareTip/part-00000 \
-output /Volumes/750GB/hahn/big_data/taxi/2013/TripFareTipTract
