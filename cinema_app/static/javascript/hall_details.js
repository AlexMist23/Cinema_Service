document.addEventListener("DOMContentLoaded", function(event){

    const seats_div = document.querySelector(".seats_list")
    const seats = document.querySelectorAll( 'div.seats_list a');

    let new_row = document.createElement("div")
    seats.forEach(seat=>{
        new_row.classList.add("seats-row")
        new_row.appendChild(seat)
        if (seat.innerText % seat_rows === 0){
            seats_div.appendChild(new_row)
            new_row = document.createElement("div")
            new_row.classList.add("seats-row")
        }
    })
})