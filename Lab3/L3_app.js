
const count = document.querySelector('.count')
const input = document.querySelector('input')
input.addEventListener('keyup', () => {
    count.innerText = input.value.length
})
