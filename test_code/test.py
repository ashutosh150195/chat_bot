# name = 'ashutosh kumar'
# print(name.split(' '))
# print(name[0])
# print(name.split(' ')[0])
# print(name.strip())
# print(name.strip(' '))


import bs4
import requests
import collections

report = collections.namedtuple('json','user_text')

#
# def remove_white_space(location):
#     if not location:
#         return location
#
#     return location.strip()


# def remove_space(text: str):
#     string = text.split('\n')
#     return string[0].strip()


def get_json(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)
    user_text = soup.find(id='test-client-query-input').find(class_='md-errors-spacer').
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    climate = soup.find(id='curCond').find(class_='wx-value').get_text()
    # print("before cleaning white space :"+location)
    #text = remove_white_space(location)

    # print("After cleaning white space :"+text)
    #string = remove_space(text)

    final_report = report(location_name=string, temperature_value=temp, scale=scale, condition=climate)
    return final_report


def start():
    area = input_weather_report()
    url = get_zipcode(area)
    html = get_html_page(url)
    weather_report = get_json(html)

    print(weather_report.location_name, weather_report.temperature_value, weather_report.scale,
          weather_report.condition)


def get_html_page(url):
    response = requests.get(url)
    return response.text


def input_weather_report():
    area = input('Register your location zipcode : ')
    return area


def get_url():
    url = "https://console.api.ai/api-client/#/agent/0290e0b9-b5ad-4f34-b089-512123e725b4/entities"
    return url


if __name__ == start():
    start()
