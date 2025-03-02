from moduly_packages_imports.Accounting.application.db.people import get_employees
from moduly_packages_imports.Accounting.application.salary import calculate_salary
from datetime import datetime
import requests

if __name__ == '__main__':
    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    calculate_salary()
    get_employees()

    response = requests.get('https://api.github.com')
    print(response.status_code)
