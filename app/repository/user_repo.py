from app.database.models.user import User
from app.repository.base_repo import BaseRepository
from app.core.dependencies import DBsession


class UserRepo(BaseRepository[User]):
    # def __init__(self, session: DBsession):
    #     return super().__init__(User, session)
    pass
