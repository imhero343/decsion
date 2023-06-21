

bind = '0.0.0.0:8000'  # IP address and port to bind Gunicorn
workers = 3  # Number of worker processes
timeout = 120  # Timeout for worker processes
keepalive = 5  # Number of seconds to keep an idle connection open

# Logging
accesslog = '-'  # '-' to log to stdout
errorlog = '-'  # '-' to log to stdout
loglevel = 'info'  # Logging level ('debug', 'info', 'warning', 'error', 'critical')

# Process naming
proc_name = 'my_project_gunicorn'  # Process name prefix

# Server mechanics
preload_app = True  # Preload application code before forking worker processes
