from locust import HttpLocust, TaskSet, task, constant, seq_task


class UserBehavior(TaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.headers = {}

    @seq_task(1)
    @task(1)
    def task1(self):
        self.client.get('/api/zones/by-slug/page-gpt-dat-pi-stress-test')

    @seq_task(1)
    @task(1)
    def task2(self):
        self.client.get('/api/exam-identifiers?rollNumber=XY0230300001&formNumber=890000001')

    @seq_task(3)
    @task(1)
    def login(self):
        data = {
            "slug": "for-stress-test",
            "zigged": False,
            "iphone": False
        }

        response = self.client.put('/api/tracks', json=data)

        if response.status_code == 200:
            self.headers = {'Authorization': response.json()['session']}
        else:
            print("Login request failed")

    @seq_task(4)
    @task(1)
    def task3(self):
        data = {
            "slug": "for-stress-test",
            "bandwidth": {},
            "progress": "Instructions",
            "zigged": False,
            "iphone": False
        }

        self.client.put('/api/tracks', json=data, headers=self.headers)

    @seq_task(5)
    @task(1)
    def task4(self):
        data = {
            "slug": "for-stress-test",
            "progress": "Capture",
            "zigged": False,
            "isMobile": False,
            "iphone": False
        }

        self.client.put('/api/tracks', json=data, headers=self.headers)

    @seq_task(6)
    @task(1)
    def task5(self):
        data = {
            "data": {
                "title": "Name",
                "salutation": False,
                "firstName": True,
                "middleName": False,
                "lastName": True
            },
            "value": {
                "firstName": "Pearl Academy",
                "lastName": ""
            },
            "type": "Name"
        }

        self.client.put('/api/tracks/capture/for-stress-test', json=data, headers=self.headers)

    @seq_task(7)
    @task(1)
    def task6(self):
        data = {
            "data": {
                "title": "Name",
                "salutation": False,
                "firstName": True,
                "middleName": False,
                "lastName": True
            },
            "value": {
                "firstName": "Pearl Academy",
                "lastName": "sadsad"
            },
            "type": "Name"
        }

        self.client.put('/api/tracks/capture/for-stress-test', json=data, headers=self.headers)

    @seq_task(8)
    @task(1)
    def task7(self):
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

        self.client.put('/api/tracks/capture/for-stress-test', json=data, headers=self.headers)

    @seq_task(9)
    @task(1)
    def task8(self):
        data = {
            "progress": "Questions",
            "isMobile": False,
            "slug": "for-stress-test",
            "zigged": False,
            "iphone": False
        }

        self.client.put('/api/tracks', json=data, headers=self.headers)

    @seq_task(10)
    @task(1)
    def task9(self):
        self.client.get('/api/tracks/questions/for-stress-test?zigged=false', headers=self.headers)

    @seq_task(11)
    @task(50)
    def task10(self):
        data = {
            "slug": "for-stress-test",
            "answer": {
                "question": "5e98010a13ae465161676291",
                "content": {
                    "value": "1234",
                    "time": 60
                },
                "isDirty": True
            },
            "zigged": False,
            "forceCalculation": True,
            "iphone": False
        }

        self.client.put('/api/tracks', json=data, headers=self.headers)

    @seq_task(12)
    def task11(self):
        data = {
            "slug": "for-stress-test",
            "progress": "Done",
            "zigged": False,
            "iphone": False
        }
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = constant(1)
