document.addEventListener("DOMContentLoaded", function(event){

    const seats_div = document.querySelector(".seats_list")

    for (let x = 1; x <= (seat_columns * seat_rows); x = x + seat_columns)
    {
        let new_row = document.createElement("div")
        new_row.classList.add("seats-row")
        for (let i = 1; i <= seat_rows; i++)
        {
            let new_seat = document.createElement("div")
            new_seat.innerText = ((i + x)-1).toString()
            new_seat.classList.add("seat")
            new_row.appendChild(new_seat)
        }
        seats_div.appendChild(new_row)

    }
})