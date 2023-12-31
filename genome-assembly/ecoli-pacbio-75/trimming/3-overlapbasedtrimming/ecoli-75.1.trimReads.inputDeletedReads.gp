set title 'inputDeletedReads'
set xlabel 'length, bin width = 250'
set ylabel 'number'

binwidth=250
set boxwidth binwidth
bin(x,width) = width*floor(x/width) + binwidth/2.0

set terminal png size 1024,1024
set output './ecoli-75.1.trimReads.inputDeletedReads.png'
plot [] [0:] './ecoli-75.1.trimReads.inputDeletedReads.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes title ''
