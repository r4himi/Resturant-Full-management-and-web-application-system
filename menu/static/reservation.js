const form = document.getElementById("reservationForm");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    emailjs.sendForm(
        "service_jwjo3ov",
        "template_knk2lcy",
        this
    ).then (()=> {

        emailjs.sendForm(
            "service_jwjo3ov",
            "template_q6000e6",
            this
        ).then(()=> {
            alert("Reservation successful! Emails sent to customer and admin.");
            form.reset();
        });


    }).catch((error)=> {
        console.error("EmailJS error:", error);
        alert("Failed to send reservation. please try again.")
    });
});


