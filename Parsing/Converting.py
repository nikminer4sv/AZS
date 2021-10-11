from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import os

driver = webdriver.Chrome('./chromedriver')
driver.get("https://snipp.ru/tools/address-coord")

data_file = open('data.txt', 'r')
output_file = open('data2.0.txt', 'a')

coords = ''
counter = 494

for line in data_file:

	counter += 1

	temp = line[:len(line) - 1]

	line = line.split('] [')[1]
	adress = line[0:len(line) - 2]

	input_field = driver.find_element_by_class_name('ymaps-b-form-input__input')
	input_field.send_keys(adress)
	input_field.send_keys(Keys.ENTER)

	time.sleep(1)

	driver.find_element_by_id('ypoint-copy').click()
	if (coords == pyperclip.paste()):
		#print("Error")
		output_file.write(temp + ' [Error]\n')
	else:
		coords = pyperclip.paste()
		output_file.write(temp + ' [' + coords + ']\n')
		#print(coords)


	clear_button = driver.find_element_by_class_name('ymaps-b-form-input__clear')
	clear_button.click()

	os.system('cls||clear')

	print('[' + str(counter) + '/839]')

	time.sleep(1)


"""
data_file = open('data.txt', 'r')
line = data_file.readline().split('] [')[1]
adress = line[0:len(line) - 2]
#data_file.close()


driver = webdriver.Chrome('./chromedriver')
driver.get("https://snipp.ru/tools/address-coord")

input_field = driver.find_element_by_class_name('ymaps-b-form-input__input')
input_field.send_keys(adress)
input_field.send_keys(Keys.ENTER)

time.sleep(1)

driver.find_element_by_id('ypoint-copy').click()
print(pyperclip.paste())
"""




'''data_file = open('data.txt', 'r')

line = data_file.readline().split('] [')[1]
adress = line[0:len(line) - 2]
line = data_file.readline().split('] [')[1]
adress = line[0:len(line) - 2]
line = data_file.readline().split('] [')[1]
adress = line[0:len(line) - 2]

print(adress)

'''