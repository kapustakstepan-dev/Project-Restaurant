import sys
import os

# Add the project path to sys.path to find online_restaurant_db
sys.path.append('/Users/stefkooo/Documents/GitHub/Project-Restaurant/ProyectRestourant/')

from ProyectRestourant.back.BD.online_restaurant_db import Users, engine
from sqlalchemy.orm import Session

def seed_admins():
    with Session(engine) as session:
        admins = [
            {
                "nickname": "superadmin",
                "email": "superadmin@gmail.com",
                "password": "super123"
            },
            {
                "nickname": "manager",
                "email": "manager@gmail.com",
                "password": "manager123"
            }
        ]

        print("Seeding Administrators...")
        for admin_data in admins:
            existing = session.query(Users).filter_by(nickname=admin_data['nickname']).first()
            if not existing:
                new_admin = Users(
                    nickname=admin_data['nickname'],
                    email=admin_data['email'],
                    role="admin"
                )
                new_admin.set_password(admin_data['password'])
                session.add(new_admin)
                print(f"Admin created:")
                print(f"email: {admin_data['email']}")
                print(f"password: {admin_data['password']}")
                print("-" * 20)
            else:
                print(f"Admin '{admin_data['nickname']}' already exists. Skipping.")

        session.commit()
        print("Seeding completed successfully!")

if __name__ == "__main__":
    seed_admins()
