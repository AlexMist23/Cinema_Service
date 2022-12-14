document.addEventListener("DOMContentLoaded", function(event){

    const seats_div = document.querySelector(".seats_list")
    const seats = document.querySelectorAll( 'div.seats_list a');

    let new_row = document.createElement("div")
    let row_symbol
    let row_num = 1

    seats.forEach(seat=>{
        if (seat.innerText % seat_rows === 1){
            row_symbol = document.createElement("p")
            row_symbol.classList.add("row-symbol")
            row_symbol.innerText = row_num.toString()
            new_row.appendChild(row_symbol)

        }
        new_row.classList.add("seats-row")
        new_row.appendChild(seat)
        if (seat.innerText % seat_rows === 0){
            row_symbol = document.createElement("p")
            row_symbol.classList.add("row-symbol")
            row_symbol.innerText = row_num.toString()
            new_row.appendChild(row_symbol)
            row_num++

            seats_div.appendChild(new_row)
            new_row = document.createElement("div")
            new_row.classList.add("seats-row")
        }
    })

    const free_seats = document.querySelectorAll('a.free')
    free_seats.forEach(seat =>{
        seat.addEventListener('click', event=>{
            seat.classList.toggle('selected')
        })
    })

    const reservation = document.querySelector('#reservation_btn')
    reservation.addEventListener('click', event=>{
        let selected_seats = document.querySelectorAll('.selected')
            if (selected_seats[0]){
                let seats = ''
                selected_seats.forEach(seat=>{
                    seats += seat.innerText + ','
                })
                window.location.href = seats;
            }

    })
})