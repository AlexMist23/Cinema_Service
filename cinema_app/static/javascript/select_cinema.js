document.addEventListener("DOMContentLoaded", function(event){
    const select_label = document.querySelector("#select-cinema form p label")
    const select_input = document.querySelector("#select-cinema form select")
    const form = document.querySelector('form')
    const title = document.querySelector('#select-cinema-p')

    select_label.style.display='None'
    if (!select_input.value){
        form.style.display='None'
        title.innerText = 'No Cinemas in Database ||| Please Add Cinema'
    }
})