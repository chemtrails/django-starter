const visOn = document.querySelector('#vis-on')
const visOff = document.querySelector('#vis-off')
const password1 = document.querySelector('#password1')
const password2 = document.querySelector('#password2')

function showPassword(visible) {
    if (visible === true) {
        visOn.style.display = 'none'
        visOff.style.display = 'block'
        password1.type = 'password'
        if (password2) password2.type = 'password'
        return
    }
    visOn.style.display = 'block'
    visOff.style.display = 'none'
    password1.type = 'text'
    if (password2) password2.type = 'text'
}