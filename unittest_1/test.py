from calculator import Count

class TeseCount:

    def test_add(self):
        try:
            j = Count(2,3)
            add = j.add()
            assert(add == 5), 'integer addition result error!'
        except AssertionError as msg:
            print(msg)

        else:
            print('test pass!')

mytest =TeseCount()
mytest.test_add()