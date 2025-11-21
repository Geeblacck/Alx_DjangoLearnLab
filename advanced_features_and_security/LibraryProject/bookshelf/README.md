# Permissions and Groups Setup

## Groups:
- Admins: can_view, can_create, can_edit, can_delete
- Editors: can_view, can_create, can_edit
- Viewers: can_view

## Usage:
- Assign users to groups via Django Admin or programmatically.
- Views are protected using `@permission_required('myapp.permission_codename')`.
- Custom permissions are defined in `models.py` under `Meta.permissions`.
