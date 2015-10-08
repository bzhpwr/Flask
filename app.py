workers = 2 
bind = 'unix:medi_hs2.sock'
backlog = 2048
umask = 002
application = 'medi_hs:app'

#access-logfile = '/var/log/nginx/access_gunicorn2.log'
#error-logfile = '/var/log/nginx/error_unicorn2.log'
