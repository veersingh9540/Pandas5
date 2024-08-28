import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['Department'] = None
    for j in department['id']:
        for i in range(len(employee)):
            if employee['departmentId'][i] == j :
                employee['Department'][i] = department['name'][(department['id'] == j)]
    
    DF = employee.groupby('departmentId').apply(
        lambda x: x[x['salary'] == x['salary'].max()]
    ).sort_values(by=['id'])
    return DF[['Department', 'name', 'salary']].rename(columns = {
        'name': 'Employee',
        'salary': 'Salary'
            })