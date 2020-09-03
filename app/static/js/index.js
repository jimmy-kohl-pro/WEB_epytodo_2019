const username = document.getElementById('name')
const password = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
    let messages = []
    if (name.value === '' || name.value == null) {
        messages.push('Name is required')
    }

    if (password.lenght <= 6) {
        messages.push('Password must be longer than 6 characters')
    }

    if (password.lenght >= 20) {
        messages.push('Password must be less than 20 characters')
    }

    if (password.value === 'password') {
        messages.push('Password cannot be password')
    }

    if (messages.lenght > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
})