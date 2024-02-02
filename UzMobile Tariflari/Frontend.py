from pywebio.output import put_text, put_collapse, popup, put_button
from pywebio.input import input, input_group, checkbox
from pywebio.session import hold

from tariflar import tariflar, user_tarif_info
from Backend import get_tarifs, get_info, CheckPhoneNumber, isDigit, userData, turnTarif, checkUser, given_code


def intro_tarifs():
    """
    This function introduces tarifs
    """
    put_text("Salom👋. UzMobile Korxonansiga Xush Kelibsiz").style('font-size: 30px; text-align: center;')
    put_text(f"Bizda {get_tarifs(tariflar)[0]} mavjud tariflar. Ular: {', '.join(get_tarifs(tariflar)[1])}").style('font-size: 25px')

    tarifs = get_tarifs(tariflar)
    tarifs_info = get_info(tariflar)
    for tarif in range(tarifs[0]):
        with put_collapse(tarifs[1][tarif]):
            for j in range(len(tarifs_info[tarif])):
                put_text(tarifs_info[tarif][j])
                put_button("Tarifga o`tish", onclick = turnTarifBTN)

    put_text(user_tarif_info)


def turnTarifBTN():
    print(given_code)
    code = input("Sizga yuborilgan kodni yozing")
    if checkUser(code):
        popup(turnTarif())
    else:
        popup("Iltimos qayta urining")


def get_data():
    """
    This function gains information from user
    """
    data = input_group("O`zingizga qulay manba tanlang", [
        input("Ism, Familiya, Otangiz ismi", name = 'full_name'),
        input("Telefon raqamingiz", name = 'phone_number', validate = CheckPhoneNumber),
        input("Megabayt", name = 'mb', validate=  isDigit),
        input("SMS", name = 'sms', validate = isDigit),
        input("Minute", name = 'minute', validate = isDigit)
    ])

    data['platforms'] = get_platforms()
    put_button("Tarifga o`tish", onclick = turnTarifBTN())
    return data


def get_platforms():
    """
    The user might want to some platforms be unlimited
    """
    platforms = ['Telegram', 'Instagam', 'YouTube', 'TikTok', 'Twitter', 'Facebook', 'Likee', 'Imo', 'WhatsUp']
    selected_options = checkbox("Qaysi platformalarni cheksiz qilmoqchisiz", options=platforms)
    return selected_options


def getUserDataInfo():
    popup(userData(get_data()))
    hold()