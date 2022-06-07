set val(stop) 10.0
set ns [new Simulator]
set tracefile [open out.tr w]
$ns trace-all $tracefile
set namefile [open out.nam w]
$ns namtrace-all $namefile

set n0 [$ns node]
set n1 [$ns node]

$ns duplex-link $n0 $n1 100.0Mb 10ms DropTail
$ns queue-limit $n0 $n1 50

$ns duplex-link-op $n0 $n1 orient right

set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0

set sink1 [new Agent/TCPSink]
$ns attach-agent $n1 $sink1

$ns connect $tcp0 $sink1

$tcp0 set packetSize_ 1500

set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0

$ns at 1.0 "$ftp0 start"
$ns at 2.0 "$ftp0 stop"

proc finish {} {
	global ns tracefile namefile
	$ns flush-trace
	close $tracefile
	close $namefile
	exec nam out.nam &
	exit 0
}
$ns at $val(stop) "$ns nam-end-wireless $val(stop)"
$ns at $val(stop) "finish"
$ns run
