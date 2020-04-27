from locust import HttpLocust, TaskSequence, constant, seq_task, task


class UserBehavior(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.headers = {}

    @seq_task(1)
    def login(self):
        response = self.client.get('/api/tracks/description?slug=for-stress-test')
        if response.status_code == 200:
            self.headers = {
                'Authorization': response.json()['session']
            }
            print(response.json())
        else:
            print("Login request failed")

    # Dat Stress Test
    @seq_task(2)
    def task1(self):
        response = self.client.get('/api/tracks/header/gpt-stress-test', headers=self.headers)
        print(response.json())

    @seq_task(3)
    def task2(self):
        response = self.client.get('/api/tracks/description?slug=gpt-stress-test', headers=self.headers)
        print(response.json())

    @seq_task(4)
    def task3(self):
        data = {
            "slug": "gpt-stress-test",
            "user": {
                "zaccess": "test",
                "zpin": "test"
            },
            "zigged": False,
            "iphone": False
        }

        response = self.client.put('/api/tracks', json=data)
        print(response.json())

    @seq_task(5)
    def task4(self):
        with open('requirements.txt', 'rb') as binary:
            data = {
                'file': binary
            }

            response = self.client.post('/api/assets/upload/blob', files=data, headers=self.headers)
            print(response.json())

    # Failing: Getting Bad request error
    @seq_task(6)
    def task5(self):
        response = self.client.get('/api/assets/blob/11587973724676', headers=self.headers)
        print(response.json())

    # Failing: Getting Bad request error
    @seq_task(7)
    def task6(self):
        data = {
            "slug": "gpt-stress-test",
            "bandwidth": {},
            "progress": "Instructions",
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    # Failing: Getting Bad request error
    @seq_task(8)
    def task7(self):
        response = self.client.get('/api/tracks/instruction/gpt-stress-test?zigged=false',
                                   headers=self.headers)
        print(response.json())

    # Failing: Getting Bad request error
    @seq_task(9)
    def task8(self):
        data = {
            "slug": "dat-stress-test",
            "progress": "Capture",
            "zigged": False,
            "isMobile": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    # tested
    @seq_task(10)
    def task9(self):
        response = self.client.get('/api/tracks/capture/gpt-stress-test', headers=self.headers)
        print(response.json())

    @seq_task(11)
    def task10(self):
        data = {
            "data": {
                "title": "Name",
                "salutation": False,
                "firstName": True,
                "middleName": True,
                "lastName": True
            },
            "value": {
                "firstName": "test",
                "lastName": "test",
                "middleName": "test"
            },
            "type": "Name"
        }
        response = self.client.put('/api/tracks/capture/gpt-stress-test', json=data,
                                   headers=self.headers)
        print(response.json())

    @seq_task(12)
    def task11(self):
        data = {
            "data": {
                "title": "Email",
                "placeholder": "Email",
                "emailValidation": False,
                "unique": False
            },
            "value": {
                "data": "test@test.com"
            },
            "type": "Email"
        }

        response = self.client.put('/api/tracks/capture/gpt-stress-test', json=data,
                                   headers=self.headers)
        print(response.json())

    @seq_task(13)
    def task12(self):
        data = {
            "slug": "gpt-stress-test",
            "capture": [
                {
                    "type": "Name",
                    "value": {
                        "firstName": "test",
                        "lastName": "test",
                        "middleName": "test"
                    },
                    "data": {
                        "title": "Name",
                        "salutation": False,
                        "firstName": True,
                        "middleName": True,
                        "lastName": True
                    }
                },
                {
                    "type": "Email",
                    "value": {
                        "data": "test@test.com"
                    },
                    "data": {
                        "title": "Email",
                        "placeholder": "Email",
                        "emailValidation": False,
                        "unique": False
                    }
                }
            ],
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    @seq_task(14)
    def task13(self):
        data = {
            "progress": "Questions",
            "isMobile": False,
            "slug": "gpt-stress-test",
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    @seq_task(15)
    def task14(self):
        response = self.client.get('/api/tracks/questions/gpt-stress-test?zigged=false',
                                   headers=self.headers)
        print(response.json())

    @seq_task(16)
    def task15(self):
        response = self.client.get('/api/tracks/tag/5ea6b76ef7f8942cacb8c4b0', headers=self.headers)
        print(response.json())

    @seq_task(17)
    def task16(self):
        response = self.client.get('/api/tracks/questions/dat-stress-test?zigged=false',
                                   headers=self.headers)
        print(response.json())

    @seq_task(19)
    def task18(self):
        with open('requirements.txt', 'rb') as binary:
            data = {
                'file': binary
            }

            response = self.client.post('/api/assets/upload/blob', files=data, headers=self.headers)
            print(response.json())

    @seq_task(20)
    def task19(self):
        self.client.get('/api/assets/blob/21587973999102', headers=self.headers)

    @seq_task(21)
    @task(60)
    def task20(self):
        data = {
            "slug": "gpt-stress-test",
            "answer": {
                "question": "5ea433646c1ff75123cd2cb7",
                "content": 0,
                "isDirty": True
            },
            "zigged": False,
            "forceCalculation": True,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    @seq_task(22)
    def task21(self):
        data = {
            "slug": "gpt-stress-test",
            "progress": "Done",
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    @seq_task(23)
    def task22(self):
        with open('requirements.txt', 'rb') as binary:
            data = {
                'file': binary
            }

            response = self.client.post('/api/assets/upload/blob', files=data, headers=self.headers)
            print(response.json())


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = constant(1)
