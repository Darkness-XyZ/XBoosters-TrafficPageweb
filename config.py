# Configuration settings for proxy lists, analytics, and scheduling

# Proxy configuration
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

# Analytics settings
analytics = {
    'enabled': True,
    'tracking_id': 'UA-XXXXX-Y'
}

# Scheduling settings
schedule = {
    'cron_job': '0 * * * *',  # Runs every hour
    'timezone': 'UTC'
}