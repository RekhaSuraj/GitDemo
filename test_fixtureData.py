import pytest
from pyTestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_Example2(self, dataLoad):
        log = self.get_logger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])


        # print(dataLoad[0])
        # print(dataLoad[2])
