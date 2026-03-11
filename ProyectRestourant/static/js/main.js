// Main script for general interactions
document.addEventListener('DOMContentLoaded', () => {

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Handle Buy Food / Add to Cart example triggers for Invoice popup
    const orderBtns = document.querySelectorAll('.trigger-order');
    orderBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const itemName = btn.dataset.item;
            const itemPrice = parseFloat(btn.dataset.price);

            // Mock order data
            const orderData = {
                items: [
                    { name: itemName, price: itemPrice, quantity: 1 }
                ]
            };

            if (window.invoiceSystem) {
                window.invoiceSystem.show(orderData);
            }
        });
    });
});
