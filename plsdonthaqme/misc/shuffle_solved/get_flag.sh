touch ascii.txt
for i in 593 $(seq 0 593)
do
  l=$(grep "::$i::" shuffle.txt)
  echo "$l" >>ascii.txt
done