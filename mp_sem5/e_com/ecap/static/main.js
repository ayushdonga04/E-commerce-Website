/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* Menu show */
navToggle.addEventListener('click', () =>{
   navMenu.classList.add('show-menu')
})

/* Menu hidden */
navClose.addEventListener('click', () =>{
   navMenu.classList.remove('show-menu')
})

/*=============== LOGIN ===============*/
const login = document.getElementById('login'),
      loginBtn = document.getElementById('login-btn'),
      loginClose = document.getElementById('login-close')

/* Login show */
loginBtn.addEventListener('click', () =>{
   login.classList.add('show-login')
})

/* Login hidden */
loginClose.addEventListener('click', () =>{
   login.classList.remove('show-login')
})

const openFormBtn = document.getElementById('openFormBtn');
    const closeFormBtn = document.getElementById('closeFormBtn');
    const myForm = document.getElementById('myForm');
    const overlay = document.getElementById('overlay');

    openFormBtn.onclick = function() {
        myForm.style.display = 'block';
        overlay.style.display = 'block';
    }

    closeFormBtn.onclick = function() {
        myForm.style.display = 'none';
        overlay.style.display = 'none';
    }

    overlay.onclick = function() {
        myForm.style.display = 'none';
        overlay.style.display = 'none';
    }


