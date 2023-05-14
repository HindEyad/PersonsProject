FROM nginx

COPY ui.html /usr/share/nginx/html/

RUN echo 'server { \
    listen 4000; \
    server_name localhost; \
    location / { \
    root /usr/share/nginx/html; \
    index ui.html; \
    } \
    }' > /etc/nginx/conf.d/default.conf

EXPOSE 4000

CMD ["nginx", "-g", "daemon off;"]
