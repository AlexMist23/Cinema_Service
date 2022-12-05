document.addEventListener("DOMContentLoaded", function(event){
    const city = document.querySelector("#id_city")
    const street = document.querySelector("#id_street")
    const postal_code = document.querySelector("#id_postal_code")
    const email = document.querySelector("#id_email")
    const telephone = document.querySelector("#id_telephone")
    const form = document.querySelector("form")
    city.placeholder = "E. g. Warsaw"
    street.placeholder = "E. g. ul. Example Street 132"
    postal_code.placeholder = "E. g. 12-345"
    email.placeholder = "E. g. address@emial.com"
    telephone.placeholder = "E. g. 123456789"
})