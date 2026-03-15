document.addEventListener('DOMContentLoaded', () => {
    // Animación de Logo
    const logo = document.querySelector('.logo');
    logo.addEventListener('click', (e) => {
        e.preventDefault();
        logo.classList.add('neon-flash');
        setTimeout(() => {
            window.location.href = "home.html";
        }, 500);
    });

    // Toggle Login / Registro
    const btnLogin = document.getElementById('btn-login-tab');
    const btnReg = document.getElementById('btn-reg-tab');
    const formLogin = document.getElementById('form-login');
    const formReg = document.getElementById('form-reg');

    if(btnLogin) {
        btnLogin.addEventListener('click', () => {
            formLogin.classList.remove('hidden');
            formReg.classList.add('hidden');
            btnLogin.classList.add('active');
            btnReg.classList.remove('active');
        });

        btnReg.addEventListener('click', () => {
            formLogin.classList.add('hidden');
            formReg.classList.remove('hidden');
            btnReg.classList.add('active');
            btnLogin.classList.remove('active');
        });
    }
});

// Simulación de envío de factura por email
function sendInvoice() {
    alert("Invoice generated! A copy has been sent to your registered email (Placeholder).");
}