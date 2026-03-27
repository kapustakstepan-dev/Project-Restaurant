const translations = {
    en: {
        nav_home: "Home", nav_menu: "Menu", nav_login: "Login", nav_register: "Register", nav_orders: "My Orders", nav_reserved: "Reservation", nav_logout: "Logout", nav_admin: "Admin",
        hero_title: "Welcome to RetroBite", hero_subtitle: "Taste the nostalgic flavors of the past, served with a modern twist.", hero_cta: "View Menu",
        menu_title: "Food From The Past", add_to_cart: "Add to Cart", order_now: "Order Now",
        login_title: "Welcome Back", login_btn: "Login", register_title: "Join the Club", register_btn: "Register",
        username_label: "Username", email_label: "Email", password_label: "Password", name_label: "Full Name",
        invoice_title: "RetroBite Receipt", invoice_send: "Send to Email", close: "Close",
        orders_title: "My Orders", my_orders_title: "My Orders", orders_empty: "No active orders found.", recent_orders_title: "Recent Orders",
        total: "Total", res_title: "Book a Table", res_subtitle: "Experience nostalgic dining at its best. Secure your spot today!",
        res_success: "Reservation submitted successfully! See you soon.", label_name: "Name", label_email: "Email", label_phone: "Phone", label_guests: "Guests",
        label_date: "Date", label_time: "Time", label_table_type: "Table Type", table_regular: "Regular Table", table_booth: "Cozy Booth", table_window: "Window Seat", table_outdoor: "Outdoor Terrace",
        btn_reserve: "Confirm Reservation", btn_reserve_more: "Book More Tables", btn_delete: "Delete", confirm_delete_res: "Are you sure you want to delete this reservation?",
        order_id: "Order #", status_delivered: "Delivered", status_preparing: "Preparing", status_onway: "On the Way", weight_label: "Weight", ingredients_label: "Ingredients",
        description_label: "Description:", back_to_menu: "Back to Menu", checkout_title: "Checkout", btn_confirm_order: "Confirm & Order", empty_basket_checkout: "Your basket is empty.",
        add_more_items: "Add more items &larr;", login_footer: "Don't have an account? ", register_footer: "Already have an account? ", login_link: "Login", register_link: "Register",
        error_404_subtitle: "Page Not Found", error_404_description1: "It seems you've lost yourself in time.", error_404_description2: "Return to the present for the best retro flavor!", error_404_btn: "BACK TO HOME",
        my_reservations_title: "My Reservations", no_active_reservations: "You have no active reservations.", go_to_reserve: "Go to reservations", recent_orders: "Recent Orders",
        no_recent_orders: "You have no recent orders.",
        admin_menu_crud: "Menu CRUD", admin_global_orders: "Global Orders", admin_reservations: "Reservations", admin_users: "Users", admin_exit: "Exit Admin",
        admin_gest_menu: "Menu Management", admin_add_plate: "+ Add Item", admin_img: "IMG", admin_name: "Name", admin_price: "Price", admin_status: "Status", admin_actions: "Actions",
        admin_active: "Active", admin_inactive: "Inactive", admin_edit: "Edit", admin_delete: "Delete", admin_new_plate: "New Item", admin_desc: "Description", admin_img_file: "Image (filename)",
        admin_add: "Add", admin_close: "Close", admin_ref: "Ref", admin_client: "Client", admin_total: "Total", admin_date: "Date", admin_action: "Action", admin_user: "User",
        admin_nickname: "Nickname", admin_role: "Role", admin_save: "Save Changes", admin_cancel: "Cancel", admin_active_menu: "Active in menu?",
        err_past_date: "Error: You cannot reserve a table for a past date.", label_id: "ID", view_details: "View Details &rarr;", checkout_btn: "Place Order Now",
        current_basket: "Current Basket", quantity_label: "Quantity", explore_menu: "Explore Menu", empty_basket: "Your basket is currently empty.",
        receipt_order_id: "Order #", receipt_total: "Total:", receipt_date: "Date:", receipt_items: "Items:", receipt_thanks: "Thank you for your visit!", receipt_keep_retro: "Keep it Retro.",
        item_burger: "Retro Burger", item_pizza: "Classic Pizza", item_wrap: "Chicken Wrap", item_fries: "Crispy Fries", item_shake: "Vintage Milkshake", item_nachos: "Arcade Nachos",
        desc_burger: "Classic double patty with melted cheese, lettuce, and secret diner sauce.", desc_fries: "Crispy crinkle-cut fries seasoned with our special retro spice blend.",
        desc_milkshake: "Thick vanilla strawberry shake topped with whipped cream and a cherry.", desc_pancakes: "Fluffy buttermilk stack with melting butter and maple syrup.",
        desc_pizza: "Cheesy pepperoni slice baked in our classic brick oven.", desc_nachos: "Loaded corn chips with jalapeños, melted cheese, and salsa.",
        desc_wrap: "Tender grilled chicken with fresh veggies and garlic yogurt sauce.", desc_ramen: "Rich broth with noodles, soft egg, and classic toppings.", desc_sundae: "Three scoops of nostalgia with fudge and sprinkles."
    },
    es: {
        nav_home: "Inicio", nav_menu: "Menú", nav_login: "Iniciar sesión", nav_register: "Registrarse", nav_orders: "Pedidos", nav_reserved: "Reserva", nav_logout: "Cerrar sesión", nav_admin: "Admin",
        hero_title: "Bienvenido a RetroBite", hero_subtitle: "Prueba los sabores nostálgicos del pasado, servidos con un toque moderno.", hero_cta: "Ver Menú",
        menu_title: "Comida del Pasado", add_to_cart: "Añadir al carrito", order_now: "Pedir Ahora",
        login_title: "Bienvenido de nuevo", login_btn: "Entrar", register_title: "Únete al Club", register_btn: "Regístrate",
        username_label: "Usuario", email_label: "Correo", password_label: "Contraseña", name_label: "Nombre completo",
        invoice_title: "Recibo de RetroBite", invoice_send: "Enviar por correo", close: "Cerrar",
        orders_title: "Mis Pedidos", my_orders_title: "Mis Pedidos", orders_empty: "No tienes pedidos activos.", recent_orders_title: "Pedidos Recientes",
        total: "Total", res_title: "Reservar Mesa", res_subtitle: "Vive una experiencia gastronómica nostálgica. ¡Asegura tu lugar hoy!",
        res_success: "¡Reserva enviada con éxito! Nos vemos pronto.", label_name: "Nombre", label_email: "Correo", label_phone: "Teléfono", label_guests: "Personas",
        label_date: "Fecha", label_time: "Hora", label_table_type: "Tipo de Mesa", table_regular: "Mesa Regular", table_booth: "Box Acogedor", table_window: "Mesa de Ventana", table_outdoor: "Terraza",
        btn_reserve: "Confirmar Reserva", btn_reserve_more: "Reservar más", btn_delete: "Eliminar", confirm_delete_res: "¿Estás seguro de que quieres eliminar esta reserva?",
        order_id: "Pedido #", status_delivered: "Entregado", status_preparing: "Preparando", status_onway: "En camino", weight_label: "Peso", ingredients_label: "Ingredientes",
        description_label: "Descripción:", back_to_menu: "Volver al Menú", checkout_title: "Finalizar Compra", btn_confirm_order: "Confirmar Pedido", empty_basket_checkout: "Tu cesta está vacía.",
        add_more_items: "Añadir más productos", login_footer: "¿No tienes una cuenta? ", register_footer: "¿Ya tienes una cuenta? ", login_link: "Entrar", register_link: "Regístrate",
        error_404_subtitle: "Página no encontrada", error_404_description1: "Parece que te has perdido en el tiempo.", error_404_description2: "¡Vuelve al presente para disfrutar del mejor sabor retro!", error_404_btn: "VOLVER AL INICIO",
        my_reservations_title: "Mis Reservas", no_active_reservations: "No tienes reservas activas.", go_to_reserve: "Ir a reservar", recent_orders: "Pedidos Recientes",
        no_recent_orders: "No tienes pedidos recientes.",
        admin_menu_crud: "Gestión Menú", admin_global_orders: "Pedidos Globales", admin_reservations: "Reservas", admin_users: "Usuarios", admin_exit: "Salir de Admin",
        admin_gest_menu: "Gestión del Menú", admin_add_plate: "+ Añadir Plato", admin_img: "IMG", admin_name: "Nombre", admin_price: "Precio", admin_status: "Estado", admin_actions: "Acciones",
        admin_active: "Activo", admin_inactive: "Inactivo", admin_edit: "Editar", admin_delete: "Eliminar", admin_new_plate: "Nuevo Plato", admin_desc: "Descripción", admin_img_file: "Imagen (archivo)",
        admin_add: "Añadir", admin_close: "Cerrar", admin_ref: "Ref", admin_client: "Cliente", admin_total: "Total", admin_date: "Fecha", admin_action: "Acción", admin_user: "Usuario",
        admin_nickname: "Apodo", admin_role: "Rol", admin_save: "Guardar Cambios", admin_cancel: "Cancelar", admin_active_menu: "¿Activo en el menú?",
        err_past_date: "Error: No puedes reservar para una fecha pasada.", label_id: "ID", view_details: "Ver detalles &rarr;", checkout_btn: "Realizar Pedido",
        current_basket: "Cesta Actual", quantity_label: "Cantidad", explore_menu: "Explorar Menú", empty_basket: "Tu cesta está vacía.",
        receipt_order_id: "Pedido #", receipt_total: "Total:", receipt_date: "Fecha:", receipt_items: "Productos:", receipt_thanks: "¡Gracias por tu visita!", receipt_keep_retro: "Mantente Retro.",
        item_burger: "Hamburguesa Retro", item_pizza: "Pizza Clásica", item_wrap: "Wrap de Pollo", item_fries: "Papas Crujientes", item_shake: "Batido Vintage", item_nachos: "Nachos Arcade",
        desc_burger: "Doble hamburguesa clásica con queso derretido, lechuga y salsa secreta.", desc_fries: "Papas fritas crujientes sazonadas con nuestra mezcla especial retro.",
        desc_milkshake: "Batido espeso de vainilla y fresa con crema batida y cereza.", desc_pancakes: "Pancakes esponjosos con mantequilla derretida y miel de maple.",
        desc_pizza: "Porción de pizza con queso y pepperoni horneada estilo clásico.", desc_nachos: "Nachos cargados con jalapeños, queso derretido y salsa.",
        desc_wrap: "Pollo a la parrilla con verduras frescas y salsa de yogur y ajo.", desc_ramen: "Caldo rico con fideos, huevo tierno y toppings clásicos.", desc_sundae: "Tres bolas de nostalgia con chocolate y chispas."
    },
    ua: {
        nav_home: "Головна", nav_menu: "Меню", nav_login: "Увійти", nav_register: "Реєстрація", nav_orders: "Замовлення", nav_reserved: "Резерв", nav_logout: "Вийти", nav_admin: "Адмін",
        hero_title: "Ласкаво просимо до RetroBite", hero_subtitle: "Скуштуйте ностальгічні смаки минулого у сучасному виконанні.", hero_cta: "Переглянути меню",
        menu_title: "Їжа з минулого", add_to_cart: "Додати в кошик", order_now: "Замовити зараз",
        login_title: "З поверненням", login_btn: "Увійти", register_title: "Приєднуйся до клубу", register_btn: "Реєстрація",
        username_label: "Нікнейм", email_label: "Електронна пошта", password_label: "Пароль", name_label: "Повне ім'я",
        invoice_title: "Чек RetroBite", invoice_send: "Відправити на email", close: "Закрити",
        orders_title: "Мої Замовлення", my_orders_title: "Мої Замовлення", orders_empty: "Замовлень не знайдено.", recent_orders_title: "Історія Замовлень",
        total: "Всього", res_title: "Забронювати Столик", res_subtitle: "Відчуйте атмосферу ностальгії. Забронюйте столик вже сьогодні!",
        res_success: "Бронювання успішно надіслано! До зустрічі.", label_name: "Ім'я", label_email: "Email", label_phone: "Телефон", label_guests: "Гості",
        label_date: "Дата", label_time: "Час", label_table_type: "Тип Столика", table_regular: "Звичайний столик", table_booth: "Затишна кабінка", table_window: "Місце біля вікна", table_outdoor: "Тераса",
        btn_reserve: "Підтвердити", btn_reserve_more: "Бронювати ще", btn_delete: "Видалити", confirm_delete_res: "Ви впевнені, що хочете видалити це бронювання?",
        order_id: "Замовлення #", status_delivered: "Доставлено", status_preparing: "Готується", status_onway: "В дорозі", weight_label: "Вага", ingredients_label: "Інгредієнти",
        description_label: "Опис:", back_to_menu: "До Меню", checkout_title: "Оформлення", btn_confirm_order: "Підтвердити", empty_basket_checkout: "Ваш кошик порожній.",
        add_more_items: "Додати ще товари", login_footer: "Немає акаунту? ", register_footer: "Вже є акаунт? ", login_link: "Увійти", register_link: "Реєстрація",
        error_404_subtitle: "Сторінку не знайдено", error_404_description1: "Схоже, ви загубилися в часі.", error_404_description2: "Поверніться в сьогодення за найкращим ретро смаком!", error_404_btn: "НА ГОЛОВНУ",
        my_reservations_title: "Мої Бронювання", no_active_reservations: "У вас немає активних бронювань.", go_to_reserve: "Забронювати", recent_orders: "Останні замовлення",
        no_recent_orders: "У вас немає останніх замовлень.",
        admin_menu_crud: "Управління Меню", admin_global_orders: "Всі Замовлення", admin_reservations: "Бронювання", admin_users: "Користувачі", admin_exit: "Вийти з Адмінки",
        admin_gest_menu: "Управління Меню", admin_add_plate: "+ Додати Страву", admin_img: "Зображення", admin_name: "Назва", admin_price: "Ціна", admin_status: "Статус", admin_actions: "Дії",
        admin_active: "Активно", admin_inactive: "Неактивно", admin_edit: "Редагувати", admin_delete: "Видалити", admin_new_plate: "Нова Страва", admin_desc: "Опис", admin_img_file: "Зображення (файл)",
        admin_add: "Додати", admin_close: "Закрити", admin_ref: "№", admin_client: "Клієнт", admin_total: "Всього", admin_date: "Дата", admin_action: "Дія", admin_user: "Користувач",
        admin_nickname: "Нікнейм", admin_role: "Роль", admin_save: "Зберегти Зміни", admin_cancel: "Скасувати", admin_active_menu: "Активно в меню?",
        err_past_date: "Помилка: Не можна бронювати на минулу дату.", label_id: "ID", view_details: "Детальніше &rarr;", checkout_btn: "Замовити Зараз",
        current_basket: "Поточний Кошик", quantity_label: "Кількість", explore_menu: "Переглянути Меню", empty_basket: "Ваш кошик порожній.",
        receipt_order_id: "Замовлення №", receipt_total: "Разом:", receipt_date: "Дата:", receipt_items: "Товари:", receipt_thanks: "Дякуємо за візит!", receipt_keep_retro: "Залишайся в стилі Ретро.",
        item_burger: "Ретро Бургер", item_pizza: "Класична Піца", item_wrap: "Рол з Куркою", item_fries: "Хрустка Фрі", item_shake: "Вінтажний Шейк", item_nachos: "Аркадні Начос",
        desc_burger: "Класична подвійна котлета з сиром, салатом та секретним соусом.", desc_fries: "Хрустка картопля фрі з нашими фірмовими ретро спеціями.",
        desc_milkshake: "Густий ванільно-полуничний шейк зі збитими вершками та вишнею.", desc_pancakes: "Пухкі млинці з маслом та кленовим сиропом.",
        desc_pizza: "Шматочок піци з пепероні, випеченої у класичній печі.", desc_nachos: "Кукурудзяні чипси з халапеньйо, сиром та сальсою.",
        desc_wrap: "Ніжна курка гриль зі свіжими овочами та часниковим соусом.", desc_ramen: "Насичений бульйон з локшиною, яйцем та класичними додатками.", desc_sundae: "Три кульки ностальгії з шоколадом та посипкою."
    }
};

class Translator {
    constructor() {
        this.currentLang = localStorage.getItem('language') || 'en';
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
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            const translation = translations[this.currentLang][key];
            if (translation) {
                if (el.tagName === 'INPUT' && el.hasAttribute('placeholder')) {
                    el.setAttribute('placeholder', translation);
                } else {
                    el.innerHTML = translation;
                }
            }
        });
    }

    setupButtons() {
        document.querySelectorAll('.lang-btn').forEach(btn => {
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

document.addEventListener('DOMContentLoaded', () => {
    window.translator = new Translator();
});
