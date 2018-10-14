FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY myweb_nginx.conf /etc/nginx/sites-available/
COPY cert /etc/nginx/cert

RUN mkdir -p /etc/nginx/sites-enabled/\
#    && mkdir -p /etc/nginx/cert\
    && ln -s /etc/nginx/sites-available/myweb_nginx.conf /etc/nginx/sites-enabled/

# RUN mkdir -p /etc/nginx/sites-enabled/\
#     && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/\
#     && rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]