
python3 pumpDamon.py &
pumpProcess=$!
sudo motion on 
motionProcess=$!
cd ../../ 
sudo python3 manage.py runserver 10.0.1.6:8000 &
serverProcess=$!


echo $pumpProcess
echo $motionProcess
echo $serverProcess


