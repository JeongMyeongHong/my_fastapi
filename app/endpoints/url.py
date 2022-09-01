from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.detector import DetectorService
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, DETECT


class Url:
    def router(self, menu):
        if menu == LOGIN:
            UserService().login(
                input('id'),
                input('password'))
        elif menu == CALCULATOR:
            CalculatorService().calculate(
                int(input('첫번째 값 입력: ')),
                int(input('두번째 값 입력: ')))
        elif menu == DETECT:
            #data/tmc/test.jpg
            DetectorService().detect(input('이미지 주소 입력: '))

