from app import db


class Task(db.Model):
    STATUS_WAIT = 1
    STATUS_EXECUTE = 2
    STATUS_COMPLETE = 2
    STATUS_CHOICES = (
        (STATUS_WAIT, 'En espera'),
        (STATUS_EXECUTE, 'Ejecutandose'),
        (STATUS_COMPLETE, 'Ejecutado')
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(64),
        index=True,
        unique=True
    )
    time = db.Column(
        db.Integer,
    )

    status = db.Column(
        db.SmallInteger,
        default=STATUS_WAIT
    )

    def __repr__(self):
        return '<Task %r>' % (self.name)