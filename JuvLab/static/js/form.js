const save_participant_btn = document.getElementById('save-student-btn');
save_participant_btn.addEventListener('click', () => {
    const first_name = document.getElementById('first-name');
    const last_name = document.getElementById('last-name');
    const email = document.getElementById('student-email');
    const phone = document.getElementById('student-phone');
    const program = document.getElementById('student-program');
    const dataToSend = {
        'first_name' : first_name.value,
        'last_name': last_name.value,
        'email': email.value,
        'phone': parseInt(phone.value),
        'program': program.value,
    }

    console.log(dataToSend)
})