#! /bin/bash
kill -9 `ps -ef |grep 'nginx_log_ans.py' |grep -v color | awk '{print $2}'` 
python /lee/nginx/log/nginx_log_ans.py & 
