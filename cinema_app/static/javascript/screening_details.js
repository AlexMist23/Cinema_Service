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
})