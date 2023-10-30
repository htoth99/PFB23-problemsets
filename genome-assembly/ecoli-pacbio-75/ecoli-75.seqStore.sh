#!/bin/sh


#  Path to Canu.

bin="/Users/pfb11/problemsets/genome-assembly/canu-2.2/bin"

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which java`
echo "  " `java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_CLIENT_UA=
export CANU_OBJECT_STORE_CLIENT_DA=
export CANU_OBJECT_STORE_NAMESPACE=
export CANU_OBJECT_STORE_PROJECT=





/Users/pfb11/problemsets/genome-assembly/canu-2.2/bin/sqStoreCreate \
  -o ./ecoli-75.seqStore.BUILDING \
  -minlength 1000 \
  -genomesize 4800000 \
  -coverage   200 \
  -bias       0 \
  -raw -pacbio filtered_0.75 /Users/pfb11/problemsets/genome-assembly/filtered_0.75.fastq \
&& \
mv ./ecoli-75.seqStore.BUILDING ./ecoli-75.seqStore \
&& \
exit 0

exit 1
