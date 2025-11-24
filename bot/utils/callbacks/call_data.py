from enum import Enum

from aiogram.filters.callback_data import CallbackData


class Action(str, Enum):
    view = 'view'
    back = 'back'
    start = 'start'


class CategoryData(CallbackData, prefix='cat'):  # "cat:1"
    id: int


class SubcategoryData(CallbackData, prefix='sub'):  # "sub:action:1"
    action: Action
    id: int
    cat_id: int


class QuizData(CallbackData, prefix='quiz'):  # "quiz:action:1"
    action: Action
    id: int
    sub_id: int
    cat_id: int


# davomi bor.

if __name__ == '__main__':
    calldata = CategoryData(id=1)
    sub_calldata = SubcategoryData(action=Action.view, id=3, cat_id=1)
    print(sub_calldata.pack())
