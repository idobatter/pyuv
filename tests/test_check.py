
import common
import unittest

import pyuv


class CheckTest(common.UVTestCase):

    def test_check1(self):
        self.check_cb_called = 0
        def check_cb(check, data):
            self.check_cb_called += 1
            check.stop()
            check.close()
        self.timer_cb_called = 0
        def timer_cb(timer):
            self.timer_cb_called += 1
            timer.stop()
            timer.close()
        loop = pyuv.Loop.default_loop()
        check = pyuv.Check(loop)
        check.start(check_cb)
        timer = pyuv.Timer(loop)
        timer.start(timer_cb, 1, 0)
        loop.run()
        self.assertEqual(self.check_cb_called, 1)


if __name__ == '__main__':
    unittest.main()
