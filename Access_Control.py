class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions  # list of allowed resources

    def has_access(self, resource):
        return resource in self.permissions


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def access_resource(self, resource):
        if self.role.has_access(resource):
            print(f"{self.username} ({self.role.name}) has access to '{resource}'")
        else:
            print(f"{self.username} ({self.role.name}) does NOT have access to '{resource}'")


#defining the resources
resources = {
    "dashboard": "Admin Panel",
    "employee_data": "Employee Records",
    "public_info": "Public Information"
}

# יצירת תפקידים והרשאות
admin_role = Role("Admin", permissions=["dashboard", "employee_data", "public_info"])
employee_role = Role("Employee", permissions=["employee_data", "public_info"])
guest_role = Role("Guest", permissions=["public_info"])

# יצירת משתמשים
admin_user = User("Alice", admin_role)
employee_user = User("Bob", employee_role)
guest_user = User("Charlie", guest_role)

# בדיקות גישה
users = [admin_user, employee_user, guest_user]
resources_to_check = ["dashboard", "employee_data", "public_info"]

for user in users:
    for res in resources_to_check:
        user.access_resource(res)
    print("\n")
