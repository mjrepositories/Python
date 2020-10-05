# MAERSK

browser.get('https://www.maersk.com/schedules/')

start = browser.find_element_by_xpath('//*[@id="originLocation"]')
start.send_keys('rotterdam')
start.send_keys(u'\ue004')
end = browser.find_element_by_xpath('//*[@id="destinationLocation"]')
end.send_keys('buenos aires')
end-send_keys(u'\ue004')
button=browser.find_element_by_id('searchSchedulesByPoint2Point')
button.click()
days = browser.find_element_by_xpath('//*[@id="shipmentResults"]/div[1]/div[1]/div/dl[4]/dd[3]')
x = days.text
y = x.find(" ")
no_of_days = x[:y]

start.clear()
end.clear()


# CMA

browser.get('https://www.cma-cgm.com/ebusiness/schedules')

origin = browser.find_element_by_xpath('//*[@id="AutoCompletePOL"]')
origin.send_keys('rotterdam')
origin.send_keys(u'\ue004')

end = browser.find_element_by_xpath('//*[@id="AutoCompletePOD"]')
end.send_keys('buenos aires')
end-send_keys(u'\ue004')

button = browser.find_element_by_xpath('//*[@id="wrapper"]/div/form/p/button')
button.click()
days = browser.find_element_by_xpath('')
x = days.text
y = x.find(" ")
no_of_days = x[:y]

start.clear()
end.clear()

# Cosco

browser.get("https://elines.coscoshipping.com/ebusiness/sailingSchedule/searchByCity")

start = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[1]/div[1]/div/div/div/div[2]/div/div[1]/input')
start.send_keys('new york')
selection = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/ul[2]/div/li[2]')
selection.click()
end = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[2]/div[1]/div/div/div/div[2]/div/div[1]/input')
end.send_keys('rotterdam')
selection_end = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[2]/div[1]/div/div/div/div[2]/div/div[2]/ul[2]/div/li[1]')
selection_end.click()
button = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[5]/div/div')
button.click()

days = browser.find_element_by_xpath('//*[@id="capture"]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/span')
x = days.text
y = x.find(" ")
no_of_days = x[:y]

start.clear()
end.clear()
