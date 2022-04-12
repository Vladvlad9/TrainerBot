from sqlalchemy.future import select
from sqlalchemy.orm import Session

from utils.db_api.loader import engine
from utils.db_api.models import Users


class UsersCrud(object):

    @staticmethod
    def add_user(id_users: int, name: str, position) -> None:
        with Session(bind=engine) as session:
            session.add(
                Users(
                    id_users=id_users,
                    name=name,
                    positions=position
                )
            )
            session.commit()




