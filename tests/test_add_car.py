import os.path

from data.car_data import create_car
from pages.add_car_page import AddCarPage

PHOTO_PATH = os.path.join(
    os.path.dirname(__file__),"..","resources","images","bugatti_veyron.jpg"
)


def test_add_car_success(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path = PHOTO_PATH)

    car_work_page.open_car_form()
    car_work_page.fill_car_form(car)
    car_work_page.submit_car()

    car_work_page.open_car_form()
    car_work_page.fill_car_form(car)
    car_work_page.submit_car()

    assert car_work_page.error_message_text()=="Failed to submit car"