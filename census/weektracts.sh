hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduces=1 \
-file tractweeksmap.py -mapper tractweeksmap.py \
-file tractweeksreduce.py -reducer tractweeksreduce.py \
-input /Volumes/750GB/hahn/big_data/taxi/2013/TripFareTip/test \
-output /Volumes/750GB/hahn/big_data/taxi/2013/WeekTipTract
