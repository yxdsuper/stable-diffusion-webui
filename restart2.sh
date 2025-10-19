process_name="launch.py"
if ps aux | grep $process_name | grep -v grep >/dev/null; then
	  echo "$process_name is running"
	    pid=$(ps aux | grep $process_name | grep -v grep | awk '{print $2}')
	      echo "Killing $process_name with PID $pid"
	        kill -9 $pid
	else
		  echo "$process_name is not running"
fi
echo "to start $process_name"
#cd /root/stable-diffusion-webui
COMMANDLINE_ARGS="--nowebui --api --medvram --always-batch-cond-uncond --xformers --port 6006" REQS_FILE="requirements.txt" nohup ./venv/bin/python $process_name 2>&1 >> sd_log.txt &
#COMMANDLINE_ARGS="--nowebui --api --medvram --always-batch-cond-uncond --xformers --port 6006" REQS_FILE="requirements.txt" ./venv/bin/python launch.py
