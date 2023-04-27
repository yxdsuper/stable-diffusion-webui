process_name="launch.py"
if ps aux | grep $process_name | grep -v grep >/dev/null; then
	  echo "$process_name is running"
	    pid=$(ps aux | grep $process_name | grep -v grep | awk '{print $2}')
	      echo "Killing $process_name with PID $pid"
	        kill -9 $pid
	else
		  echo "$process_name is not running"
fi
