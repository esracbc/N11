from locust import HttpLocust, TaskSet
import csv

def search(l):
	csvFile = csv.reader(open('test.csv'))
	for row in csvFile:
		for keyword in row:
			l.client.get('/arama?q=' + keyword)
	return


class UserBehavior(TaskSet):
    def on_start(self):
        search(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000