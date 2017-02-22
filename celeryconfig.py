from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    "poll_SO": {
        "task": "feed_scraper.feeds",
        "schedule": timedelta(seconds=30),
        "args": []
    }
}
