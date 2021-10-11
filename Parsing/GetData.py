from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

AZS_NAME = 'Белоруснефть'

AZS_DICTIONARY = {
	1 : 'A-100',
	2 : 'Белоруснефть',
	3 : 'Блок',
	4 : 'Веста',
	5 : 'Газпромнефть',
	6 : 'Лукойл',
	7 : 'Роснефть',
	8 : 'Татнефть',
	9 : 'Трайпл',
	10 : 'Гомельтранснефть "Дружба"',
	11 : 'United Company',
	12 : 'Модуль АЗС'
}

NUMBER_OF_AZS = 12;

driver = webdriver.Chrome('./chromedriver')
driver.get("https://zaprauka.by/map/")

filter_button = driver.find_element_by_xpath('//*[@id="map_filter-form"]/div/div[3]')
filter_button.click()

output_file = open("data.txt", "a")

for x in range(NUMBER_OF_AZS):

	if (x > 0):
		previous_filter_option_button = driver.find_element_by_xpath('//*[@id="map_filter-form"]/div/div[3]/div[2]/ul/li[' + str(x) + ']/label')
		previous_filter_option_button.click()

	time.sleep(2)

	filter_option_button = driver.find_element_by_xpath('//*[@id="map_filter-form"]/div/div[3]/div[2]/ul/li[' + str(x+1) + ']/label')
	filter_option_button.click()

	time.sleep(3)

	while (True):
		try:
			button = driver.find_element_by_class_name('gas_station_more_button')
			if (button.is_displayed() == True):
				button.click()
			time.sleep(3)	
		except:
			break;

	azs = driver.find_elements_by_class_name('modal__adr')

	for j in azs:
		output_file.write('[' + AZS_DICTIONARY.get(x + 1) + '] [' + j.find_element_by_tag_name('p').get_attribute('innerHTML') + ']\n')

	print('[' + str(x + 1) + '/' + str(NUMBER_OF_AZS) + '] ' + AZS_DICTIONARY.get(x + 1) + ' was written.')
