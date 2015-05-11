chmod +x map_crd_nozero.py
chmod +x reduce_month.py

hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduce=1 \
    -file map_crd_nozero.py -mapper map_crd_nozero.py \
    -file reduce_month.py -reducer reduce_month.py \
    -input /Volumes/750GB/hahn/big_data/taxi/2013/TripFareTip/part-00000 \
    -output /Volumes/750GB/hahn/big_data/taxi/2013/CreditTipMonthsNoZero/

#hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduce=1 \
#    -file map_crd.py -mapper map_crd.py \
#    -file reduce_month.py -reducer reduce_month.py \
#    -input /Volumes/750GB/hahn/big_data/taxi/2012/TripFareTip/part-00000 \
#    -output /Volumes/750GB/hahn/big_data/taxi/2012/CreditTipMonths/
#
#hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduce=1 \
#    -file map_crd.py -mapper map_crd.py \
#    -file reduce_month.py -reducer reduce_month.py \
#    -input /Volumes/750GB/hahn/big_data/taxi/2011/TripFareTip/part-00000 \
#    -output /Volumes/750GB/hahn/big_data/taxi/2011/CreditTipMonths/
