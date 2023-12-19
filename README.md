On node0:

./server

On node1:

./client 10.1.1.1 100000

To measure interrupts within a 10s time window:

cat /proc/interrupts > interrupts1; sleep 10; cat /proc/interrupts > interrupts2;
python diff_interrupts.py interrupts1 interrupts2
