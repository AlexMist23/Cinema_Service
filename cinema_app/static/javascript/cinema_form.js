document.addEventListener("DOMContentLoaded", function(event){
    const city = document.querySelector("#id_city")
    const street = document.querySelector("#id_street")
    const postal_code = document.querySelector("#id_postal_code")
    const email = document.querySelector("#id_email")
    const telephone = document.querySelector("#id_telephone")
    city.placeholder = "Example: Warsaw"
    street.placeholder = "Example: ul. Example Street 132"
    postal_code.placeholder = "Example: 12-345"
    email.placeholder = "Example: address@emial.com"
    telephone.placeholder = "Example: 123456789"
})