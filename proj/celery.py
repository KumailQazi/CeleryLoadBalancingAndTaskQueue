# Setting up celery to support application and library

from __future__ import absolute_import, unicode_literals
from celery import Celery

# Creating a celery instance
app = Celery('proj', broker='amqp://', backend='amqp://', include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.conf.update(
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)

# Starting the App
if __name__ == '__main__':
    app.start(
        app.config_from_object('celeryconfig')
    )
