chmod +x map.py
chmod +x reduce.py

hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduce=1 \
    -file map.py -mapper map.py \
    -file reduce.py -reducer reduce.py \
    -input /Volumes/750GB/hahn/big_data/taxi/2012/*csv \
    -output /Volumes/750GB/hahn/big_data/taxi/2012/TripFareJoin
