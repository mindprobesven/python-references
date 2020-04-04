#!/usr/bin/env python3

def singleton(class_):
    class class_w(class_):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if class_w._instance is None:
                print('Creating ClassSingleton')
                class_w._instance = super(class_w, cls).__new__(cls)
                class_w._instance._sealed = False
            else:
                print("ClassSingleton exists. Returning instance.")

            return class_w._instance

        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True

    class_w.__name__ = class_.__name__
    return class_w
