from aiogram.filters.callback_data import CallbackData


class CategoryData(CallbackData, prefix='cat'):  # "cat:1"
    id: int


class SubcategoryData(CallbackData, prefix='sub'):  # "sub:1"
    id: int


if __name__ == '__main__':
    calldata = CategoryData(id=1)
    print(calldata.pack())
