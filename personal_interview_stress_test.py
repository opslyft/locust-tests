from locust import HttpLocust, TaskSequence, constant, seq_task


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

    # Personal Interview Page
    @seq_task(2)
    def task1(self):
        response = self.client.get('/api/tracks/header/personal-interview-stress-test', headers=self.headers)
        print(response.json())

    @seq_task(3)
    def task2(self):
        response = self.client.get('/api/tracks/description?slug=personal-interview-stress-test', headers=self.headers)
        print(response.json())

    @seq_task(4)
    def task3(self):
        data = {
            "slug": "personal-interview-stress-test",
            "user": {
                "zaccess": "test",
                "zpin": "test"
            },
            "zigged": False,
            "iphone": False
        }

        response = self.client.put('/api/tracks', json=data, headers=self.headers)
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
            "slug": "personal-interview-stress-test",
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
        response = self.client.get('/api/tracks/instruction/personal-interview-stress-test?zigged=false',
                                   headers=self.headers)
        print(response.json())

    # Failing: Getting Bad request error
    @seq_task(9)
    def task8(self):
        data = {
            "slug": "personal-interview-stress-test",
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
        response = self.client.get('/api/tracks/capture/personal-interview-stress-test', headers=self.headers)
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
        response = self.client.put('/api/tracks/capture/personal-interview-stress-test', json=data,
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

        response = self.client.put('/api/tracks/capture/personal-interview-stress-test', json=data,
                                   headers=self.headers)
        print(response.json())

    @seq_task(13)
    def task12(self):
        data = {
            "slug": "personal-interview-stress-test",
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
            "slug": "personal-interview-stress-test",
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())

    @seq_task(15)
    def task14(self):
        response = self.client.get('/api/tracks/questions/personal-interview-stress-test?zigged=false',
                                   headers=self.headers)
        print(response.json())

    @seq_task(16)
    def task15(self):
        response = self.client.get('/api/tracks/tag/5ea68e5c05ea4b3391ef6398', headers=self.headers)
        print(response.json())

    @seq_task(17)
    def task16(self):
        response = self.client.get('/api/tracks/instruction/personal-interview-stress-test?zigged=false',
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
    def task20(self):
        data = {
            "slug": "personal-interview-stress-test",
            "answer": {
                "question": "5ea433026c1ff75123cd2ca7",
                "content": {
                    "url": "https://video.talent.social/00c29670-885d-11ea-a9d3-6dbfc7bc21d4.webm",
                    "thumbnail": None
                },
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
            "slug": "personal-interview-stress-test",
            "progress": "Done",
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = constant(1)
