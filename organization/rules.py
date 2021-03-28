import rules

# Predicates
@rules.predicate
def is_staff(user):
    if user and user.is_staff:
        return True
    return False

@rules.predicate
def is_org_admin(user):
    if not user or not user.employee:
        return False
    return user.employee.is_org_admin

@rules.predicate
def is_ou_manager(user,orgunit):
    if not user or not user.employee:
        return False
    return orgunit.manager == user.employee

@rules.predicate
def is_employee_manager(employee, user):
    return user.is_staff | user.is_org_admin | employee.supervisor == user


# Rules

rules.add_rule('change_orgunit', is_staff|is_org_admin | is_ou_manager)
rules.add_rule('delete_orgunit', is_staff|is_org_admin)
rules.add_rule('create_orgunit', is_staff|is_org_admin)

# Permissions

rules.add_perm('organization.change_orgunit', is_staff|is_org_admin | is_ou_manager)
rules.add_perm('organization.delete_orgunit', is_staff|is_org_admin)