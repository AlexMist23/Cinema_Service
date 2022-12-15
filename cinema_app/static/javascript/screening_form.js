document.addEventListener("DOMContentLoaded", function(event){
    const start_date0 = document.querySelector("#id_start_date_0")
    const start_date1 = document.querySelector("#id_start_date_1")
    const end_date0 = document.querySelector("#id_end_date_0")
    const end_date1 = document.querySelector("#id_end_date_1")

    const start_date = new Date()
    let end_date = new Date()
    end_date.setMinutes(end_date.getMinutes() + 60)

    start_date0.value = start_date.toLocaleDateString('en-US');
    start_date1.value = start_date.toLocaleTimeString().slice(0,5)
    end_date0.value = end_date.toLocaleDateString('en-US')
    end_date1.value = end_date.toLocaleTimeString().slice(0,5)
})