from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.options import courses_default
from keyboards.inline import go
from keyboards.inline.courses import courses_inline
from keyboards.inline.go import go_inline
from keyboards.inline.math import math_inline
from loader import dp, bot
from states.opinion import OpinionState
from states.phtone_state import PhoneState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=courses_default)


@dp.message_handler(text="📁Kurslar")
async def send_courses(message: types.Message):
    await message.answer("Biz ushbu fanlardan yuqori malakali ustozlar va sifatli materiallarga egamiz: ",
                         reply_markup=courses_inline)


@dp.callback_query_handler(text="27.secret.matematika")
async def math(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        "Ustozimiz Sardorxon Ufronxonov boshchiligadi jamoa Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
        reply_markup=math_inline)


@dp.callback_query_handler(text="27.secret.kimyo")
async def math(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        "Ustozimiz Kimyo fanlari doctori boshchiligadi jamoa Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
        reply_markup=math_inline)


@dp.callback_query_handler(text="27.secret.matematika")
async def math(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        "Ustozimiz Sardorxon Ufronxonov boshchiligadi jamoa Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
        reply_markup=math_inline)


@dp.callback_query_handler(text="27.secret.go.math.course")
async def mathCourse(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Telefon raqamingizni kiriting, adminlar siz bilan bog'lanishadi")
    await PhoneState.math.set()


@dp.callback_query_handler(text="27.secret.go.chemistry.course")
async def mathCourse(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Telefon raqamingizni kiriting, adminlar siz bilan bog'lanishadi")
    await PhoneState.chemistry.set()


@dp.message_handler(state=PhoneState.math)
async def mathPhoneState(message: types.Message, state: FSMContext):
    await message.answer("Ma'lumotlaringiz adminga yuborildi, siz bilan tez orada bog'lanishadi. ")
    await bot.send_message("1038753516",
                           f"username: @{message.from_user.username}\nfullname: {message.from_user.full_name}\ntel: {message.text}\nkurs: Matematika", )
    await state.finish()


@dp.message_handler(state=PhoneState.chemistry)
async def mathPhoneState(message: types.Message, state: FSMContext):
    await message.answer("Ma'lumotlaringiz adminga yuborildi, siz bilan tez orada bog'lanishadi. ")
    await bot.send_message("1038753516",
                           f"username: @{message.from_user.username}\nfullname: {message.from_user.full_name}\ntel: {message.text}\nkurs: Kimyo", )
    await state.finish()


@dp.message_handler(text="ℹ️Taklif & Shikoyatlar")
async def contacts(message: types.Message):
    await message.answer(
        "Fikrlaringizni yozib qoldiring, sizning fikringiz shaxsan ceo ga jo'natiladi"
    )
    await OpinionState.writing.set()


@dp.message_handler(state=OpinionState.writing)
async def send_ceo(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message("1038753516",
                           f"username: @{message.from_user.username}\nfullname: {message.from_user.full_name}\nfikr: <b>{message.text}</b>\n")


@dp.message_handler(text="📞Kontaktlar")
async def contacts(message: types.Message):
    await message.answer(
        "Grand Edu o'quv markazi <b>Minor Metro</b>si yonida, <b>Qozoqiston mehmonxona</b>si binosida joylashgan\n<i>Telefon raqamlarimiz</i>: \n📞<b>(99) 033 09-19</b>\n📞<b>(99) 937 07-07</b>",
        reply_markup=go_inline
    )


@dp.message_handler(text="📝Kursga yozilish")
async def contacts(message: types.Message):
    await message.answer(
        "O'zingizga ma'qul kursni tanlang",
        reply_markup=courses_inline
    )
