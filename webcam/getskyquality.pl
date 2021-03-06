#!/usr/bin/perl
#Filename: read-sqmle.pl
#Description: Utility to read Unihedron Sky Quality Meter-LE (Ethernet model)
# Define the required module
use IO::Socket;
# Open and configure serial port
$remote = IO::Socket::INET->new(
              PeerAddr => '142.1.110.13',
PeerPort => 10001, Proto => 'tcp');
# Send request to SQM
$remote->send("rx");
# Get response from SQM
$remote->recv($saw,255);
# Close the socket so that other programs can use the SQM
$remote->close;
# Print the SQM result to the screen
printf("%s", $saw);
my $filename = 'skyquality.log';
open(my $fh, '>>', $filename) or die "Could not open file '$filename' $!";
printf $fh ("%d, %s", time(), $saw);
close $fh;
system('echo "$(tail -1440 skyquality.log)" > skyquality.log');
system('tail -n 1 skyquality.log| awk -F, "{print \$1,\$3}" | sed \'s/m//g\' >> all_skyquality.log');
