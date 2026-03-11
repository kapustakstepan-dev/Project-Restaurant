const translations = {
    en: {
        nav_home: "Home",
        nav_menu: "Menu",
        nav_login: "Login",
        nav_register: "Register",
        nav_orders: "My Orders",
        nav_reserved: "Reservation",
        hero_title: "Welcome to RetroBite",
        hero_subtitle: "Taste the nostalgic flavors of the past, served with a modern twist.",
        hero_cta: "View Menu",
        menu_title: "Food From The Past",
        add_to_cart: "Add to Cart",
        order_now: "Order Now",
        login_title: "Welcome Back",
        login_btn: "Login",
        register_title: "Join the Club",
        register_btn: "Register",
        email_label: "Email Address",
        password_label: "Password",
        name_label: "Full Name",
        invoice_title: "RetroBite Receipt",
        invoice_send: "Send to Email",
        close: "Close",
        orders_title: "My Orders",
        total: "Total",
        reservation_title: "Table Reservation",
        desc_burger: "Classic double patty with melted cheese, lettuce, and secret diner sauce.",
        desc_fries: "Crispy crinkle-cut fries seasoned with our special retro spice blend.",
        desc_milkshake: "Thick vanilla strawberry shake topped with whipped cream and a cherry.",
        desc_pancakes: "Fluffy buttermilk stack with melting butter and maple syrup.",
        desc_pizza: "Cheesy pepperoni slice baked in our classic brick oven.",
        desc_nachos: "Loaded corn chips with jalapeños, melted cheese, and salsa.",
        desc_ramen: "Rich broth with noodles, soft egg, and classic toppings.",
        desc_sundae: "Three scoops of nostalgia with fudge and sprinkles."
    },
    es: {
        nav_home: "Inicio",
        nav_menu: "Menú",
        nav_login: "Iniciar sesión",
        nav_register: "Registrarse",
        nav_orders: "Mis pedidos",
        nav_reserved: "Reservar mesa",
        hero_title: "Bienvenido a RetroBite",
        hero_subtitle: "Prueba los sabores nostálgicos del pasado, servidos con un toque moderno.",
        hero_cta: "Ver Menú",
        menu_title: "Comida del Pasado",
        add_to_cart: "Añadir al carrito",
        order_now: "Pedir Ahora",
        login_title: "Bienvenido de nuevo",
        login_btn: "Iniciar sesión",
        register_title: "Únete al Club",
        register_btn: "Registrarse",
        email_label: "Correo electrónico",
        password_label: "Contraseña",
        name_label: "Nombre completo",
        invoice_title: "Recibo de RetroBite",
        invoice_send: "Enviar por correo",
        close: "Cerrar",
        orders_title: "Mis pedidos",
        total: "Total",
        reservation_title: "Reserva de mesa",
        desc_burger: "Doble hamburguesa clásica con queso derretido, lechuga y salsa secreta.",
        desc_fries: "Papas fritas crujientes sazonadas con nuestra mezcla especial retro.",
        desc_milkshake: "Batido espeso de vainilla y fresa con crema batida y cereza.",
        desc_pancakes: "Pancakes esponjosos con mantequilla derretida y miel de maple.",
        desc_pizza: "Porción de pizza con queso y pepperoni horneada estilo clásico.",
        desc_nachos: "Nachos cargados con jalapeños, queso derretido y salsa.",
        desc_ramen: "Caldo rico con fideos, huevo tierno y toppings clásicos.",
        desc_sundae: "Tres bolas de nostalgia con chocolate y chispas."
    },
    ua: {
        nav_home: "Головна",
        nav_menu: "Меню",
        nav_login: "Увійти",
        nav_register: "Реєстрація",
        nav_orders: "Мої замовлення",
        nav_reserved: "Бронювання столика",
        hero_title: "Ласкаво просимо до RetroBite",
        hero_subtitle: "Скуштуйте ностальгічні смаки минулого у сучасному виконанні.",
        hero_cta: "Переглянути меню",
        menu_title: "Їжа з минулого",
        add_to_cart: "Додати в кошик",
        order_now: "Замовити зараз",
        login_title: "З поверненням",
        login_btn: "Увійти",
        register_title: "Приєднуйся до клубу",
        register_btn: "Реєстрація",
        email_label: "Електронна пошта",
        password_label: "Пароль",
        name_label: "Повне ім'я",
        invoice_title: "Чек RetroBite",
        invoice_send: "Відправити на email",
        close: "Закрити",
        orders_title: "Мої замовлення",
        total: "Всього",
        reservation_title: "Бронювання столика",
        desc_burger: "Класична подвійна котлета з сиром, салатом та секретним соусом.",
        desc_fries: "Хрустка картопля фрі з нашими фірмовими ретро спеціями.",
        desc_milkshake: "Густий ванільно-полуничний шейк зі збитими вершками та вишнею.",
        desc_pancakes: "Пухкі млинці з маслом та кленовим сиропом.",
        desc_pizza: "Шматочок піци з пепероні, випеченої у класичній печі.",
        desc_nachos: "Кукурудзяні чипси з халапеньйо, сиром та сальсою.",
        desc_ramen: "Насичений бульйон з локшиною, яйцем та класичними додатками.",
        desc_sundae: "Три кульки ностальгії з шоколадом та посипкою."
    }
};

class Translator {
    constructor() {
        this.currentLang = localStorage.getItem('language') || 'en';
        this.elements = document.querySelectorAll('[data-i18n]');

        this.init();
    }

    init() {
        this.updateDOM();
        this.setupButtons();
    }

    setLanguage(lang) {
        if (translations[lang]) {
            this.currentLang = lang;
            localStorage.setItem('language', lang);
            this.updateDOM();
            this.updateActiveButton();
        }
    }

    updateDOM() {
        this.elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[this.currentLang][key]) {
                if (el.tagName === 'INPUT' && el.hasAttribute('placeholder')) {
                    el.setAttribute('placeholder', translations[this.currentLang][key]);
                } else {
                    el.textContent = translations[this.currentLang][key];
                }
            }
        });
    }

    setupButtons() {
        const btns = document.querySelectorAll('.lang-btn');
        btns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.setLanguage(e.target.dataset.lang);
            });
        });
        this.updateActiveButton();
    }

    updateActiveButton() {
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.lang === this.currentLang);
        });
    }
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    window.translator = new Translator();
});
