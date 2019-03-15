pidfile = '/run/gunicorn/cursopython.pid'
bind = [ '0.0.0.0:5000', ]
user = 'http'
group = 'http'
capture_output = True
accesslog = '/var/log/gunicorn/cursopython.access.log'
errorlog = '/var/log/gunicorn/cursopython.error.log'

# raw_env = [
    # 'CACAHUATE_SETTINGS=/home/innovacion/apps/cacahuate_tracsa/'
    # 'settings_production.py',
# ]

worker_class = 'eventlet'
workers = 3 # número de núcleos del servidor * 2 + 1
