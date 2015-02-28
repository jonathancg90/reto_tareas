from app import db
from app import app
from app import models
import time
from threading import Thread


def print_queue_size():
    try:
        while True:
            tasks = models.Task.query.filter(models.Task.status != models.Task.STATUS_COMPLETE).all()
            for task in tasks:
                task.status = models.Task.STATUS_EXECUTE
                db.session.commit()
                app.logger.debug("Execute Task: %s" % (task.name))
                time.sleep(task.time)
                task.status = models.Task.STATUS_COMPLETE
                db.session.commit()
            time.sleep(1)
    except:
        app.logger.debug("Exception thread")

t = Thread(target=print_queue_size, args=())
t.setDaemon(True)
t.start()