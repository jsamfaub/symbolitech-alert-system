import json

class SuccessRateController:

    def __init__(self, file_name):
        self.load_file_data(file_name)
        self._file_name=file_name

    def load_file_data(self, file_name):
        with open(file_name, 'r') as file:
            try:
                data = json.load(file)
                if (not "number_of_success" in data) or (not "number_of_success" in data) or (not "number_of_success" in data):
                    raise Exception("The file {} is not formatted correctly".format(file_name))
            except Exception as e:
                print(e)
                data = {
                    "number_of_success":0,
                    "number_of_error":0,
                    "success_rate":0,
                }
        self._data=data
    def add_error(self):
        self._data['number_of_error']+=1

    def add_success(self):
        self._data['number_of_success']+=1

    def get_number_of_success(self):
        return self._data['number_of_success']

    def get_number_of_error(self):
        return self._data['number_of_error']

    def __del__(self):
        num_of_error=self.get_number_of_error()
        num_of_success=self.get_number_of_success()
        success_rate=format(num_of_success/(num_of_error+num_of_success), '.5f')
        data={
            "number_of_success":num_of_success,
            "number_of_error":num_of_error,
            "success_rate":success_rate
        }
        if self._file_name:
            with open(self._file_name, 'w') as file:
                json.dump(data, file)

class UrlStatusController:

    def __init__(self, file_name):
        self.load_file_data(file_name)
        self._file_name=file_name

    def load_file_data(self, file_name):
        with open(file_name, 'r') as file:
            try:
                status_data = json.load(file)
            except Exception as e:
                print(e)
                status_data = {}
        self._status_data=status_data

    def set_current_status_for_url(self, url, status_code):
        status_code=int(status_code)
        changed=False
        if url in self._status_data:
            if self._status_data[url] != status_code:
                changed=True
        self._status_data[url]=status_code
        return changed

    def __del__(self):
        if self._file_name and self._status_data:
            with open(self._file_name, 'w') as file:
                json.dump(self._status_data, file)
