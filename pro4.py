class DataProvider:
        def __init__(self):
            self._internal_value = 50

        def get_value(self):
            return self._internal_value

        def set_value(self, new_value):
            self._internal_value = new_value

class DataConsumer:
        def __init__(self, provider):
            self.provider = provider

        def display_data(self):
            value = self.provider.get_value()
            print(f"Value from provider: {value}")

provider_obj = DataProvider()
consumer_obj = DataConsumer(provider_obj)
consumer_obj.display_data()