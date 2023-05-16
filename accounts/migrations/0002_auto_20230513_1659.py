# Generated by Django 4.2.1 on 2023-05-13 16:59

from django.db import migrations

def populate_departments(apps, shcemaeditor):
    entries = {
        "Veterinary": "Animal health",
        "Zookeeper": "Feeding and cleaning"
    }
    Department = apps.get_model("accounts", "Department")
    for key, value in entries.items():
        dept = Department(name=key, description=value)
        dept.save()

def populate_roles(apps, schemaeditor):
    entries = {
        "Veterinary": ("Responsible for animal health"),
        "Zookeeper": ("Responsible for feeding and cleaning "
                    "animals and habitats")
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role = Role(name=key, description=value)
        role.save()



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_departments),
        migrations.RunPython(populate_roles),
    ]
