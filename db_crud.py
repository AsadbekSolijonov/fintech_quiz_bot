# query
from sqlalchemy import select
from db.models import User
from db.session import get_session


def get_all_users():
    with get_session() as db:
        query = select(User)
        users = db.execute(query).scalars().all()
        return users


def get_first_user():
    with get_session() as db:
        query = select(User)
        user = db.execute(query).scalar()
        return user


def filter_user(chat_id: int):
    with get_session() as db:
        query = select(User).where(chat_id == User.chat_id)
        user = db.execute(query).scalar_one()
        return user


def update_user(chat_id: int):
    with get_session() as db:
        query = select(User).where(chat_id == User.chat_id)
        user = db.execute(query).scalar_one()
        user.fullname = 'Muhammadayub'
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


def delete_user(chat_id: int):
    with get_session() as db:
        query = select(User).where(chat_id == User.chat_id)
        user = db.execute(query).scalar_one()
        db.delete(user)
        db.commit()
        return user




def init_querys():
    # [x] all users
    # users = get_all_users()
    # for user in users:
    #     print(user.fullname)

    # [x] first user
    # user = get_first_user()
    # print(user)

    # [x] filter user
    # user = filter_user(chat_id=5342739186)
    # print(user)

    # [x] update user
    # user = update_user(chat_id=5342739186)
    # print(user)

    # [x] update user
    # user = delete_user(chat_id=5342739186)
    # print(user)

    pass


if __name__ == '__main__':
    init_querys()
