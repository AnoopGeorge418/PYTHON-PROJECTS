from bs4 import BeautifulSoup

with open('././index.html', 'r') as file:
    contents = file.read()
    
    # fetching all the contents
    soup = BeautifulSoup(contents, 'lxml')
    
    # getting all the course names and its prices.
    course_cards = soup.find_all('div', class_ = 'card')
    for card in course_cards:
        courses_name = card.h4.text
        course_price = card.button.text.split()[-1]
        
        print(f'{courses_name}: {course_price}')