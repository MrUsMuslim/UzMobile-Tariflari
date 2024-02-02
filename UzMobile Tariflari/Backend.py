import re
from math import ceil
from random import randint


def get_tarifs(tarifs):
    """
    This function returns length and names of tarifs
    """

    return [len(tarifs), [name for name in tarifs.keys()]]


def get_info(tarifs):
    """
    This function returns informations about tarifs (list)
    """
    
    return [tarif for tarif in tarifs.values()]


def CheckPhoneNumber(phone_number):
    """
    Checks if the phone number matchs
    """
    pattern = r'^[\+]{1}998 99 [0-9]{3} [0-9]{4}$'

    if not re.match(pattern, phone_number):
        return 'Telefon raqamni shu ko`rinishda kirgizing: +998 99 xxx xxxx'


def isDigit(number):
    """
    Checks if the number is not foat or string
    """
    if not number.isdigit():
        return "Butun son kiriting!"
    if int(number) < 0:
        return "Musbat son kiriting!"


def calculateMB(mb):
    """
    This function calculates the avarage price of mb.
    You can find it in tarifs module (user_tarif_info)
    """
    mb = int(mb)
    sum = 0

    if mb > 10000:
        sum = 0.5
    if mb <= 10000:
        sum = 0.8
    if mb <= 5000:
        sum = 0.9
    if mb <= 1500:
        sum = 10
    
    return sum * mb


def calculateSMS(sms):
    """
    This function calculates the avarage price of sms.
    You can find it in tarifs module (user_tarif_info)
    """
    sms = int(sms)
    sum = 0

    if sms > 500:
        sum = 10
    if sms <= 500:
        sum = 15
    if sms <= 100:
        sum = 20
    
    return sum * sms


def calculateMinute(minute):
    """
    This function calculates the avarage price of minute.
    You can find it in tarifs module (user_tarif_info)
    """
    minute = int(minute)
    sum = 0

    if minute > 1000:
        sum = 10
    if minute <= 1000:
        sum = 20
    if minute <= 500:
        sum = 50
    
    return sum * minute


def calculatePlatform(list):
    """
    Calculates the price of platforms
    """
    return len(list) * 4000


def calculateAll(data):
    """
    Calculates the finanl price
    """

    minute = data['minute']
    sms = data['sms']
    mb = data['mb']
    platforms = data['platforms']

    sum = ceil(calculateMinute(minute) + calculateMB(mb) + calculateSMS(sms)) + calculatePlatform(platforms)
    return sum


def giveDiscount(summa):
    """
    This function gives discount based on price.
    You can find it in tarifs module (user_tarif_info)
    """
    discount = 0

    if summa > 100_000:
        discount = 8000
        summa -= discount

    if summa <= 80_000:
        discount = 6500
        summa -= discount

    if summa <= 60_000:
        discount = 5000
        summa -= discount
    
    if summa <= 40_000:
        discount = 2000
        summa -= discount

    return summa, discount


def turnTarif():
    """
    Returns tarif`s info
    """
    return 'Sizning tarifingiz o`zgartirildi.'


def userData(data):
    """
    The funcion returns information about user`s tarif
    """
    full_name = data['full_name']
    summa = giveDiscount(calculateAll(data))

    text = f"Siz {full_name} {calculateAll(data)} sum tarif yig`dingiz.\n"
    text += f"Siz uchun umumiy hisobda {summa[1]} sum chegirma.\n"
    text += f"Sizning tarif rejangiz:\n"
    text += f"Megabayt {data['mb']}, SMS {data['sms']}, Minute {data['minute']}"

    return text


# The funcion is called not only in Backend but also in Frontend. so the code will different from each other
given_code = randint(1000, 10000)
def checkUser(code):
    """
    Checks if the user is not bot
    """
    if int(code) == given_code:
        return True
    else:
        return False