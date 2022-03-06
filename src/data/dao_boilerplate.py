from data.base import Session, getsession

class BaseDao:
    def __init__(self, cls):
        self.cls = cls
    
    def get_all(self):
        """ Retrieve all instances of the base class 
            from the database 
        """
        with getsession(expunge_all=True) as session:
            return session.query(self.cls).all()

    def add(self, *instances):
        """ Persist passed instances in the database """
        with getsession() as session:
            for instance in instances:
                session.add(instance)