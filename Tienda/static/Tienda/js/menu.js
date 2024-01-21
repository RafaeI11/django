// Función para darle estilo al scroll
const nav = document.querySelector('.nav');
window.addEventListener('scroll', function () {
    nav.classList.toggle('active', window.scrollY > 0)
})

