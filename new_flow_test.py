from locust import HttpLocust, TaskSequence, TaskSet, constant, seq_task, task

class UserBehavior(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.headers = {}

    @seq_task(1)
    def login(self):
        data = {
            "slug": "stress-test-flow",
            "zigged": False,
            "iphone": False
            }
        
        response = self.client.put('/api/zig-tracks', json=data)
        
        if response.status_code == 200:
            self.headers = {'Authorization': response.json()['session']}
        else:
            print("Login request failed")

    @seq_task(2)
    def task1(self):
        print('1111')
        data = {
            "slug": "stress-test-flow",
            "iphone": False
        }
        response = self.client.put('/api/zig-tracks', json=data, headers=self.headers)
        print(response.json())
    
    @seq_task(3)
    def task2(self):
        print('2222')
        response = self.client.get('/api/zig-tracks/instruction/stress-test-flow', headers=self.headers)
        print(response.json())
    
    @seq_task(4)
    def task3(self):
        print('3333')
        data = {
            "slug": "stress-test-flow",
            "progress": "Capture",
            "iphone": False
        }

        response = self.client.put('/api/zig-tracks', json=data, headers=self.headers)
        print(response)
    
    @seq_task(5)
    def task4(self):
        print('4444')
        data = {
            "data": {
                "title": "Name",
                "salutation": False,
                "firstName": True,
                "middleName": False,
                "lastName": True
            },
            "value": {
                "firstName": "Aayush",
                "lastName": ""
            },
            "type": "Name"
        }

        response = self.client.put('/api/zig-tracks/capture/stress-test-flow', json=data, headers=self.headers)
        print(response)

    @seq_task(6)
    def task5(self):
        print('5555')
        data = {
            "data": {
                "title": "Name",
                "salutation": False,
                "firstName": True,
                "middleName": False,
                "lastName": True
            },
            "value": {
                "firstName": "Aayush",
                "lastName": "Kumar"
            },
            "type": "Name"
        }

        response = self.client.put('/api/zig-tracks/capture/stress-test-flow', json=data, headers=self.headers)
        print(response)

    @seq_task(7)
    def task6(self):
        print('6666')
        data = {
            "data": {
                "title": "Name",
                "salutation": False,
                "firstName": True,
                "middleName": False,
                "lastName": True
            },
            "value": {
                "firstName": "Aayush",
                "lastName": "Kumar"
            },
            "type": "Name"
        }

        response = self.client.put('/api/zig-tracks/capture/stress-test-flow', json=data, headers=self.headers)
        print(response)
    
    @seq_task(8)
    def task7(self):
        print('7777')
        data = {
            "data": {
                "title": "Email",
                "placeholder": "Email",
                "emailValidation": False,
                "unique": False
            },
            "value": {
                "data": "aayush@opslyft.com"
            },
            "type": "Email"
        }

        response = self.client.put('/api/zig-tracks/capture/stress-test-flow', json=data, headers=self.headers)
        print(response)
    
    @seq_task(9)
    def task8(self):
        print('8888')
        data = {
            "slug": "stress-test-flow",
            "capture": [
                {
                    "type": "Name",
                    "value": {
                        "firstName": "Aayush",
                        "lastName": "Kumar"
                },
                "data": {
                    "title": "Name",
                    "salutation": False,
                    "firstName": True,
                    "middleName": False,
                    "lastName": True
                    }
                },
                {
                    "type": "Email",
                    "value": {
                        "data": "aayush@opslyft.com"
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

        response = self.client.put('/api/zig-tracks', json=data, headers=self.headers)
        print(response.json())

    @seq_task(10)
    def task9(self):
        print('9999')
        response = self.client.get('/api/zig-tracks/tracks/stress-test-flow', headers=self.headers)
        print(response.json())
    
    @seq_task(11)
    def task10(self):
        print('10 10 10 10')
        response = self.client.get('/api/tracks/header/stress-test-essay', headers=self.headers)
        print(response.json())
    
    @seq_task(12)
    def task11(self):
        print('11 11 11 11')
        response = self.client.get('/api/zig-tracks/tracks/stress-test-flow', headers=self.headers)
        print(response.json())
    
    @seq_task(13)
    def task12(self):
        print('12 12 12 12')
        data = {
            "slug": "stress-test-essay",
            "zigIdentifier": "4556f3d0-8b37-11ea-ad1d-330a9a281998",
            "zigged": True,
            "iphone": False
        }
        
        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())
    
    @seq_task(14)
    def task13(self):
        print('13 13 13 13')
        data = {
            "slug": "stress-test-essay",
            "progress": "Questions",
            "zigged": True,
            "isMobile": False,
            "iphone": False
        }

        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())
    
    @seq_task(15)
    def task14(self):
        print('14 14 14 14')
        response = self.client.get('/api/tracks/questions/stress-test-essay?zigged=true', headers=self.headers)
        print(response.json())
    
    @seq_task(16)
    def task15(self):
        print('15 15 15 15')
        data = {
            "slug": "stress-test-essay",
            "answer": {
                "question": "5eab25a73677615a6d5f2885",
                "content": 0,
                "isDirty": True
            },
            "zigged": True,
            "forceCalculation": True,
            "iphone": False
        }

        response = self.client.put('/api/tracks', json=data, headers=self.headers)
        print(response.json())
    
    @seq_task(17)
    def task16(self):
        print('16 16 16 16')
        data = {
            "slug": "stress-test-flow",
            "progress": "Done",
            "iphone": False
        }

        response = self.client.put('/api/zig-tracks', json=data, headers=self.headers)
        print(response.json())

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = constant(1)
