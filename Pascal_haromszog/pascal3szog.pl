#!/usr/bin/perl

open(FILEID,">$ARGV[0]");
for ($k=0;$k<$ARGV[0];$k++) {
     $pascal[$k] = [];
     push @{$pascal[$k]},1;
     for ($l=1;$l<=$k;$l++) {
        push @{$pascal[$k]},$pascal[$k-1][$l-1]+$pascal[$k-1][$l];
        }
     }
foreach (@pascal) {
$n_els = @{$_};
        $nsp = 1 - 2 * $n_els;
        $form = (" " x $nsp).("%7d" x $n_els)."\n";
        printf FILEID $form, @{$_};
        }
close(FILEID);
