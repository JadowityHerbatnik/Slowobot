from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import szukacz
import nauka
import time



#browser = webdriver.Firefox()
lista = []


def wejdzdogry(login, haslo, browser):
    url = 'http://slowotok.pl/play'
    browser.get(url)
    username = browser.find_element_by_name("Email")
    password = browser.find_element_by_name("Password")

    username.send_keys(login)
    password.send_keys(haslo)
    button = browser.find_element_by_xpath('/html/body/div[3]/div/form/div[7]/input')
    button.click()


def getczas(browser):
    czass = browser.find_element_by_css_selector('#time')
    return czass.text


def getstan(browser):
    zegaropis = browser.find_elements_by_xpath('//*[@id="time_desc"]')
    druk = []
    druk.append(zegaropis[0].text)
    return druk


def fetch(browser):
    lista.clear()
    for a in range(16):
        lokalizacja = '//*[@id="' + str(a) + '"]'
        pierw = browser.find_element_by_xpath(lokalizacja)
        lista.append(pierw.text)


def loka(numer):
    numer = numer
    string = '''//*[@id="''' + str(numer) + '''"]'''
    return string


def zaznacz(wykonaj, browser):
    for a in wykonaj:
        try:
            ActionChains(browser).click_and_hold(browser.find_element_by_xpath(loka(a[0]))).perform()
            for x in range(len(a) - 1):
                ActionChains(browser).move_to_element(browser.find_element_by_xpath(loka(a[x + 1]))).perform()
                if x == (len(a) - 2):
                    ActionChains(browser).release(browser.find_element_by_xpath(loka(a[x + 1]))).perform()
            if (getstan(browser)[0] == "WYNIKI ZA:"):
                break
        except Exception as e:
            print(e)
            break


def konwertnasek(czas):
    sekundy = (int(czas[2:])) + ((int(czas[0])) * 60)
    return sekundy


def startgry(browser):
    print("startgry()")
    fetch(browser)
    wykonaj = szukacz.konwerstujnaslowa(lista)
    return wykonaj


def zbierzslowa(browser):
    tabela = browser.find_elements_by_xpath('//*[@id="words"]')
    tabeladruk = []
    for t in tabela:
        tabeladruk.append(t.text)
    return tabeladruk


def granapunkty(training, browser):
    while True:
        stan = getstan(browser)
        if stan[0] == "DO KOŃCA:":
            time.sleep(0.3)
            wykonaj = startgry(browser)
            if training == False:
                zaznacz(wykonaj, browser)

            czas2 = getczas(browser)

            time.sleep(konwertnasek(czas2) + 4)
            czyjuzsawyniki = getstan(browser)
            while czyjuzsawyniki[0] != "WYNIKI ZA:":
                time.sleep(1)
                czyjuzsawyniki = getstan(browser)
            else:
                tabeladruk = zbierzslowa(browser)
            nauka.nauka(tabeladruk, wykonaj, lista)

        else:
            czas = getczas(browser)
            ile = int(czas[2:]) + 1
            print("czekamy", ile, "sekund na gre")
            time.sleep(ile)

def start(training, login, haslo):
    browser = webdriver.Firefox()
    wejdzdogry(login, haslo, browser)
    granapunkty(training, browser)
