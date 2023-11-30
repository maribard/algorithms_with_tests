import requests


class DBClient:

    def get_total_amount_of_users(self):
        response = requests.get('https://reqres.in/api/users')

        return response.json()['total']

