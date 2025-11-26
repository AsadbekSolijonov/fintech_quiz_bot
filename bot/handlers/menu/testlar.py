from typing import Union

from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from bot.keyboards.inline.category import builder_category
from bot.keyboards.inline.option import builder_quiz_options
from bot.keyboards.inline.quiz import builder_quizzes_state
from bot.keyboards.inline.subcategory import builder_subcategory
from bot.states.quiz import QuizState
from bot.utils.callbacks.call_data import CategoryData, SubcategoryData, Action, QuizData, UserAnswerData
from bot.utils.quiz.category import get_categories
from bot.utils.quiz.quizzes import get_quizzes
from bot.utils.quiz.subcategory import get_subcategories
from bot.utils.quiz.user import get_user
from aiogram.fsm.context import FSMContext

test_router = Router()


@test_router.message(F.text == 'Test')
@test_router.callback_query(SubcategoryData.filter(F.action == Action.back))
async def test_handler(msg: Union[Message, CallbackQuery]):
    categories = get_categories()
    if categories:
        ct_btns = builder_category(categories)
        if isinstance(msg, Message):
            await msg.answer("Savollar kategoriyasi.", reply_markup=ct_btns)
        elif isinstance(msg, CallbackQuery):
            await msg.message.edit_text("Savollar kategoriyasi.", reply_markup=ct_btns)
    else:
        if isinstance(msg, Message):
            await msg.edit_text("Savollar kategoriyasi mavjud emas!")
        elif isinstance(msg, CallbackQuery):
            await msg.message.edit_text("Savollar kategoriyasi mavjud emas!")


@test_router.callback_query(CategoryData.filter())
@test_router.callback_query(QuizData.filter(F.action == Action.back))
async def handler_category(call: CallbackQuery, callback_data: Union[CategoryData, SubcategoryData]):
    if isinstance(callback_data, QuizData):
        cat_id = callback_data.cat_id
        print(cat_id)
    elif isinstance(callback_data, CategoryData):
        cat_id = callback_data.id
    subcategories = get_subcategories(cat_id=cat_id)
    if subcategories:
        sb_btns = builder_subcategory(subcategories)
        await call.message.edit_text("Subkategoriyalar", reply_markup=sb_btns)
    else:
        await call.message.answer(text=f"Subcategoriyalar mavjud emas.")


@test_router.callback_query(SubcategoryData.filter(F.action == Action.view))
async def handler_subcategory(call: CallbackQuery, callback_data: SubcategoryData, state: FSMContext):
    cat_id = callback_data.cat_id
    sub_id = callback_data.id
    quizzes = get_quizzes(sub_id)
    if quizzes:
        await call.message.edit_text(f"Test {len(quizzes)} ta savoldan iborat",
                                     reply_markup=builder_quizzes_state(sub_id, cat_id))
        await state.set_state(QuizState.quiz)
    else:
        await call.message.edit_text(f"Bu bo'limda savollar yo'q")


@test_router.callback_query(QuizState.quiz, QuizData.filter(F.action == Action.start))
async def quiz_start(call: CallbackQuery, callback_data: QuizData, state: FSMContext):
    quizzes = get_quizzes(sub_id=callback_data.sub_id)
    idx = 0
    quiz = quizzes[0]
    text = quiz.text
    options = quiz.options
    btns = builder_quiz_options(options, quiz_index=idx)
    await call.message.edit_text(text=text, reply_markup=btns)


@test_router.callback_query(QuizState.quiz, UserAnswerData.filter())
async def option_filer(call: CallbackQuery, callback_data: UserAnswerData, state: FSMContext):
    user = get_user(chat_id=call.message.chat.id)
    if user:
        user_id = user.id
        quiz_id = callback_data.quiz_id
        option_id = callback_data.option_id
        # save_user_answer

    await call.message.answer(text=f"{callback_data.pack()}")
