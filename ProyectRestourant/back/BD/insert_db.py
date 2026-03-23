from sqlalchemy.orm import Session
from online_restaurant_db import Users, engine, Menu

with Session(engine) as session:
    dishes = [
        Menu(
            name="Arcade Nachos",
            weight="300",
            ingredients="Corn Tortilla Chips, Nacho Cheese Sauce, Pickled Jalapeños, Fresh Salsa, Sour Cream",
            description="Loaded corn chips with jalapeños, melted cheese, and salsa.",
            price=10.99,
            active=True,
            file_name="nachos.jpg"
        ),
        Menu(
            name="Chicken Wrap",
            weight="300",
            ingredients="Grilled Chicken, Flour Tortilla, Mixed Greens, Tomatoes, Garlic Sauce",
            description="Tender grilled chicken with fresh veggies and garlic yogurt sauce.",
            price=11.50,
            active=True,
            file_name="wrap.jpg"
        ),
        Menu(
            name="Crispy Fries",
            weight="200",
            ingredients="Crinkle-cut Potatoes, Vegetable Oil, Retro Salt Blend, Paprika, Garlic Powder",
            description="Crispy crinkle-cut fries seasoned with our special retro spice blend.",
            price=4.99,
            active=True,
            file_name="fries.jpg"
        ),
        Menu(
            name="Vintage Milkshake",
            weight="400",
            ingredients="Whole Milk, Vanilla Ice Cream, Fresh Strawberries, Whipped Cream, Maraschino Cherry",
            description="Thick vanilla strawberry shake topped with whipped cream and a cherry.",
            price=6.50,
            active=True,
            file_name="milkshake.jpg"
        ),
        Menu(
            name="Classic Pizza",
            weight="250",
            ingredients="Pizza Dough, Tomato Sauce, Mozzarella Cheese, Premium Pepperoni, Italian Herbs",
            description="Cheesy pepperoni slice baked in our classic brick oven.",
            price=14.99,
            active=True,
            file_name="pizza.jpg"
        ),
        Menu(
            name="Retro Burger",
            weight="450",
            ingredients="Beef Patty (x2), Cheddar Cheese, Lettuce & Tomato, Secret Sauce, Brioche Bun",
            description="Classic double patty with melted cheese, lettuce, and secret diner sauce.",
            price=12.99,
            active=True,
            file_name="burger.jpg"
        )
    ]

    session.add_all(dishes)
    existing_admin = session.query(Users).filter_by(nickname="admin").first()

    if not existing_admin:
        admin = Users(
            nickname="admin",
            email="adminjaj@gmail.com",
            role="admin"
        )
        admin.set_password("qwerty1233")
        session.add(admin)
        print("Admin creado")
    else:
        print("Admin ya existe")
    
    session.commit()

print("Меню успішно додано!")