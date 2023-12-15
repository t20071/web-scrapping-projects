from bs4 import BeautifulSoup

with open('home.html',"r") as html_file:
    content = html_file.read()
    print(content)

    soup = BeautifulSoup(content,"lxml")
    # print(soup.prettify())
    # tags = soup.find('h5')
    # tags = soup.findAll('h5')
    # for tag in tags:
    #     print(tag)
    course_cards = soup.findall('div',class_='card')
    for course in course_cards:
        print(course.h5.text)
        print(course.a.text)

