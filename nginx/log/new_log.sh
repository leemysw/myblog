#!/bin/sh

#tar -czPf /var/log/nginx/access.log-$(date +%Y%m%d%H).gz /var/log/nginx/access.log
/usr/bin/python /lee/nginx/log/nginx_log_ans.py
rm -f /lee/nginx/log/access.log
touch /lee/nginx/log/access.log
/usr/bin/docker exec -it lee_nginx_1 /bin/bash -c 'kill -USR1 $(cat /var/run/nginx.pid)'