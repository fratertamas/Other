#!/usr/bin/perl

$i=0;
if ( @ARGV >= "2" ){
	print "Tul sok parameter! \n";
}else{
	if ( @ARGV == "" ) {
	print "Nincs megadva parameter! \n";
}else{
	foreach( @ARGV ) {
	$parameter = @ARGV[$i];
$fakt=1;
	for ( $j=1; $j<=$parameter; $j++ ){
	$fakt=$fakt*$j;
	}
@tomb2;
for ( $k=1; $k<=$fakt; $k++){
	for ( $z=1; $z<=$parameter; $z++ ){
	push(@tomb,$z);	
	@tomb2=@tomb;
	}
	print "$k. sor: @tomb";
	print "\n";
	@tomb=();
}
	$i++;
};};}