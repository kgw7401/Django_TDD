from selenium import webdriver

browser = webdriver.Chrome(executable_path='D:\WebDev\chromedriver.exe')
browser.get('http://localhost:8000')

assert 'successfully' in browser.title