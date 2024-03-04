class Employee:
    def __init__(self, id: int, importance: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id: int) -> int:
        # Create a dictionary to map employee IDs to their Employee objects
        employee_dict = {employee.id: employee for employee in employees}
        
        # Define the DFS function
        def dfs(employee_id):
            # Base case: if the employee has no subordinates, return their importance
            if not employee_dict[employee_id].subordinates:
                return employee_dict[employee_id].importance
            # Recursive case: sum the importance of the employee and their subordinates
            else:
                total_importance = employee_dict[employee_id].importance
                for subordinate_id in employee_dict[employee_id].subordinates:
                    total_importance += dfs(subordinate_id)
                return total_importance
        
        # Calculate the total importance of the given employee
        return dfs(id)
