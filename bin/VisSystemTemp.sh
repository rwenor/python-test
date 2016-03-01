
for (( i = 1; i <= 1000; i++)) do
  cat /sys/class/thermal/thermal_zone0/temp 
  cat /sys/class/thermal/thermal_zone0/temp >> temp.dat
  sleep 1
done