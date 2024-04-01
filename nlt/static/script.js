const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.signup-link');
const regisLink = document.querySelector('.signin-link');
const Popup = document.querySelector('#login');
const iconClose = document.querySelector('.icon-close');

loginLink.onclick = () => {
    wrapper.classList.add('active');
};

regisLink.onclick = () => {
    wrapper.classList.remove('active');
};

Popup.onclick = () => {
    wrapper.classList.add('active-popup');
};

iconClose.onclick = () => {
    wrapper.classList.remove('active-popup');
};
