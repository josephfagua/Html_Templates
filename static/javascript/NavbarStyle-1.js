<!--
    This javascript file was developed by the Crattivo Department of Gocreattivo.
    It is designed to perform the necessary functions required by the NavbarStyle-1.html template.
    Our team specializes in Full Stack Development, Database Management, API Integration,
    Frontend & Backend Coordination, and Code Optimization.
    Gocreattivo is committed to delivering user-friendly, high-performance web solutions.
-->

function toggleNav() {
    document.body.classList.toggle("mobile-nav-open");
}
document.addEventListener('scroll', () =>{
    const header = document.querySelector('header');
    if (window.scrollY >0){
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
})